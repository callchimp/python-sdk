# callchimp.ScriptsApi

All URIs are relative to *https://api.callchimp.ai/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**scripts_delete**](ScriptsApi.md#scripts_delete) | **DELETE** /scripts/{Id} | Delete Script by Id
[**scripts_get**](ScriptsApi.md#scripts_get) | **GET** /scripts/{Id} | Get Script by Id
[**scripts_list**](ScriptsApi.md#scripts_list) | **GET** /scripts | List Script
[**scripts_post**](ScriptsApi.md#scripts_post) | **POST** /scripts | Create a Script
[**scripts_update**](ScriptsApi.md#scripts_update) | **PATCH** /scripts/{Id} | Update Script by Id


# **scripts_delete**
> scripts_delete(id)

Delete Script by Id



### Example

* Api Key Authentication (x-api-key):

```python
import callchimp
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
    api_instance = callchimp.ScriptsApi(api_client)
    id = 56 # int | Numeric Script Id

    try:
        # Delete Script by Id
        api_instance.scripts_delete(id)
    except Exception as e:
        print("Exception when calling ScriptsApi->scripts_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Numeric Script Id | 

### Return type

void (empty response body)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**401** |  |  -  |
**404** |  |  -  |
**405** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scripts_get**
> ScriptResponse scripts_get(id)

Get Script by Id



### Example

* Api Key Authentication (x-api-key):

```python
import callchimp
from callchimp.models.script_response import ScriptResponse
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
    api_instance = callchimp.ScriptsApi(api_client)
    id = 56 # int | Numeric Script Id

    try:
        # Get Script by Id
        api_response = api_instance.scripts_get(id)
        print("The response of ScriptsApi->scripts_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScriptsApi->scripts_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Numeric Script Id | 

### Return type

[**ScriptResponse**](ScriptResponse.md)

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
**404** |  |  -  |
**405** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scripts_list**
> ScriptListResponse scripts_list(page=page)

List Script



### Example

* Api Key Authentication (x-api-key):

```python
import callchimp
from callchimp.models.script_list_response import ScriptListResponse
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
    api_instance = callchimp.ScriptsApi(api_client)
    page = 56 # int | Page Number (optional)

    try:
        # List Script
        api_response = api_instance.scripts_list(page=page)
        print("The response of ScriptsApi->scripts_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScriptsApi->scripts_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page Number | [optional] 

### Return type

[**ScriptListResponse**](ScriptListResponse.md)

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

# **scripts_post**
> ScriptResponse scripts_post(script_request)

Create a Script



### Example

* Api Key Authentication (x-api-key):

```python
import callchimp
from callchimp.models.script_request import ScriptRequest
from callchimp.models.script_response import ScriptResponse
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
    api_instance = callchimp.ScriptsApi(api_client)
    script_request = {"name":"Callchimp script","script":"Greet the user by saying, \"Hello, I am Chimpy, a bot at Callchimp. Would you like to hear a joke?\"\n\nIf the user responds positively, reply \"Why did the chimp call customer service? Because he couldn't find the ape on his phone! Goodbye!\"\n\nBut if the user responds negatively, reply \"Sorry, but you missed an amazing joke! Goodbye!\"\n"} # ScriptRequest | 

    try:
        # Create a Script
        api_response = api_instance.scripts_post(script_request)
        print("The response of ScriptsApi->scripts_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScriptsApi->scripts_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **script_request** | [**ScriptRequest**](ScriptRequest.md)|  | 

### Return type

[**ScriptResponse**](ScriptResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**401** |  |  -  |
**405** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scripts_update**
> WebhookResponse scripts_update(id, script_request)

Update Script by Id



### Example

* Api Key Authentication (x-api-key):

```python
import callchimp
from callchimp.models.script_request import ScriptRequest
from callchimp.models.webhook_response import WebhookResponse
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
    api_instance = callchimp.ScriptsApi(api_client)
    id = 56 # int | Numeric Script Id
    script_request = {"name":"Callchimp script updated"} # ScriptRequest | 

    try:
        # Update Script by Id
        api_response = api_instance.scripts_update(id, script_request)
        print("The response of ScriptsApi->scripts_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScriptsApi->scripts_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Numeric Script Id | 
 **script_request** | [**ScriptRequest**](ScriptRequest.md)|  | 

### Return type

[**WebhookResponse**](WebhookResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**401** |  |  -  |
**404** |  |  -  |
**405** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

