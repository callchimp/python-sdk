# CallReportResponseAnsweredCalls


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current** | **int** |  | [optional] 
**past** | **int** |  | [optional] 

## Example

```python
from callchimp.models.call_report_response_answered_calls import CallReportResponseAnsweredCalls

# TODO update the JSON string below
json = "{}"
# create an instance of CallReportResponseAnsweredCalls from a JSON string
call_report_response_answered_calls_instance = CallReportResponseAnsweredCalls.from_json(json)
# print the JSON string representation of the object
print CallReportResponseAnsweredCalls.to_json()

# convert the object into a dict
call_report_response_answered_calls_dict = call_report_response_answered_calls_instance.to_dict()
# create an instance of CallReportResponseAnsweredCalls from a dict
call_report_response_answered_calls_form_dict = call_report_response_answered_calls.from_dict(call_report_response_answered_calls_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


