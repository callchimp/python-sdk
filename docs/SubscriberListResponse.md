# SubscriberListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**current_page** | **int** |  | [optional] 
**results** | [**List[SubscriberResponse]**](SubscriberResponse.md) |  | [optional] 
**total_pages** | **int** |  | [optional] 

## Example

```python
from callchimp.models.subscriber_list_response import SubscriberListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriberListResponse from a JSON string
subscriber_list_response_instance = SubscriberListResponse.from_json(json)
# print the JSON string representation of the object
print SubscriberListResponse.to_json()

# convert the object into a dict
subscriber_list_response_dict = subscriber_list_response_instance.to_dict()
# create an instance of SubscriberListResponse from a dict
subscriber_list_response_form_dict = subscriber_list_response.from_dict(subscriber_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


