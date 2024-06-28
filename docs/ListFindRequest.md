# ListFindRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query** | **str** |  | [optional] 

## Example

```python
from callchimp.models.list_find_request import ListFindRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ListFindRequest from a JSON string
list_find_request_instance = ListFindRequest.from_json(json)
# print the JSON string representation of the object
print(ListFindRequest.to_json())

# convert the object into a dict
list_find_request_dict = list_find_request_instance.to_dict()
# create an instance of ListFindRequest from a dict
list_find_request_from_dict = ListFindRequest.from_dict(list_find_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


