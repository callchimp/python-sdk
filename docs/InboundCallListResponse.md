# InboundCallListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**current_page** | **int** |  | [optional] 
**results** | [**List[InboundCallResponse]**](InboundCallResponse.md) |  | [optional] 
**total_pages** | **int** |  | [optional] 

## Example

```python
from callchimp.models.inbound_call_list_response import InboundCallListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of InboundCallListResponse from a JSON string
inbound_call_list_response_instance = InboundCallListResponse.from_json(json)
# print the JSON string representation of the object
print InboundCallListResponse.to_json()

# convert the object into a dict
inbound_call_list_response_dict = inbound_call_list_response_instance.to_dict()
# create an instance of InboundCallListResponse from a dict
inbound_call_list_response_form_dict = inbound_call_list_response.from_dict(inbound_call_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


