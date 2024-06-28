# CampaignListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**current_page** | **int** |  | [optional] 
**results** | [**List[CampaignResponse]**](CampaignResponse.md) |  | [optional] 
**total_pages** | **int** |  | [optional] 

## Example

```python
from callchimp.models.campaign_list_response import CampaignListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CampaignListResponse from a JSON string
campaign_list_response_instance = CampaignListResponse.from_json(json)
# print the JSON string representation of the object
print(CampaignListResponse.to_json())

# convert the object into a dict
campaign_list_response_dict = campaign_list_response_instance.to_dict()
# create an instance of CampaignListResponse from a dict
campaign_list_response_from_dict = CampaignListResponse.from_dict(campaign_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


