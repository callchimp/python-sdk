# CampaignFindRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query** | **str** |  | [optional] 

## Example

```python
from callchimp.models.campaign_find_request import CampaignFindRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CampaignFindRequest from a JSON string
campaign_find_request_instance = CampaignFindRequest.from_json(json)
# print the JSON string representation of the object
print(CampaignFindRequest.to_json())

# convert the object into a dict
campaign_find_request_dict = campaign_find_request_instance.to_dict()
# create an instance of CampaignFindRequest from a dict
campaign_find_request_from_dict = CampaignFindRequest.from_dict(campaign_find_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


