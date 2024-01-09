# PostDevCallsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lead** | **int** |  | 
**vendor_lead_code** | **str** |  | 

## Example

```python
from callchimp.models.post_dev_calls_request import PostDevCallsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostDevCallsRequest from a JSON string
post_dev_calls_request_instance = PostDevCallsRequest.from_json(json)
# print the JSON string representation of the object
print PostDevCallsRequest.to_json()

# convert the object into a dict
post_dev_calls_request_dict = post_dev_calls_request_instance.to_dict()
# create an instance of PostDevCallsRequest from a dict
post_dev_calls_request_form_dict = post_dev_calls_request.from_dict(post_dev_calls_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


