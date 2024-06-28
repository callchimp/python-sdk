# VoiceResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**accents** | **List[str]** |  | [optional] 
**language** | **str** |  | [optional] 
**gender** | **str** |  | [optional] 

## Example

```python
from callchimp.models.voice_response import VoiceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of VoiceResponse from a JSON string
voice_response_instance = VoiceResponse.from_json(json)
# print the JSON string representation of the object
print(VoiceResponse.to_json())

# convert the object into a dict
voice_response_dict = voice_response_instance.to_dict()
# create an instance of VoiceResponse from a dict
voice_response_from_dict = VoiceResponse.from_dict(voice_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


