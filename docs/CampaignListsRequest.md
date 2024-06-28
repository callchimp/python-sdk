# CampaignListsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Campaign and list name | 
**phone_number** | **int** | Phone number foreign key | 
**type** | **str** |  | 
**transaction_template** | **str** |  | [optional] 
**description** | **str** |  | [optional] 

## Example

```python
from callchimp.models.campaign_lists_request import CampaignListsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CampaignListsRequest from a JSON string
campaign_lists_request_instance = CampaignListsRequest.from_json(json)
# print the JSON string representation of the object
print(CampaignListsRequest.to_json())

# convert the object into a dict
campaign_lists_request_dict = campaign_lists_request_instance.to_dict()
# create an instance of CampaignListsRequest from a dict
campaign_lists_request_from_dict = CampaignListsRequest.from_dict(campaign_lists_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


