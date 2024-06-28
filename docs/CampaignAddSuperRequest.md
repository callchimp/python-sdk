# CampaignAddSuperRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**supervisors** | **List[int]** |  | [optional] 

## Example

```python
from callchimp.models.campaign_add_super_request import CampaignAddSuperRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CampaignAddSuperRequest from a JSON string
campaign_add_super_request_instance = CampaignAddSuperRequest.from_json(json)
# print the JSON string representation of the object
print(CampaignAddSuperRequest.to_json())

# convert the object into a dict
campaign_add_super_request_dict = campaign_add_super_request_instance.to_dict()
# create an instance of CampaignAddSuperRequest from a dict
campaign_add_super_request_from_dict = CampaignAddSuperRequest.from_dict(campaign_add_super_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


