# CampaignUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**max_retry** | **int** | How many times call should be retried if not picked up | [optional] 
**phone_number** | **int** | PhoneNumber foreign key | [optional] 
**type** | **str** | Type of campaign | [optional] 
**transaction_template** | **str** | Template text with variable placeholders, where variables are represented like &#x60;{var1}&#x60;. Only required for &#x60;transactional&#x60; campaigns. | [optional] 
**script** | **int** | Script id, Can be found from the Script Listing API. This is the GenAI prompt telling the bot how to behave when asked a question or how to continue the conversation. | [optional] 
**voice** | **int** | Voice id. Can be found from the Voice Listing API. Head over to [Voice Garden](https://voices.callchimp.ai/) by Callchimp for samples. | [optional] 

## Example

```python
from callchimp.models.campaign_update_request import CampaignUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CampaignUpdateRequest from a JSON string
campaign_update_request_instance = CampaignUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(CampaignUpdateRequest.to_json())

# convert the object into a dict
campaign_update_request_dict = campaign_update_request_instance.to_dict()
# create an instance of CampaignUpdateRequest from a dict
campaign_update_request_from_dict = CampaignUpdateRequest.from_dict(campaign_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


