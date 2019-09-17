# swagger_client.ProjectApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_project**](ProjectApi.md#create_project) | **POST** /iaas/api/projects | Create project
[**delete_project**](ProjectApi.md#delete_project) | **DELETE** /iaas/api/projects/{id} | Delete project
[**get_project**](ProjectApi.md#get_project) | **GET** /iaas/api/projects/{id} | Get project
[**get_project_resource_metadata**](ProjectApi.md#get_project_resource_metadata) | **GET** /iaas/api/projects/{id}/resource-metadata | Get project resource metadata
[**get_projects**](ProjectApi.md#get_projects) | **GET** /iaas/api/projects | Get projects
[**update_project**](ProjectApi.md#update_project) | **PATCH** /iaas/api/projects/{id} | Update project
[**update_project_resource_metadata**](ProjectApi.md#update_project_resource_metadata) | **PATCH** /iaas/api/projects/{id}/resource-metadata | Update project resource metadata

# **create_project**
> Project create_project(body, api_version=api_version)

Create project

Create project

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectApi()
body = swagger_client.ProjectSpecification() # ProjectSpecification | Project Specification instance
api_version = 'api_version_example' # str | The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about (optional)

try:
    # Create project
    api_response = api_instance.create_project(body, api_version=api_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->create_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProjectSpecification**](ProjectSpecification.md)| Project Specification instance | 
 **api_version** | **str**| The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about | [optional] 

### Return type

[**Project**](Project.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, app/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_project**
> delete_project(id, api_version=api_version)

Delete project

Delete project with a given id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectApi()
id = 'id_example' # str | The ID of the project.
api_version = 'api_version_example' # str | The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about (optional)

try:
    # Delete project
    api_instance.delete_project(id, api_version=api_version)
except ApiException as e:
    print("Exception when calling ProjectApi->delete_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the project. | 
 **api_version** | **str**| The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project**
> Project get_project(id, api_version=api_version)

Get project

Get project with a given id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectApi()
id = 'id_example' # str | The ID of the project.
api_version = 'api_version_example' # str | The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about (optional)

try:
    # Get project
    api_response = api_instance.get_project(id, api_version=api_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->get_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the project. | 
 **api_version** | **str**| The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about | [optional] 

### Return type

[**Project**](Project.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, app/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_resource_metadata**
> ProjectResourceMetadata get_project_resource_metadata(id, api_version=api_version)

Get project resource metadata

Get project resource metadata by a given project id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectApi()
id = 'id_example' # str | The ID of the project.
api_version = 'api_version_example' # str | The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about (optional)

try:
    # Get project resource metadata
    api_response = api_instance.get_project_resource_metadata(id, api_version=api_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->get_project_resource_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the project. | 
 **api_version** | **str**| The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about | [optional] 

### Return type

[**ProjectResourceMetadata**](ProjectResourceMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, app/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_projects**
> ProjectResult get_projects(api_version=api_version)

Get projects

Get all projects

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectApi()
api_version = 'api_version_example' # str | The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about (optional)

try:
    # Get projects
    api_response = api_instance.get_projects(api_version=api_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->get_projects: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_version** | **str**| The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about | [optional] 

### Return type

[**ProjectResult**](ProjectResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, app/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_project**
> Project update_project(body, id, api_version=api_version)

Update project

Update project

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectApi()
body = swagger_client.ProjectSpecification() # ProjectSpecification | Project specification
id = 'id_example' # str | The ID of the project.
api_version = 'api_version_example' # str | The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about (optional)

try:
    # Update project
    api_response = api_instance.update_project(body, id, api_version=api_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->update_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProjectSpecification**](ProjectSpecification.md)| Project specification | 
 **id** | **str**| The ID of the project. | 
 **api_version** | **str**| The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about | [optional] 

### Return type

[**Project**](Project.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, app/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_project_resource_metadata**
> Project update_project_resource_metadata(body, id, api_version=api_version)

Update project resource metadata

Update project resource metadata by a given project id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectApi()
body = swagger_client.ProjectResourceMetadataSpecification() # ProjectResourceMetadataSpecification | Project specification
id = 'id_example' # str | The ID of the project.
api_version = 'api_version_example' # str | The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about (optional)

try:
    # Update project resource metadata
    api_response = api_instance.update_project_resource_metadata(body, id, api_version=api_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->update_project_resource_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProjectResourceMetadataSpecification**](ProjectResourceMetadataSpecification.md)| Project specification | 
 **id** | **str**| The ID of the project. | 
 **api_version** | **str**| The version of the API in yyyy-MM-dd format (UTC). For versioning information please refer to /iaas/api/about | [optional] 

### Return type

[**Project**](Project.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, app/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

