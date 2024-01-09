# InboundCallResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**callchimp_number** | [**InboundCallResponseCallchimpNumber**](InboundCallResponseCallchimpNumber.md) |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**dial_status** | **str** |  | [optional] 
**duration** | **int** | Call duration in seconds | [optional] 
**hangup_cause** | [**InboundCallResponseHangupCause**](InboundCallResponseHangupCause.md) |  | [optional] 
**id** | **int** |  | [optional] 
**inbound_caller** | **str** |  | [optional] 
**is_answered** | **bool** |  | [optional] 
**organization** | **int** |  | [optional] 
**supervisor** | [**InboundCallResponseSupervisor**](InboundCallResponseSupervisor.md) |  | [optional] 
**supervisor_number** | [**InboundCallResponseHangupCause**](InboundCallResponseHangupCause.md) |  | [optional] 

## Example

```python
from callchimp.models.inbound_call_response import InboundCallResponse

# TODO update the JSON string below
json = "{}"
# create an instance of InboundCallResponse from a JSON string
inbound_call_response_instance = InboundCallResponse.from_json(json)
# print the JSON string representation of the object
print InboundCallResponse.to_json()

# convert the object into a dict
inbound_call_response_dict = inbound_call_response_instance.to_dict()
# create an instance of InboundCallResponse from a dict
inbound_call_response_form_dict = inbound_call_response.from_dict(inbound_call_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


