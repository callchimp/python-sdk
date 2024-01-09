# callchimp.SubscribersApi

All URIs are relative to *https://api.callchimp.ai/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**patch_dev_subscribers_by_id**](SubscribersApi.md#patch_dev_subscribers_by_id) | **PATCH** /subscribers/{Id} | Update Subscriber by Id
[**subscribers_delete**](SubscribersApi.md#subscribers_delete) | **DELETE** /subscribers/{Id} | Delete Subscriber by Id
[**subscribers_get**](SubscribersApi.md#subscribers_get) | **GET** /subscribers/{Id} | Get Subscriber by Id
[**subscribers_list**](SubscribersApi.md#subscribers_list) | **GET** /subscribers | List Subscribers
[**subscribers_post**](SubscribersApi.md#subscribers_post) | **POST** /subscribers | Create one or more Subscriber(s)


# **patch_dev_subscribers_by_id**
> SubscriberResponse patch_dev_subscribers_by_id(id, subscribers_update)

Update Subscriber by Id



### Example

* Api Key Authentication (x-api-key):

```python
import time
import os
import callchimp
from callchimp.models.subscriber_response import SubscriberResponse
from callchimp.models.subscribers_update import SubscribersUpdate
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
    subscribers_update = {"first_name":"John"} # SubscribersUpdate | 

    try:
        # Update Subscriber by Id
        api_response = api_instance.patch_dev_subscribers_by_id(id, subscribers_update)
        print("The response of SubscribersApi->patch_dev_subscribers_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscribersApi->patch_dev_subscribers_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Numeric Subscriber Id | 
 **subscribers_update** | [**SubscribersUpdate**](SubscribersUpdate.md)|  | 

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subscribers_delete**
> subscribers_delete(id)

Delete Subscriber by Id



### Example

* Api Key Authentication (x-api-key):

```python
import time
import os
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
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subscribers_get**
> SubscriberResponse subscribers_get(id)

Get Subscriber by Id



### Example

* Api Key Authentication (x-api-key):

```python
import time
import os
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subscribers_list**
> SubscriberListResponse subscribers_list(page=page)

List Subscribers



### Example

* Api Key Authentication (x-api-key):

```python
import time
import os
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
    page = 'page_example' # str | page (optional)

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
 **page** | **str**| page | [optional] 

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subscribers_post**
> SubscriberResponse subscribers_post(subscriber_request, call=call)

Create one or more Subscriber(s)



### Example

* Api Key Authentication (x-api-key):

```python
import time
import os
import callchimp
from callchimp.models.subscriber_request import SubscriberRequest
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
    subscriber_request = {"first_name":"John","last_name":"Doe","leadlist":142,"phone_code":"91","phone_number":"90XXXXXXXX"} # SubscriberRequest | 
    call = True # bool | Set to true if you want to place call after inserting the subscriber (optional)

    try:
        # Create one or more Subscriber(s)
        api_response = api_instance.subscribers_post(subscriber_request, call=call)
        print("The response of SubscribersApi->subscribers_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscribersApi->subscribers_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscriber_request** | [**SubscriberRequest**](SubscriberRequest.md)|  | 
 **call** | **bool**| Set to true if you want to place call after inserting the subscriber | [optional] 

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

