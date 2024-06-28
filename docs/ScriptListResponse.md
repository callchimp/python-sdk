# ScriptListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**current_page** | **int** |  | [optional] 
**results** | [**List[ScriptResponse]**](ScriptResponse.md) |  | [optional] 
**total_pages** | **int** |  | [optional] 

## Example

```python
from callchimp.models.script_list_response import ScriptListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ScriptListResponse from a JSON string
script_list_response_instance = ScriptListResponse.from_json(json)
# print the JSON string representation of the object
print(ScriptListResponse.to_json())

# convert the object into a dict
script_list_response_dict = script_list_response_instance.to_dict()
# create an instance of ScriptListResponse from a dict
script_list_response_from_dict = ScriptListResponse.from_dict(script_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


