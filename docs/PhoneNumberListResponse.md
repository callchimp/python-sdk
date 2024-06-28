# PhoneNumberListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**current_page** | **int** |  | [optional] 
**results** | [**List[PhoneNumberResponse]**](PhoneNumberResponse.md) |  | [optional] 
**total_pages** | **int** |  | [optional] 

## Example

```python
from callchimp.models.phone_number_list_response import PhoneNumberListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PhoneNumberListResponse from a JSON string
phone_number_list_response_instance = PhoneNumberListResponse.from_json(json)
# print the JSON string representation of the object
print(PhoneNumberListResponse.to_json())

# convert the object into a dict
phone_number_list_response_dict = phone_number_list_response_instance.to_dict()
# create an instance of PhoneNumberListResponse from a dict
phone_number_list_response_from_dict = PhoneNumberListResponse.from_dict(phone_number_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


