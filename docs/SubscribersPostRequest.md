# SubscribersPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **str** |  | 
**last_name** | **str** |  | 
**leadlist** | **int** |  | 
**phone_code** | **str** |  | 
**phone_number** | **str** |  | 
**vendor_lead_code** | **str** |  | [optional] 

## Example

```python
from callchimp.models.subscribers_post_request import SubscribersPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SubscribersPostRequest from a JSON string
subscribers_post_request_instance = SubscribersPostRequest.from_json(json)
# print the JSON string representation of the object
print(SubscribersPostRequest.to_json())

# convert the object into a dict
subscribers_post_request_dict = subscribers_post_request_instance.to_dict()
# create an instance of SubscribersPostRequest from a dict
subscribers_post_request_from_dict = SubscribersPostRequest.from_dict(subscribers_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


