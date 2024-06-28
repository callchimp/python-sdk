# CallsPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lead** | **int** | Lead Id | 
**transaction_audio_gender** | **str** | Gender of the generated voice | [optional] 
**transaction_vars** | **object** | Transaction variable values that should match the variables in campaign &#x60;transaction_template&#x60; | 
**vendor_lead_code** | **str** |  | 

## Example

```python
from callchimp.models.calls_post_request import CallsPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CallsPostRequest from a JSON string
calls_post_request_instance = CallsPostRequest.from_json(json)
# print the JSON string representation of the object
print(CallsPostRequest.to_json())

# convert the object into a dict
calls_post_request_dict = calls_post_request_instance.to_dict()
# create an instance of CallsPostRequest from a dict
calls_post_request_from_dict = CallsPostRequest.from_dict(calls_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


