# SupervisorVerifyOtpRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**otp** | **int** |  | [optional] 

## Example

```python
from callchimp.models.supervisor_verify_otp_request import SupervisorVerifyOtpRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SupervisorVerifyOtpRequest from a JSON string
supervisor_verify_otp_request_instance = SupervisorVerifyOtpRequest.from_json(json)
# print the JSON string representation of the object
print SupervisorVerifyOtpRequest.to_json()

# convert the object into a dict
supervisor_verify_otp_request_dict = supervisor_verify_otp_request_instance.to_dict()
# create an instance of SupervisorVerifyOtpRequest from a dict
supervisor_verify_otp_request_form_dict = supervisor_verify_otp_request.from_dict(supervisor_verify_otp_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


