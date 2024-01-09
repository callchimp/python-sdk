# InboundCallResponseSupervisor


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**phone** | **str** |  | [optional] 
**priority** | **int** |  | [optional] 

## Example

```python
from callchimp.models.inbound_call_response_supervisor import InboundCallResponseSupervisor

# TODO update the JSON string below
json = "{}"
# create an instance of InboundCallResponseSupervisor from a JSON string
inbound_call_response_supervisor_instance = InboundCallResponseSupervisor.from_json(json)
# print the JSON string representation of the object
print InboundCallResponseSupervisor.to_json()

# convert the object into a dict
inbound_call_response_supervisor_dict = inbound_call_response_supervisor_instance.to_dict()
# create an instance of InboundCallResponseSupervisor from a dict
inbound_call_response_supervisor_form_dict = inbound_call_response_supervisor.from_dict(inbound_call_response_supervisor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


