# SubscriberRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **str** |  | 
**last_name** | **str** |  | 
**leadlist** | **int** |  | 
**phone_code** | **str** |  | 
**phone_number** | **str** |  | 

## Example

```python
from callchimp.models.subscriber_request import SubscriberRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriberRequest from a JSON string
subscriber_request_instance = SubscriberRequest.from_json(json)
# print the JSON string representation of the object
print SubscriberRequest.to_json()

# convert the object into a dict
subscriber_request_dict = subscriber_request_instance.to_dict()
# create an instance of SubscriberRequest from a dict
subscriber_request_form_dict = subscriber_request.from_dict(subscriber_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


