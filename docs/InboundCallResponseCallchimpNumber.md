# InboundCallResponseCallchimpNumber


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**number** | **str** | Outbound caller id in E.164 format, e.g. &#x60;[+][country_code][number]&#x60;. | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from callchimp.models.inbound_call_response_callchimp_number import InboundCallResponseCallchimpNumber

# TODO update the JSON string below
json = "{}"
# create an instance of InboundCallResponseCallchimpNumber from a JSON string
inbound_call_response_callchimp_number_instance = InboundCallResponseCallchimpNumber.from_json(json)
# print the JSON string representation of the object
print(InboundCallResponseCallchimpNumber.to_json())

# convert the object into a dict
inbound_call_response_callchimp_number_dict = inbound_call_response_callchimp_number_instance.to_dict()
# create an instance of InboundCallResponseCallchimpNumber from a dict
inbound_call_response_callchimp_number_from_dict = InboundCallResponseCallchimpNumber.from_dict(inbound_call_response_callchimp_number_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


