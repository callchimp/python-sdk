# callchimp.VoicesApi

All URIs are relative to *https://api.callchimp.ai/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**voices_list**](VoicesApi.md#voices_list) | **GET** /voices | List Available Voices


# **voices_list**
> List[VoiceResponse] voices_list()

List Available Voices

Lists available voices for an organization. For a preview of available voices, go to [Voice Garden](https://voices.callchimp.ai/) by Callchimp 

### Example

* Api Key Authentication (x-api-key):

```python
import callchimp
from callchimp.models.voice_response import VoiceResponse
from callchimp.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.callchimp.ai/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = callchimp.Configuration(
    host = "https://api.callchimp.ai/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: x-api-key
configuration.api_key['x-api-key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# Enter a context with an instance of the API client
with callchimp.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = callchimp.VoicesApi(api_client)

    try:
        # List Available Voices
        api_response = api_instance.voices_list()
        print("The response of VoicesApi->voices_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VoicesApi->voices_list: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[VoiceResponse]**](VoiceResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**401** |  |  -  |
**405** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

