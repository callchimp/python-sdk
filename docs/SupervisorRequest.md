# SupervisorRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the supervisor | 
**phone** | **str** | [E.164](https://www.twilio.com/docs/glossary/what-e164) formatted phone number of supervisor.  | 
**priority** | **int** | Priority of supervisor in the queue | 
**organization** | **int** | Current organization id. Can be found in the Callchimp [Settings](https://callchimp.ai/settings) -&gt; Organization tab -&gt; Org ID Column. | [optional] 

## Example

```python
from callchimp.models.supervisor_request import SupervisorRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SupervisorRequest from a JSON string
supervisor_request_instance = SupervisorRequest.from_json(json)
# print the JSON string representation of the object
print(SupervisorRequest.to_json())

# convert the object into a dict
supervisor_request_dict = supervisor_request_instance.to_dict()
# create an instance of SupervisorRequest from a dict
supervisor_request_from_dict = SupervisorRequest.from_dict(supervisor_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


