# callchimp.ListsApi

All URIs are relative to *https://api.callchimp.ai/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_dev_lists150**](ListsApi.md#delete_dev_lists150) | **DELETE** /lists/{Id} | Delete List by Id
[**get_dev_lists137**](ListsApi.md#get_dev_lists137) | **GET** /lists/{Id} | Get List by Id
[**lists_list**](ListsApi.md#lists_list) | **GET** /lists | List Lists
[**patch_dev_lists151**](ListsApi.md#patch_dev_lists151) | **PATCH** /lists/{Id} | Update List by Id
[**post_dev_lists**](ListsApi.md#post_dev_lists) | **POST** /lists | Create a List


# **delete_dev_lists150**
> delete_dev_lists150(id)

Delete List by Id



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
    api_instance = callchimp.ListsApi(api_client)
    id = 56 # int | Numeric List Id

    try:
        # Delete List by Id
        api_instance.delete_dev_lists150(id)
    except Exception as e:
        print("Exception when calling ListsApi->delete_dev_lists150: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Numeric List Id | 

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
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dev_lists137**
> ListsResponse get_dev_lists137(id)

Get List by Id



### Example

* Api Key Authentication (x-api-key):

```python
import time
import os
import callchimp
from callchimp.models.lists_response import ListsResponse
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
    api_instance = callchimp.ListsApi(api_client)
    id = 56 # int | Numeric List Id

    try:
        # Get List by Id
        api_response = api_instance.get_dev_lists137(id)
        print("The response of ListsApi->get_dev_lists137:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ListsApi->get_dev_lists137: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Numeric List Id | 

### Return type

[**ListsResponse**](ListsResponse.md)

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

# **lists_list**
> ListsListResponse lists_list(page=page)

List Lists



### Example

* Api Key Authentication (x-api-key):

```python
import time
import os
import callchimp
from callchimp.models.lists_list_response import ListsListResponse
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
    api_instance = callchimp.ListsApi(api_client)
    page = 56 # int | Page Number (optional)

    try:
        # List Lists
        api_response = api_instance.lists_list(page=page)
        print("The response of ListsApi->lists_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ListsApi->lists_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page Number | [optional] 

### Return type

[**ListsListResponse**](ListsListResponse.md)

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

# **patch_dev_lists151**
> ListsResponse patch_dev_lists151(id, lists_request)

Update List by Id



### Example

* Api Key Authentication (x-api-key):

```python
import time
import os
import callchimp
from callchimp.models.lists_request import ListsRequest
from callchimp.models.lists_response import ListsResponse
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
    api_instance = callchimp.ListsApi(api_client)
    id = 56 # int | Numeric List Id
    lists_request = {"name":"Sample List"} # ListsRequest | 

    try:
        # Update List by Id
        api_response = api_instance.patch_dev_lists151(id, lists_request)
        print("The response of ListsApi->patch_dev_lists151:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ListsApi->patch_dev_lists151: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Numeric List Id | 
 **lists_request** | [**ListsRequest**](ListsRequest.md)|  | 

### Return type

[**ListsResponse**](ListsResponse.md)

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

# **post_dev_lists**
> ListsResponse post_dev_lists(lists_request)

Create a List



### Example

* Api Key Authentication (x-api-key):

```python
import time
import os
import callchimp
from callchimp.models.lists_request import ListsRequest
from callchimp.models.lists_response import ListsResponse
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
    api_instance = callchimp.ListsApi(api_client)
    lists_request = {"campaign":555,"description":"whenever","name":"Whatever"} # ListsRequest | 

    try:
        # Create a List
        api_response = api_instance.post_dev_lists(lists_request)
        print("The response of ListsApi->post_dev_lists:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ListsApi->post_dev_lists: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lists_request** | [**ListsRequest**](ListsRequest.md)|  | 

### Return type

[**ListsResponse**](ListsResponse.md)

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

