# SubscriberResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**status** | **str** |  | [optional] 
**user** | **int** |  | [optional] 
**vendor_lead_code** | **str** |  | [optional] 
**source_id** | **str** |  | [optional] 
**gmt_offset_now** | **int** | Integer milisecond offset for call place | [optional] 
**called_since_last_reset** | **str** |  | [optional] 
**phone_code** | **str** |  | [optional] 
**phone_number** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**first_name** | **str** |  | [optional] 
**middle_initial** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**address1** | **str** |  | [optional] 
**address2** | **str** |  | [optional] 
**address3** | **str** |  | [optional] 
**city** | **str** |  | [optional] 
**state** | **str** |  | [optional] 
**province** | **str** |  | [optional] 
**postal_code** | **str** |  | [optional] 
**country_code** | **str** |  | [optional] 
**gender** | **str** |  | [optional] 
**date_of_birth** | **str** |  | [optional] 
**alt_phone** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**comments** | **str** |  | [optional] 
**called_count** | **int** |  | [optional] 
**last_local_call_time** | **int** |  | [optional] 
**rank** | **str** |  | [optional] 
**custom_data** | **str** |  | [optional] 
**owner** | **str** |  | [optional] 
**origin_type** | **str** |  | [optional] 
**leadlist** | **int** | Leadlist foreign key | [optional] 
**upload** | **int** | Upload foreign key | [optional] 
**organization** | **int** | Organization foreign key | [optional] 

## Example

```python
from callchimp.models.subscriber_response import SubscriberResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriberResponse from a JSON string
subscriber_response_instance = SubscriberResponse.from_json(json)
# print the JSON string representation of the object
print SubscriberResponse.to_json()

# convert the object into a dict
subscriber_response_dict = subscriber_response_instance.to_dict()
# create an instance of SubscriberResponse from a dict
subscriber_response_form_dict = subscriber_response.from_dict(subscriber_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


