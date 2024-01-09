# SupervisorRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**phone** | **str** |  | 
**priority** | **int** |  | 

## Example

```python
from callchimp.models.supervisor_request import SupervisorRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SupervisorRequest from a JSON string
supervisor_request_instance = SupervisorRequest.from_json(json)
# print the JSON string representation of the object
print SupervisorRequest.to_json()

# convert the object into a dict
supervisor_request_dict = supervisor_request_instance.to_dict()
# create an instance of SupervisorRequest from a dict
supervisor_request_form_dict = supervisor_request.from_dict(supervisor_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


