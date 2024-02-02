import os
from google.cloud import asset_v1

# Create client
client = asset_v1.AssetServiceClient()

# Set filter for the asset types
filter_asset_types = ["cloudresourcemanager.googleapis.com/Project", "cloudresourcemanager.googleapis.com/Folder", "cloudresourcemanager.googleapis.com/Organization"]

# Initialize request argument
request = asset_v1.SearchAllResourcesRequest(
    scope="organizations/" + os.environ['ORG_ID'],
    asset_types = filter_asset_types,
)

# Make the request
page_result = client.search_all_resources(request=request)

# Handle the response
for response in page_result:
    print(response)