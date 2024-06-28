# callchimp.SubscribersApi

All URIs are relative to *https://api.callchimp.ai/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**subscribers_delete**](SubscribersApi.md#subscribers_delete) | **DELETE** /subscribers/{Id} | Delete Subscriber by Id
[**subscribers_get**](SubscribersApi.md#subscribers_get) | **GET** /subscribers/{Id} | Get Subscriber by Id
[**subscribers_list**](SubscribersApi.md#subscribers_list) | **GET** /subscribers | List Subscribers
[**subscribers_post**](SubscribersApi.md#subscribers_post) | **POST** /subscribers | Create one or more Subscriber(s)
[**subscribers_update**](SubscribersApi.md#subscribers_update) | **PATCH** /subscribers/{Id} | Update Subscriber by Id
[**subscribers_vendor_delete**](SubscribersApi.md#subscribers_vendor_delete) | **DELETE** /subscribers/vendor/{vendor_lead_code} | Delete Subscriber by Vendor Lead Code
[**subscribers_vendor_get**](SubscribersApi.md#subscribers_vendor_get) | **GET** /subscribers/vendor/{vendor_lead_code} | Get Subscriber by Vendor Lead Code
[**subscribers_vendor_update**](SubscribersApi.md#subscribers_vendor_update) | **PATCH** /subscribers/vendor/{vendor_lead_code} | Update Subscriber by Vendor Lead Code


# **subscribers_delete**
> subscribers_delete(id)

Delete Subscriber by Id



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
    api_instance = callchimp.SubscribersApi(api_client)
    id = 56 # int | Numeric Subscriber Id

    try:
        # Delete Subscriber by Id
        api_instance.subscribers_delete(id)
    except Exception as e:
        print("Exception when calling SubscribersApi->subscribers_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Numeric Subscriber Id | 

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
**204** |  |  -  |
**401** |  |  -  |
**404** |  |  -  |
**405** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subscribers_get**
> SubscriberResponse subscribers_get(id)

Get Subscriber by Id



### Example

* Api Key Authentication (x-api-key):

```python
import callchimp
from callchimp.models.subscriber_response import SubscriberResponse
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
    api_instance = callchimp.SubscribersApi(api_client)
    id = 56 # int | Numeric Subscriber Id

    try:
        # Get Subscriber by Id
        api_response = api_instance.subscribers_get(id)
        print("The response of SubscribersApi->subscribers_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscribersApi->subscribers_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Numeric Subscriber Id | 

### Return type

[**SubscriberResponse**](SubscriberResponse.md)

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

# **subscribers_list**
> SubscriberListResponse subscribers_list(page=page)

List Subscribers



### Example

* Api Key Authentication (x-api-key):

```python
import callchimp
from callchimp.models.subscriber_list_response import SubscriberListResponse
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
    api_instance = callchimp.SubscribersApi(api_client)
    page = 56 # int | page (optional)

    try:
        # List Subscribers
        api_response = api_instance.subscribers_list(page=page)
        print("The response of SubscribersApi->subscribers_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscribersApi->subscribers_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| page | [optional] 

### Return type

[**SubscriberListResponse**](SubscriberListResponse.md)

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

# **subscribers_post**
> SubscribersPost200Response subscribers_post(subscribers_post_request, call=call)

Create one or more Subscriber(s)



### Example

* Api Key Authentication (x-api-key):

```python
import callchimp
from callchimp.models.subscribers_post200_response import SubscribersPost200Response
from callchimp.models.subscribers_post_request import SubscribersPostRequest
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
    api_instance = callchimp.SubscribersApi(api_client)
    subscribers_post_request = {"first_name":"John","last_name":"Doe","leadlist":142,"phone_code":"91","phone_number":"90XXXXXXXX"} # SubscribersPostRequest | 
    call = True # bool | Set to true if you want to place call after inserting the subscriber (optional)

    try:
        # Create one or more Subscriber(s)
        api_response = api_instance.subscribers_post(subscribers_post_request, call=call)
        print("The response of SubscribersApi->subscribers_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscribersApi->subscribers_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscribers_post_request** | [**SubscribersPostRequest**](SubscribersPostRequest.md)|  | 
 **call** | **bool**| Set to true if you want to place call after inserting the subscriber | [optional] 

### Return type

[**SubscribersPost200Response**](SubscribersPost200Response.md)

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

# **subscribers_update**
> SubscriberResponse subscribers_update(id, subscriber_update_request)

Update Subscriber by Id



### Example

* Api Key Authentication (x-api-key):

```python
import callchimp
from callchimp.models.subscriber_response import SubscriberResponse
from callchimp.models.subscriber_update_request import SubscriberUpdateRequest
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
    api_instance = callchimp.SubscribersApi(api_client)
    id = 56 # int | Numeric Subscriber Id
    subscriber_update_request = {"first_name":"John"} # SubscriberUpdateRequest | 

    try:
        # Update Subscriber by Id
        api_response = api_instance.subscribers_update(id, subscriber_update_request)
        print("The response of SubscribersApi->subscribers_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscribersApi->subscribers_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Numeric Subscriber Id | 
 **subscriber_update_request** | [**SubscriberUpdateRequest**](SubscriberUpdateRequest.md)|  | 

### Return type

[**SubscriberResponse**](SubscriberResponse.md)

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

# **subscribers_vendor_delete**
> subscribers_vendor_delete(vendor_lead_code)

Delete Subscriber by Vendor Lead Code



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
    api_instance = callchimp.SubscribersApi(api_client)
    vendor_lead_code = 'vendor_lead_code_example' # str | Lead id in customer database

    try:
        # Delete Subscriber by Vendor Lead Code
        api_instance.subscribers_vendor_delete(vendor_lead_code)
    except Exception as e:
        print("Exception when calling SubscribersApi->subscribers_vendor_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vendor_lead_code** | **str**| Lead id in customer database | 

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
**204** |  |  -  |
**401** |  |  -  |
**404** |  |  -  |
**405** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subscribers_vendor_get**
> List[SubscriberResponse] subscribers_vendor_get(vendor_lead_code)

Get Subscriber by Vendor Lead Code



### Example

* Api Key Authentication (x-api-key):

```python
import callchimp
from callchimp.models.subscriber_response import SubscriberResponse
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
    api_instance = callchimp.SubscribersApi(api_client)
    vendor_lead_code = 'vendor_lead_code_example' # str | Lead id in customer database

    try:
        # Get Subscriber by Vendor Lead Code
        api_response = api_instance.subscribers_vendor_get(vendor_lead_code)
        print("The response of SubscribersApi->subscribers_vendor_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscribersApi->subscribers_vendor_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vendor_lead_code** | **str**| Lead id in customer database | 

### Return type

[**List[SubscriberResponse]**](SubscriberResponse.md)

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

# **subscribers_vendor_update**
> List[SubscriberResponse] subscribers_vendor_update(vendor_lead_code, subscriber_update_request)

Update Subscriber by Vendor Lead Code



### Example

* Api Key Authentication (x-api-key):

```python
import callchimp
from callchimp.models.subscriber_response import SubscriberResponse
from callchimp.models.subscriber_update_request import SubscriberUpdateRequest
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
    api_instance = callchimp.SubscribersApi(api_client)
    vendor_lead_code = 'vendor_lead_code_example' # str | Lead id in customer database
    subscriber_update_request = {"first_name":"John"} # SubscriberUpdateRequest | 

    try:
        # Update Subscriber by Vendor Lead Code
        api_response = api_instance.subscribers_vendor_update(vendor_lead_code, subscriber_update_request)
        print("The response of SubscribersApi->subscribers_vendor_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscribersApi->subscribers_vendor_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vendor_lead_code** | **str**| Lead id in customer database | 
 **subscriber_update_request** | [**SubscriberUpdateRequest**](SubscriberUpdateRequest.md)|  | 

### Return type

[**List[SubscriberResponse]**](SubscriberResponse.md)

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

