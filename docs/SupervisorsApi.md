# callchimp.SupervisorsApi

All URIs are relative to *https://api.callchimp.ai/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**supervisors_delete**](SupervisorsApi.md#supervisors_delete) | **DELETE** /supervisors/{Id} | Delete Supervisor by Id
[**supervisors_get**](SupervisorsApi.md#supervisors_get) | **GET** /supervisors/{Id} | Get Supervisor by Id
[**supervisors_list**](SupervisorsApi.md#supervisors_list) | **GET** /supervisors | List Supervisors
[**supervisors_post**](SupervisorsApi.md#supervisors_post) | **POST** /supervisors | Create a Supervisor
[**supervisors_sendotp**](SupervisorsApi.md#supervisors_sendotp) | **POST** /supervisors/{Id}/send_otp | Send OTP to Supervisor by Id
[**supervisors_update**](SupervisorsApi.md#supervisors_update) | **PATCH** /supervisors/{Id} | Update Supervisor by Id
[**supervisors_verifyotp**](SupervisorsApi.md#supervisors_verifyotp) | **POST** /supervisors/{Id}/verify_otp | Verify Supervisor OTP by Id


# **supervisors_delete**
> supervisors_delete(id)

Delete Supervisor by Id



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
    api_instance = callchimp.SupervisorsApi(api_client)
    id = 56 # int | Numeric Supervisor Id

    try:
        # Delete Supervisor by Id
        api_instance.supervisors_delete(id)
    except Exception as e:
        print("Exception when calling SupervisorsApi->supervisors_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Numeric Supervisor Id | 

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

# **supervisors_get**
> SupervisorResponse supervisors_get(id)

Get Supervisor by Id



### Example

* Api Key Authentication (x-api-key):

```python
import callchimp
from callchimp.models.supervisor_response import SupervisorResponse
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
    api_instance = callchimp.SupervisorsApi(api_client)
    id = 56 # int | Numeric Supervisor Id

    try:
        # Get Supervisor by Id
        api_response = api_instance.supervisors_get(id)
        print("The response of SupervisorsApi->supervisors_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SupervisorsApi->supervisors_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Numeric Supervisor Id | 

### Return type

[**SupervisorResponse**](SupervisorResponse.md)

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

# **supervisors_list**
> SupervisorListResponse supervisors_list(page=page)

List Supervisors



### Example

* Api Key Authentication (x-api-key):

```python
import callchimp
from callchimp.models.supervisor_list_response import SupervisorListResponse
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
    api_instance = callchimp.SupervisorsApi(api_client)
    page = 56 # int | Page Number (optional)

    try:
        # List Supervisors
        api_response = api_instance.supervisors_list(page=page)
        print("The response of SupervisorsApi->supervisors_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SupervisorsApi->supervisors_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page Number | [optional] 

### Return type

[**SupervisorListResponse**](SupervisorListResponse.md)

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

# **supervisors_post**
> SupervisorResponse supervisors_post(supervisor_request)

Create a Supervisor



### Example

* Api Key Authentication (x-api-key):

```python
import callchimp
from callchimp.models.supervisor_request import SupervisorRequest
from callchimp.models.supervisor_response import SupervisorResponse
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
    api_instance = callchimp.SupervisorsApi(api_client)
    supervisor_request = {"name":"John Doe","phone":"+9190XXXXXXXX","priority":1,"organization":999} # SupervisorRequest | 

    try:
        # Create a Supervisor
        api_response = api_instance.supervisors_post(supervisor_request)
        print("The response of SupervisorsApi->supervisors_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SupervisorsApi->supervisors_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **supervisor_request** | [**SupervisorRequest**](SupervisorRequest.md)|  | 

### Return type

[**SupervisorResponse**](SupervisorResponse.md)

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

# **supervisors_sendotp**
> SupervisorSendOtpResponse supervisors_sendotp(id)

Send OTP to Supervisor by Id



### Example

* Api Key Authentication (x-api-key):

```python
import callchimp
from callchimp.models.supervisor_send_otp_response import SupervisorSendOtpResponse
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
    api_instance = callchimp.SupervisorsApi(api_client)
    id = 56 # int | Numeric Supervisor Id

    try:
        # Send OTP to Supervisor by Id
        api_response = api_instance.supervisors_sendotp(id)
        print("The response of SupervisorsApi->supervisors_sendotp:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SupervisorsApi->supervisors_sendotp: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Numeric Supervisor Id | 

### Return type

[**SupervisorSendOtpResponse**](SupervisorSendOtpResponse.md)

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

# **supervisors_update**
> SupervisorResponse supervisors_update(id, supervisor_request)

Update Supervisor by Id



### Example

* Api Key Authentication (x-api-key):

```python
import callchimp
from callchimp.models.supervisor_request import SupervisorRequest
from callchimp.models.supervisor_response import SupervisorResponse
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
    api_instance = callchimp.SupervisorsApi(api_client)
    id = 56 # int | Numeric Supervisor Id
    supervisor_request = {"name":"Sudip R."} # SupervisorRequest | 

    try:
        # Update Supervisor by Id
        api_response = api_instance.supervisors_update(id, supervisor_request)
        print("The response of SupervisorsApi->supervisors_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SupervisorsApi->supervisors_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Numeric Supervisor Id | 
 **supervisor_request** | [**SupervisorRequest**](SupervisorRequest.md)|  | 

### Return type

[**SupervisorResponse**](SupervisorResponse.md)

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

# **supervisors_verifyotp**
> SupervisorVerifyOtpResponse supervisors_verifyotp(id, supervisor_verify_otp_request)

Verify Supervisor OTP by Id



### Example

* Api Key Authentication (x-api-key):

```python
import callchimp
from callchimp.models.supervisor_verify_otp_request import SupervisorVerifyOtpRequest
from callchimp.models.supervisor_verify_otp_response import SupervisorVerifyOtpResponse
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
    api_instance = callchimp.SupervisorsApi(api_client)
    id = 56 # int | Numeric Supervisor Id
    supervisor_verify_otp_request = {"otp":"351350"} # SupervisorVerifyOtpRequest | 

    try:
        # Verify Supervisor OTP by Id
        api_response = api_instance.supervisors_verifyotp(id, supervisor_verify_otp_request)
        print("The response of SupervisorsApi->supervisors_verifyotp:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SupervisorsApi->supervisors_verifyotp: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Numeric Supervisor Id | 
 **supervisor_verify_otp_request** | [**SupervisorVerifyOtpRequest**](SupervisorVerifyOtpRequest.md)|  | 

### Return type

[**SupervisorVerifyOtpResponse**](SupervisorVerifyOtpResponse.md)

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

