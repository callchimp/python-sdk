# CampaignResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**added_at** | **datetime** |  | [optional] 
**bot_language** | **str** |  | [optional] 
**chat_script** | **str** | Script for AI campaigns | [optional] 
**customer_language** | **str** | Expected language of the leads | [optional] 
**id** | **int** |  | [optional] 
**is_active** | **bool** |  | [optional] 
**is_recording** | **bool** | If active for AI campaigns, records all calls | [optional] 
**max_retry** | **int** | How many times call should be retried if not picked up | [optional] 
**name** | **str** |  | [optional] 
**organization** | **int** | Organization foreign key | [optional] 
**phone_number** | **int** | PhoneNumber foreign key | [optional] 
**supervisors** | **List[int]** | List of supervisor foreign keys | [optional] 
**type** | **str** | Type of campaign | [optional] 

## Example

```python
from callchimp.models.campaign_response import CampaignResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CampaignResponse from a JSON string
campaign_response_instance = CampaignResponse.from_json(json)
# print the JSON string representation of the object
print(CampaignResponse.to_json())

# convert the object into a dict
campaign_response_dict = campaign_response_instance.to_dict()
# create an instance of CampaignResponse from a dict
campaign_response_from_dict = CampaignResponse.from_dict(campaign_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


