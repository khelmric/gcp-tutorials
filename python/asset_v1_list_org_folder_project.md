# Python - Listing organization, folders and project by using the Asset Inventory API

## Overview
This tutorial helps to create a Python script, which will list the organization-, folder- and project resources by using the Asset Inventory API (asset_v1).

## Links
https://cloud.google.com/python/docs/reference/cloudasset/latest
https://cloud.google.com/asset-inventory/docs/supported-asset-types
https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-asset

**Time to complete**: <walkthrough-tutorial-duration duration="15"></walkthrough-tutorial-duration>

**Prerequisites**: 
- A Google Cloud Project
- A Billing Account linked to the Google Cloud Project
- Permissions on the Google Cloud Organization:
  - Cloud Asset Viewer (roles/cloudasset.viewer)

Click the **Start** button to move to the first step.



## Preparation - Setup Python environment
Here we'll setup the virtual environment for Python.

### Steps

### Go to the python snippets folder within the cloned repository
```bash
cd gcp-tutorials/python/snippets
```

<br/>

### Create and activate the virtual environment
```bash
python3 -m venv env
source env/bin/activate
```

<br/>

### Install the dependencies
```bash
pip install google-cloud-asset
```

<br/>

Click the **Next** button to move to the next step.


## Set the required variables as environment parameter
The value for the Organization ID has to be updated to your target Organization ID.

### Set Org ID
```bash
export ORG_ID=123456789
```
<br/>

Click the **Next** button to move to the next step.


## Execute the Python script
Executing the Python script to get the required outputs.

### Run Python script
```bash
python asset_v1_list_org_folder_project.py
```

Click the **Next** button to move to the next step.



## Congratulations
<walkthrough-conclusion-trophy></walkthrough-conclusion-trophy>

You listed the project, folder and organization resources of your GCP Organization.

Done!
