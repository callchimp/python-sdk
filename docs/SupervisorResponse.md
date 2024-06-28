# SupervisorResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**added_at** | **datetime** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**organization** | **int** |  | [optional] 
**otp** | **int** |  | [optional] 
**otp_created_at** | **datetime** |  | [optional] 
**otp_verified** | **bool** |  | [optional] 
**phone** | **str** |  | [optional] 
**priority** | **int** |  | [optional] 

## Example

```python
from callchimp.models.supervisor_response import SupervisorResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SupervisorResponse from a JSON string
supervisor_response_instance = SupervisorResponse.from_json(json)
# print the JSON string representation of the object
print(SupervisorResponse.to_json())

# convert the object into a dict
supervisor_response_dict = supervisor_response_instance.to_dict()
# create an instance of SupervisorResponse from a dict
supervisor_response_from_dict = SupervisorResponse.from_dict(supervisor_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


