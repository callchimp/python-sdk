# callchimp.CampaignsApi

All URIs are relative to *https://api.callchimp.ai/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**campaigns_addsuper**](CampaignsApi.md#campaigns_addsuper) | **POST** /campaigns/{Id}/add_super | Add Supervisors to Campaign by Id
[**campaigns_delete**](CampaignsApi.md#campaigns_delete) | **DELETE** /campaigns/{Id} | Delete Campaign by Id
[**campaigns_get**](CampaignsApi.md#campaigns_get) | **GET** /campaigns/{Id} | Get Campaign by Id
[**campaigns_list**](CampaignsApi.md#campaigns_list) | **GET** /campaigns | List Campaigns
[**campaigns_post**](CampaignsApi.md#campaigns_post) | **POST** /campaigns | Create a Campaign
[**campaigns_removesuper**](CampaignsApi.md#campaigns_removesuper) | **POST** /campaigns/{Id}/remove_super | Remove Supervisors from Campaign by Id
[**campaigns_update**](CampaignsApi.md#campaigns_update) | **PATCH** /campaigns/{Id} | Update Campaign by Id
[**campaigns_uploadblast**](CampaignsApi.md#campaigns_uploadblast) | **PATCH** /campaigns/{Id}/upload_blast_file | Upload audio file to Campaign by Id


# **campaigns_addsuper**
> CampaignAddSuperResponse campaigns_addsuper(id, campaign_add_super_request)

Add Supervisors to Campaign by Id



### Example

* Api Key Authentication (x-api-key):

```python
import time
import os
import callchimp
from callchimp.models.campaign_add_super_request import CampaignAddSuperRequest
from callchimp.models.campaign_add_super_response import CampaignAddSuperResponse
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
    api_instance = callchimp.CampaignsApi(api_client)
    id = 56 # int | Numeric Campaign id
    campaign_add_super_request = {"supervisors":[34,35,36]} # CampaignAddSuperRequest | 

    try:
        # Add Supervisors to Campaign by Id
        api_response = api_instance.campaigns_addsuper(id, campaign_add_super_request)
        print("The response of CampaignsApi->campaigns_addsuper:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CampaignsApi->campaigns_addsuper: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Numeric Campaign id | 
 **campaign_add_super_request** | [**CampaignAddSuperRequest**](CampaignAddSuperRequest.md)|  | 

### Return type

[**CampaignAddSuperResponse**](CampaignAddSuperResponse.md)

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

# **campaigns_delete**
> campaigns_delete(id)

Delete Campaign by Id



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
    api_instance = callchimp.CampaignsApi(api_client)
    id = 56 # int | Numeric id to get

    try:
        # Delete Campaign by Id
        api_instance.campaigns_delete(id)
    except Exception as e:
        print("Exception when calling CampaignsApi->campaigns_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Numeric id to get | 

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

# **campaigns_get**
> CampaignResponse campaigns_get(id)

Get Campaign by Id



### Example

* Api Key Authentication (x-api-key):

```python
import time
import os
import callchimp
from callchimp.models.campaign_response import CampaignResponse
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
    api_instance = callchimp.CampaignsApi(api_client)
    id = 56 # int | Numeric id to get

    try:
        # Get Campaign by Id
        api_response = api_instance.campaigns_get(id)
        print("The response of CampaignsApi->campaigns_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CampaignsApi->campaigns_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Numeric id to get | 

### Return type

[**CampaignResponse**](CampaignResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**404** |  |  -  |
**405** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **campaigns_list**
> CampaignListResponse campaigns_list(page=page)

List Campaigns



### Example

* Api Key Authentication (x-api-key):

```python
import time
import os
import callchimp
from callchimp.models.campaign_list_response import CampaignListResponse
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
    api_instance = callchimp.CampaignsApi(api_client)
    page = 56 # int | Page Number (optional)

    try:
        # List Campaigns
        api_response = api_instance.campaigns_list(page=page)
        print("The response of CampaignsApi->campaigns_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CampaignsApi->campaigns_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page Number | [optional] 

### Return type

[**CampaignListResponse**](CampaignListResponse.md)

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

# **campaigns_post**
> CampaignResponse campaigns_post(campaign_request)

Create a Campaign



### Example

* Api Key Authentication (x-api-key):

```python
import time
import os
import callchimp
from callchimp.models.campaign_request import CampaignRequest
from callchimp.models.campaign_response import CampaignResponse
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
    api_instance = callchimp.CampaignsApi(api_client)
    campaign_request = {"max_retry":2,"name":"Blastout Campaign by API","phone_number":4,"type":"blastout"} # CampaignRequest | 

    try:
        # Create a Campaign
        api_response = api_instance.campaigns_post(campaign_request)
        print("The response of CampaignsApi->campaigns_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CampaignsApi->campaigns_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_request** | [**CampaignRequest**](CampaignRequest.md)|  | 

### Return type

[**CampaignResponse**](CampaignResponse.md)

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
**415** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **campaigns_removesuper**
> CampaignRemoveSuperResponse campaigns_removesuper(id, campaign_remove_super_request)

Remove Supervisors from Campaign by Id



### Example

* Api Key Authentication (x-api-key):

```python
import time
import os
import callchimp
from callchimp.models.campaign_remove_super_request import CampaignRemoveSuperRequest
from callchimp.models.campaign_remove_super_response import CampaignRemoveSuperResponse
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
    api_instance = callchimp.CampaignsApi(api_client)
    id = 56 # int | Numeric Campaign id
    campaign_remove_super_request = {"supervisors":[35,36]} # CampaignRemoveSuperRequest | 

    try:
        # Remove Supervisors from Campaign by Id
        api_response = api_instance.campaigns_removesuper(id, campaign_remove_super_request)
        print("The response of CampaignsApi->campaigns_removesuper:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CampaignsApi->campaigns_removesuper: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Numeric Campaign id | 
 **campaign_remove_super_request** | [**CampaignRemoveSuperRequest**](CampaignRemoveSuperRequest.md)|  | 

### Return type

[**CampaignRemoveSuperResponse**](CampaignRemoveSuperResponse.md)

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

# **campaigns_update**
> CampaignResponse campaigns_update(id, campaign_request)

Update Campaign by Id



### Example

* Api Key Authentication (x-api-key):

```python
import time
import os
import callchimp
from callchimp.models.campaign_request import CampaignRequest
from callchimp.models.campaign_response import CampaignResponse
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
    api_instance = callchimp.CampaignsApi(api_client)
    id = 56 # int | Numeric id to get
    campaign_request = {"max_retry":1,"name":"Campaign by API renamed!"} # CampaignRequest | 

    try:
        # Update Campaign by Id
        api_response = api_instance.campaigns_update(id, campaign_request)
        print("The response of CampaignsApi->campaigns_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CampaignsApi->campaigns_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Numeric id to get | 
 **campaign_request** | [**CampaignRequest**](CampaignRequest.md)|  | 

### Return type

[**CampaignResponse**](CampaignResponse.md)

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

# **campaigns_uploadblast**
> CampaignUploadAudioResponse campaigns_uploadblast(id, file)

Upload audio file to Campaign by Id



### Example

* Api Key Authentication (x-api-key):

```python
import time
import os
import callchimp
from callchimp.models.campaign_upload_audio_response import CampaignUploadAudioResponse
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
    api_instance = callchimp.CampaignsApi(api_client)
    id = 56 # int | Numeric Campaign id
    file = None # bytearray | 

    try:
        # Upload audio file to Campaign by Id
        api_response = api_instance.campaigns_uploadblast(id, file)
        print("The response of CampaignsApi->campaigns_uploadblast:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CampaignsApi->campaigns_uploadblast: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Numeric Campaign id | 
 **file** | **bytearray**|  | 

### Return type

[**CampaignUploadAudioResponse**](CampaignUploadAudioResponse.md)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**401** |  |  -  |
**404** |  |  -  |
**405** |  |  -  |
**415** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

