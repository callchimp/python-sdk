# ScriptRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the script | [optional] 
**script** | **str** | Script the bot should follow during the conversation | [optional] 

## Example

```python
from callchimp.models.script_request import ScriptRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ScriptRequest from a JSON string
script_request_instance = ScriptRequest.from_json(json)
# print the JSON string representation of the object
print(ScriptRequest.to_json())

# convert the object into a dict
script_request_dict = script_request_instance.to_dict()
# create an instance of ScriptRequest from a dict
script_request_from_dict = ScriptRequest.from_dict(script_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


