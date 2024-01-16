# Model4XXResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**errors** | [**List[Model4XXResponseErrorsInner]**](Model4XXResponseErrorsInner.md) |  | [optional] 

## Example

```python
from callchimp.models.model4_xx_response import Model4XXResponse

# TODO update the JSON string below
json = "{}"
# create an instance of Model4XXResponse from a JSON string
model4_xx_response_instance = Model4XXResponse.from_json(json)
# print the JSON string representation of the object
print Model4XXResponse.to_json()

# convert the object into a dict
model4_xx_response_dict = model4_xx_response_instance.to_dict()
# create an instance of Model4XXResponse from a dict
model4_xx_response_form_dict = model4_xx_response.from_dict(model4_xx_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


