# CallListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**current_page** | **int** |  | [optional] 
**results** | [**List[CallResponse]**](CallResponse.md) |  | [optional] 
**total_pages** | **int** |  | [optional] 

## Example

```python
from callchimp.models.call_list_response import CallListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CallListResponse from a JSON string
call_list_response_instance = CallListResponse.from_json(json)
# print the JSON string representation of the object
print(CallListResponse.to_json())

# convert the object into a dict
call_list_response_dict = call_list_response_instance.to_dict()
# create an instance of CallListResponse from a dict
call_list_response_from_dict = CallListResponse.from_dict(call_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


