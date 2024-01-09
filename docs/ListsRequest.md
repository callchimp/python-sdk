# ListsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**campaign** | **int** | Campaign foreign key | 
**description** | **str** |  | [optional] 
**name** | **str** |  | 

## Example

```python
from callchimp.models.lists_request import ListsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ListsRequest from a JSON string
lists_request_instance = ListsRequest.from_json(json)
# print the JSON string representation of the object
print ListsRequest.to_json()

# convert the object into a dict
lists_request_dict = lists_request_instance.to_dict()
# create an instance of ListsRequest from a dict
lists_request_form_dict = lists_request.from_dict(lists_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


