# CallReportRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_from** | **int** | Unix timestamp in milliseconds, start of range. | 
**to** | **int** | Unix timestamp in milliseconds, end of range. | 
**campaign** | **int** | Campaign foreign key, only use when report is required for a specific campaign. | [optional] 

## Example

```python
from callchimp.models.call_report_request import CallReportRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CallReportRequest from a JSON string
call_report_request_instance = CallReportRequest.from_json(json)
# print the JSON string representation of the object
print CallReportRequest.to_json()

# convert the object into a dict
call_report_request_dict = call_report_request_instance.to_dict()
# create an instance of CallReportRequest from a dict
call_report_request_form_dict = call_report_request.from_dict(call_report_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


