# callchimp.CallsApi

All URIs are relative to *https://api.callchimp.ai/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**calls_get**](CallsApi.md#calls_get) | **GET** /calls/{Id} | Get Call by Id
[**calls_list_inbound**](CallsApi.md#calls_list_inbound) | **GET** /calls/inbound | List Supervisor Inbound Calls
[**calls_list_outbound**](CallsApi.md#calls_list_outbound) | **GET** /calls | List Calls
[**calls_post**](CallsApi.md#calls_post) | **POST** /calls | Create a Call
[**calls_reports**](CallsApi.md#calls_reports) | **POST** /calls/reports | Generate Call Reports


# **calls_get**
> CallResponse calls_get(id)

Get Call by Id



### Example

* Api Key Authentication (x-api-key):

```python
import callchimp
from callchimp.models.call_response import CallResponse
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
    api_instance = callchimp.CallsApi(api_client)
    id = 56 # int | Numeric call id to get

    try:
        # Get Call by Id
        api_response = api_instance.calls_get(id)
        print("The response of CallsApi->calls_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CallsApi->calls_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Numeric call id to get | 

### Return type

[**CallResponse**](CallResponse.md)

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

# **calls_list_inbound**
> InboundCallListResponse calls_list_inbound(page=page)

List Supervisor Inbound Calls



### Example

* Api Key Authentication (x-api-key):

```python
import callchimp
from callchimp.models.inbound_call_list_response import InboundCallListResponse
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
    api_instance = callchimp.CallsApi(api_client)
    page = 56 # int | page (optional)

    try:
        # List Supervisor Inbound Calls
        api_response = api_instance.calls_list_inbound(page=page)
        print("The response of CallsApi->calls_list_inbound:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CallsApi->calls_list_inbound: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| page | [optional] 

### Return type

[**InboundCallListResponse**](InboundCallListResponse.md)

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

# **calls_list_outbound**
> CallListResponse calls_list_outbound(page=page)

List Calls



### Example

* Api Key Authentication (x-api-key):

```python
import callchimp
from callchimp.models.call_list_response import CallListResponse
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
    api_instance = callchimp.CallsApi(api_client)
    page = 56 # int | page (optional)

    try:
        # List Calls
        api_response = api_instance.calls_list_outbound(page=page)
        print("The response of CallsApi->calls_list_outbound:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CallsApi->calls_list_outbound: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| page | [optional] 

### Return type

[**CallListResponse**](CallListResponse.md)

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

# **calls_post**
> CallResponse calls_post(calls_post_request)

Create a Call



### Example

* Api Key Authentication (x-api-key):

```python
import callchimp
from callchimp.models.call_response import CallResponse
from callchimp.models.calls_post_request import CallsPostRequest
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
    api_instance = callchimp.CallsApi(api_client)
    calls_post_request = {"lead":11664} # CallsPostRequest | 

    try:
        # Create a Call
        api_response = api_instance.calls_post(calls_post_request)
        print("The response of CallsApi->calls_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CallsApi->calls_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **calls_post_request** | [**CallsPostRequest**](CallsPostRequest.md)|  | 

### Return type

[**CallResponse**](CallResponse.md)

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

# **calls_reports**
> CallReportResponse calls_reports(call_report_request, retries=retries)

Generate Call Reports



### Example

* Api Key Authentication (x-api-key):

```python
import callchimp
from callchimp.models.call_report_request import CallReportRequest
from callchimp.models.call_report_response import CallReportResponse
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
    api_instance = callchimp.CallsApi(api_client)
    call_report_request = {"from":1701086080554,"to":1703678080554,"campaign":499} # CallReportRequest | 
    retries = 56 # int | retries (optional)

    try:
        # Generate Call Reports
        api_response = api_instance.calls_reports(call_report_request, retries=retries)
        print("The response of CallsApi->calls_reports:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CallsApi->calls_reports: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **call_report_request** | [**CallReportRequest**](CallReportRequest.md)|  | 
 **retries** | **int**| retries | [optional] 

### Return type

[**CallReportResponse**](CallReportResponse.md)

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

