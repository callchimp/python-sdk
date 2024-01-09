# ListsListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**current_page** | **int** |  | [optional] 
**results** | [**List[ListsResponse]**](ListsResponse.md) |  | [optional] 
**total_pages** | **int** |  | [optional] 

## Example

```python
from callchimp.models.lists_list_response import ListsListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListsListResponse from a JSON string
lists_list_response_instance = ListsListResponse.from_json(json)
# print the JSON string representation of the object
print ListsListResponse.to_json()

# convert the object into a dict
lists_list_response_dict = lists_list_response_instance.to_dict()
# create an instance of ListsListResponse from a dict
lists_list_response_form_dict = lists_list_response.from_dict(lists_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


