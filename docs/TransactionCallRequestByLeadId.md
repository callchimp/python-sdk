# TransactionCallRequestByLeadId


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lead** | **int** | Lead Id | 
**transaction_audio_gender** | **str** | Gender of the generated voice | [optional] 
**transaction_vars** | **object** | Transaction variable values that should match the variables in campaign &#x60;transaction_template&#x60; | 

## Example

```python
from callchimp.models.transaction_call_request_by_lead_id import TransactionCallRequestByLeadId

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionCallRequestByLeadId from a JSON string
transaction_call_request_by_lead_id_instance = TransactionCallRequestByLeadId.from_json(json)
# print the JSON string representation of the object
print(TransactionCallRequestByLeadId.to_json())

# convert the object into a dict
transaction_call_request_by_lead_id_dict = transaction_call_request_by_lead_id_instance.to_dict()
# create an instance of TransactionCallRequestByLeadId from a dict
transaction_call_request_by_lead_id_from_dict = TransactionCallRequestByLeadId.from_dict(transaction_call_request_by_lead_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


