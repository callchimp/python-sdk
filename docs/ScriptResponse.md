# ScriptResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**added_at** | **datetime** | The timestamp when the item was added. | [optional] 
**campaigns** | **List[int]** | A list of campaign identifiers associated with the script. | [optional] 
**explanation** | **str** | An explanation of the script content and its appropriateness. | [optional] 
**final_rating** | **str** | The final rating assigned to the script content. | [optional] 
**harm_category_dangerous_content_score** | **int** | Score for dangerous content category. | [optional] 
**harm_category_harassment_score** | **int** | Score for harassment content category. | [optional] 
**harm_category_hate_speech_score** | **int** | Score for hate speech content category. | [optional] 
**harm_category_sexually_explicit_score** | **int** | Score for sexually explicit content category. | [optional] 
**id** | **int** | The unique identifier for the script. | [optional] 
**name** | **str** | The name of the script. | [optional] 
**organization** | **int** | The identifier for the organization associated with the script. | [optional] 
**script** | **str** | The full script text. | [optional] 

## Example

```python
from callchimp.models.script_response import ScriptResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ScriptResponse from a JSON string
script_response_instance = ScriptResponse.from_json(json)
# print the JSON string representation of the object
print(ScriptResponse.to_json())

# convert the object into a dict
script_response_dict = script_response_instance.to_dict()
# create an instance of ScriptResponse from a dict
script_response_from_dict = ScriptResponse.from_dict(script_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


