# Compute Engine with CMEK via Terraform

## Overview
This guide will show you how to create a Compute Engine by encrypting the boot disk with a CMEK/CSEK Key.

**Time to complete**: <walkthrough-tutorial-duration duration="10"></walkthrough-tutorial-duration>

**Prerequisites**: 
- A Google Cloud Project
- A Billing Account linked to the Google Cloud Project
- An existing CMEK or CSEK Key
- Permissions on the Google Cloud Project:
  - Enable Services
  - Grant IAM permission to the Service Account
  - Create Compute Engine instance
- Permissions on the KMS Key:
  - Grant IAM permission on the KMS Key

Click the **Start** button to move to the first step.



## Preparation - Local folder
In this step we will create the folder for the Terraform code in your Cloud Shell home directory.

### Steps

### Create a folder for your terraform code in your home directory
```bash
mkdir -p ~/gce_cmek
```

<br/>

### Go to the folder
```bash
cd ~/gce_cmek
```

Click the **Next** button to move to the next step.



## Preparation - terraform.tfvars
Create the `terraform.tfvars` file and set the required input variables for Terraform.

### Create the terraform.tfvars file
```bash
vi terraform.tfvars
```
<br/>

### Set the required values
Copy this content to the file and update values to set the required variables:
```terraform
project_id          = "<MY_PROJECT_ID>"
project_number      = "<MY_PROJECT_NUMBER>"
zone                = "<MY_ZONE>"
kms_project         = "<KMS_PROJECT_ID>"
kms_region          = "<KMS_REGION>"
kms_keyring         = "<KMS_KEYRING_NAME>"
kms_key             = "<KMS_KEY_NAME>"
```
Click the **Next** button to move to the next step.



## Preparation - variables.tf
Create the `variables.tf` file to declare variables for Terraform.

### Create the variables.tf file
```bash
vi variables.tf
```
<br/>

### Declare required variables
Copy this content to the file to declare the required variables:
```terraform
variable "project_id" {
  description = "My Project ID."
  type        = string
  default     = null
}

variable "project_number" {
  description = "My Project Number."
  type        = string
  default     = null
}

variable "billing_account" {
  description = "My Billing Account ID."
  type        = string
  default     = null
}

variable "zone" {
  description = "Zone where the GCE resources will be created."
  type        = string
  default     = null
}

variable "kms_project" {
  description = "Project ID of the KMS Key is located."
  type        = string
  default     = null
}

variable "kms_region" {
  description = "Region where the KMS Key is located."
  type        = string
  default     = null
}

variable "kms_keyring" {
  description = "The KMS Keyring name."
  type        = string
  default     = null
}

variable "kms_key" {
  description = "The KMS Key name."
  type        = string
  default     = null
}
```

Click the **Next** button to move to the next step.



## Preparation - providers.tf
Create the `providers.tf` file allow Terraform to interact with Google Cloud.

### Create the providers.tf file
```bash
vi providers.tf
```
<br/>

### Configure Google Cloud provider
Copy this content to the file to configure the Google Cloud provider:
```terraform
terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
    }
  }
}
```

Click the **Next** button to move to the next step.



## Preparation - main.tf
Create the `main.tf` file prepare the Project for the Compute Engine.

### Create the main.tf file
```bash
vi main.tf
```
<br/>

### Terraform script to prepare the Compute Engine
Copy this content to the file to prepare the Compute Engine:
```terraform
locals {
  kms_key_path = "projects/${var.kms_project}/locations/${var.kms_region}/keyRings/${var.kms_keyring}/cryptoKeys/${var.kms_key}"
}

resource "google_project_service" "project-services" {
  project = var.project_id
  for_each = toset([
    "compute.googleapis.com"
  ])
  service = each.key
}

resource "time_sleep" "waiting-for-service-account-creation" {
  create_duration = "30s"

  depends_on = [
    google_project_service.project-services
  ]
}
```

Click the **Next** button to move to the next step.



## Preparation - gce.tf
Create the `gce.tf` file create the Compute Engine.

### Create the gce.tf file
```bash
vi gce.tf
```
<br/>

### Terraform script to create the Compute Engine
Copy this content to the file to grant permission to the Compute Engine Service Account on the KMS Key and to create the Compute Engine:
```terraform
resource "google_kms_crypto_key_iam_member" "crypto_key_role_gce_sa" {
  crypto_key_id = "${var.kms_project}/${var.kms_region}/${var.kms_keyring}/${var.kms_key}"
  role          = "roles/cloudkms.cryptoKeyEncrypterDecrypter"
  member        = "serviceAccount:service-${var.project_number}@compute-system.iam.gserviceaccount.com"

  depends_on = [
    time_sleep.waiting-for-service-account-creation
  ]
}

resource "google_compute_instance" "gce-instance" {
  project      = var.project_id
  name         = "my-gce-instance"
  machine_type = "f1-micro"
  zone         = var.zone

  boot_disk {
    initialize_params {
      type  = "pd-balanced"
      image = "debian-cloud/debian-11"
    }
    kms_key_self_link = local.kms_key_path
  }

  network_interface {
    network = "default"
    access_config {
    }
  }

  depends_on = [
    google_kms_crypto_key_iam_member.crypto_key_role_gce_sa
  ]
}
```

Click the **Next** button to move to the next step.




## Deployment
Execute terraform command to deploy the Compute Engine

### Terraform init
```bash
terraform init
```

### Terraform plan
```bash
terraform plan
```

### Terraform apply
```bash
terraform apply
```

Click the **Next** button to move to the next step.



## Congratulations
<walkthrough-conclusion-trophy></walkthrough-conclusion-trophy>

You're all set!

You can now use your Compute Engine instance.

Done!
