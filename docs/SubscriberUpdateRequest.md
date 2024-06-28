# SubscriberUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**leadlist** | **int** |  | [optional] 
**phone_code** | **str** |  | [optional] 
**phone_number** | **str** |  | [optional] 
**vendor_lead_code** | **str** |  | [optional] 

## Example

```python
from callchimp.models.subscriber_update_request import SubscriberUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriberUpdateRequest from a JSON string
subscriber_update_request_instance = SubscriberUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(SubscriberUpdateRequest.to_json())

# convert the object into a dict
subscriber_update_request_dict = subscriber_update_request_instance.to_dict()
# create an instance of SubscriberUpdateRequest from a dict
subscriber_update_request_from_dict = SubscriberUpdateRequest.from_dict(subscriber_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


