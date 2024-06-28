# CallReportResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**answered_calls** | [**CallReportResponseAnsweredCalls**](CallReportResponseAnsweredCalls.md) |  | [optional] 
**campaigns_count** | **int** |  | [optional] 
**queued_calls** | [**CallReportResponseAnsweredCalls**](CallReportResponseAnsweredCalls.md) |  | [optional] 
**stats** | [**List[CallReportResponseStatsInner]**](CallReportResponseStatsInner.md) |  | [optional] 
**total_calls** | [**CallReportResponseAnsweredCalls**](CallReportResponseAnsweredCalls.md) |  | [optional] 
**total_duration** | [**CallReportResponseAnsweredCalls**](CallReportResponseAnsweredCalls.md) |  | [optional] 

## Example

```python
from callchimp.models.call_report_response import CallReportResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CallReportResponse from a JSON string
call_report_response_instance = CallReportResponse.from_json(json)
# print the JSON string representation of the object
print(CallReportResponse.to_json())

# convert the object into a dict
call_report_response_dict = call_report_response_instance.to_dict()
# create an instance of CallReportResponse from a dict
call_report_response_from_dict = CallReportResponse.from_dict(call_report_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


