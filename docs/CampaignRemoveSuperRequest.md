# CampaignRemoveSuperRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**supervisors** | **List[int]** |  | [optional] 

## Example

```python
from callchimp.models.campaign_remove_super_request import CampaignRemoveSuperRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CampaignRemoveSuperRequest from a JSON string
campaign_remove_super_request_instance = CampaignRemoveSuperRequest.from_json(json)
# print the JSON string representation of the object
print CampaignRemoveSuperRequest.to_json()

# convert the object into a dict
campaign_remove_super_request_dict = campaign_remove_super_request_instance.to_dict()
# create an instance of CampaignRemoveSuperRequest from a dict
campaign_remove_super_request_form_dict = campaign_remove_super_request.from_dict(campaign_remove_super_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


