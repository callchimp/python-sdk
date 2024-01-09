# WebhookRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**campaign** | **int** |  | [optional] 
**name** | **str** |  | 
**type** | **str** | For campaign type webhooks, &#x60;campaign&#x60; key is required. | 
**url** | **str** |  | 
**request_headers** | **str** |  | [optional] 

## Example

```python
from callchimp.models.webhook_request import WebhookRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookRequest from a JSON string
webhook_request_instance = WebhookRequest.from_json(json)
# print the JSON string representation of the object
print WebhookRequest.to_json()

# convert the object into a dict
webhook_request_dict = webhook_request_instance.to_dict()
# create an instance of WebhookRequest from a dict
webhook_request_form_dict = webhook_request.from_dict(webhook_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


