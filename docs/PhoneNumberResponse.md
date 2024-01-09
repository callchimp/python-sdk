# PhoneNumberResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | [optional] 
**description** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**number** | **str** | Outbound caller id in E.164 format, e.g. &#x60;[+][country_code][number]&#x60;. | [optional] 

## Example

```python
from callchimp.models.phone_number_response import PhoneNumberResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PhoneNumberResponse from a JSON string
phone_number_response_instance = PhoneNumberResponse.from_json(json)
# print the JSON string representation of the object
print PhoneNumberResponse.to_json()

# convert the object into a dict
phone_number_response_dict = phone_number_response_instance.to_dict()
# create an instance of PhoneNumberResponse from a dict
phone_number_response_form_dict = phone_number_response.from_dict(phone_number_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


