# ListsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**added_at** | **datetime** |  | [optional] 
**campaign** | **int** |  | [optional] 
**description** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**isactive** | **bool** |  | [optional] 
**isauto** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**organization** | **int** |  | [optional] 

## Example

```python
from callchimp.models.lists_response import ListsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListsResponse from a JSON string
lists_response_instance = ListsResponse.from_json(json)
# print the JSON string representation of the object
print ListsResponse.to_json()

# convert the object into a dict
lists_response_dict = lists_response_instance.to_dict()
# create an instance of ListsResponse from a dict
lists_response_form_dict = lists_response.from_dict(lists_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


