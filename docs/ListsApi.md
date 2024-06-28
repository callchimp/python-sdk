# callchimp.ListsApi

All URIs are relative to *https://api.callchimp.ai/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**lists_create_campaign_and_list**](ListsApi.md#lists_create_campaign_and_list) | **POST** /lists/create_campaign_and_list | Create Campaign with Default List
[**lists_delete**](ListsApi.md#lists_delete) | **DELETE** /lists/{Id} | Delete List by Id
[**lists_find**](ListsApi.md#lists_find) | **POST** /lists/find | Search List by Name or Id
[**lists_get**](ListsApi.md#lists_get) | **GET** /lists/{Id} | Get List by Id
[**lists_list**](ListsApi.md#lists_list) | **GET** /lists | List Lists
[**lists_post**](ListsApi.md#lists_post) | **POST** /lists | Create a List
[**lists_update**](ListsApi.md#lists_update) | **PATCH** /lists/{Id} | Update List by Id


# **lists_create_campaign_and_list**
> ListsResponse lists_create_campaign_and_list(campaign_lists_request)

Create Campaign with Default List



### Example

* Api Key Authentication (x-api-key):

```python
import callchimp
from callchimp.models.campaign_lists_request import CampaignListsRequest
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
    campaign_lists_request = {"name":"Transactional Campaign by API","phone_number":2,"type":"transactional","transaction_template":"Dear {first_name}, your account {account_number} has been credited with ₹{amount}.","description":"whenever"} # CampaignListsRequest | 

    try:
        # Create Campaign with Default List
        api_response = api_instance.lists_create_campaign_and_list(campaign_lists_request)
        print("The response of ListsApi->lists_create_campaign_and_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ListsApi->lists_create_campaign_and_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_lists_request** | [**CampaignListsRequest**](CampaignListsRequest.md)|  | 

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
**401** |  |  -  |
**405** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **lists_delete**
> lists_delete(id)

Delete List by Id



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
    api_instance = callchimp.ListsApi(api_client)
    id = 56 # int | Numeric List Id

    try:
        # Delete List by Id
        api_instance.lists_delete(id)
    except Exception as e:
        print("Exception when calling ListsApi->lists_delete: %s\n" % e)
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
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**401** |  |  -  |
**404** |  |  -  |
**405** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **lists_find**
> ListsResponse lists_find(list_find_request, page=page)

Search List by Name or Id



### Example

* Api Key Authentication (x-api-key):

```python
import callchimp
from callchimp.models.list_find_request import ListFindRequest
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
    list_find_request = {"query":"Rickroll"} # ListFindRequest | 
    page = 56 # int | Page Number (optional)

    try:
        # Search List by Name or Id
        api_response = api_instance.lists_find(list_find_request, page=page)
        print("The response of ListsApi->lists_find:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ListsApi->lists_find: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_find_request** | [**ListFindRequest**](ListFindRequest.md)|  | 
 **page** | **int**| Page Number | [optional] 

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
**401** |  |  -  |
**405** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **lists_get**
> ListsResponse lists_get(id)

Get List by Id



### Example

* Api Key Authentication (x-api-key):

```python
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
        api_response = api_instance.lists_get(id)
        print("The response of ListsApi->lists_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ListsApi->lists_get: %s\n" % e)
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
**401** |  |  -  |
**404** |  |  -  |
**405** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **lists_list**
> ListsListResponse lists_list(page=page)

List Lists



### Example

* Api Key Authentication (x-api-key):

```python
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
**401** |  |  -  |
**405** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **lists_post**
> ListsResponse lists_post(lists_request)

Create a List



### Example

* Api Key Authentication (x-api-key):

```python
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
        api_response = api_instance.lists_post(lists_request)
        print("The response of ListsApi->lists_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ListsApi->lists_post: %s\n" % e)
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
**401** |  |  -  |
**405** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **lists_update**
> ListsResponse lists_update(id, lists_request)

Update List by Id



### Example

* Api Key Authentication (x-api-key):

```python
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
        api_response = api_instance.lists_update(id, lists_request)
        print("The response of ListsApi->lists_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ListsApi->lists_update: %s\n" % e)
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
**401** |  |  -  |
**404** |  |  -  |
**405** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

