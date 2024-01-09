# CallResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**added_at** | **datetime** |  | [optional] 
**campaign** | **int** | Campaign foreign key | [optional] 
**dial_count** | **int** |  | [optional] 
**dial_status** | **str** | Status of how the call ended, read [more](https://www.voip-info.org/asterisk-variable-dialstatus/) | [optional] 
**disposition** | **str** | How the call is disposed, as defined in business logic | [optional] 
**duration** | **int** |  | [optional] 
**hangup_cause** | **str** | SIP code of call hangup, read [more](https://www.voip-info.org/asterisk-variable-hangupcause/) | [optional] 
**id** | **int** |  | [optional] 
**is_answered** | **bool** | Marks the call answered | [optional] 
**lead** | **int** | Lead foreign key | [optional] 
**organization** | **int** |  | [optional] 
**recording_path** | **str** |  | [optional] 
**started_at** | **datetime** |  | [optional] 

## Example

```python
from callchimp.models.call_response import CallResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CallResponse from a JSON string
call_response_instance = CallResponse.from_json(json)
# print the JSON string representation of the object
print CallResponse.to_json()

# convert the object into a dict
call_response_dict = call_response_instance.to_dict()
# create an instance of CallResponse from a dict
call_response_form_dict = call_response.from_dict(call_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


