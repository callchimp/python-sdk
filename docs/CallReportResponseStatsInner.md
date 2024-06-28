# CallReportResponseStatsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** |  | [optional] 
**total** | **int** |  | [optional] 

## Example

```python
from callchimp.models.call_report_response_stats_inner import CallReportResponseStatsInner

# TODO update the JSON string below
json = "{}"
# create an instance of CallReportResponseStatsInner from a JSON string
call_report_response_stats_inner_instance = CallReportResponseStatsInner.from_json(json)
# print the JSON string representation of the object
print(CallReportResponseStatsInner.to_json())

# convert the object into a dict
call_report_response_stats_inner_dict = call_report_response_stats_inner_instance.to_dict()
# create an instance of CallReportResponseStatsInner from a dict
call_report_response_stats_inner_from_dict = CallReportResponseStatsInner.from_dict(call_report_response_stats_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


