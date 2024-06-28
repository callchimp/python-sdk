# SupervisorListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**current_page** | **int** |  | [optional] 
**results** | [**List[SupervisorResponse]**](SupervisorResponse.md) |  | [optional] 
**total_pages** | **int** |  | [optional] 

## Example

```python
from callchimp.models.supervisor_list_response import SupervisorListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SupervisorListResponse from a JSON string
supervisor_list_response_instance = SupervisorListResponse.from_json(json)
# print the JSON string representation of the object
print(SupervisorListResponse.to_json())

# convert the object into a dict
supervisor_list_response_dict = supervisor_list_response_instance.to_dict()
# create an instance of SupervisorListResponse from a dict
supervisor_list_response_from_dict = SupervisorListResponse.from_dict(supervisor_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


