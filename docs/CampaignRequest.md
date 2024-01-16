# CampaignRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**max_retry** | **int** | How many times call should be retried if not picked up | 
**phone_number** | **int** | PhoneNumber foreign key | 
**type** | **str** | Type of campaign | 
**transaction_template** | **str** | Template text with variable placeholders, where variables are represented like &#x60;{var1}&#x60;. Only required for &#x60;transactional&#x60; campaigns. | [optional] 
**chat_script** | **str** | The GenAI prompt telling the bot how to behave when asked a question or how to continue the conversation. | [optional] 

## Example

```python
from callchimp.models.campaign_request import CampaignRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CampaignRequest from a JSON string
campaign_request_instance = CampaignRequest.from_json(json)
# print the JSON string representation of the object
print CampaignRequest.to_json()

# convert the object into a dict
campaign_request_dict = campaign_request_instance.to_dict()
# create an instance of CampaignRequest from a dict
campaign_request_form_dict = campaign_request.from_dict(campaign_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


