# xenia_python_client_library.CoreApi

All URIs are relative to *https://api.dutchanalytics.net/v1.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**configurations_list**](CoreApi.md#configurations_list) | **GET** /config/connectors | List available connector configurations
[**connectors_create**](CoreApi.md#connectors_create) | **POST** /projects/{project_name}/connectors | Create a connector
[**connectors_delete**](CoreApi.md#connectors_delete) | **DELETE** /projects/{project_name}/connectors/{connector_name} | Delete connectors
[**connectors_get**](CoreApi.md#connectors_get) | **GET** /projects/{project_name}/connectors/{connector_name} | Get connectors
[**connectors_list**](CoreApi.md#connectors_list) | **GET** /projects/{project_name}/connectors | List connectors
[**connectors_update**](CoreApi.md#connectors_update) | **PATCH** /projects/{project_name}/connectors/{connector_name} | Update connectors
[**credentials_create**](CoreApi.md#credentials_create) | **POST** /projects/{project_name}/credentials | Create credentials
[**credentials_delete**](CoreApi.md#credentials_delete) | **DELETE** /projects/{project_name}/credentials/{credentials_name} | Delete credentials
[**credentials_get**](CoreApi.md#credentials_get) | **GET** /projects/{project_name}/credentials/{credentials_name} | Get credentials
[**credentials_list**](CoreApi.md#credentials_list) | **GET** /projects/{project_name}/credentials | List credentials
[**credentials_update**](CoreApi.md#credentials_update) | **PATCH** /projects/{project_name}/credentials/{credentials_name} | Update credentials
[**metrics_get**](CoreApi.md#metrics_get) | **GET** /projects/{project_name}/metrics/{metric} | Get metrics
[**model_blob_requests_get**](CoreApi.md#model_blob_requests_get) | **GET** /projects/{project_name}/models/{model_name}/versions/{version}/requests-blob/{request_id} | Get blob model request results
[**model_environment_variables_create**](CoreApi.md#model_environment_variables_create) | **POST** /projects/{project_name}/models/{model_name}/environment-variables | Create model environment variable
[**model_environment_variables_delete**](CoreApi.md#model_environment_variables_delete) | **DELETE** /projects/{project_name}/models/{model_name}/environment-variables/{id} | Delete model environment variable
[**model_environment_variables_get**](CoreApi.md#model_environment_variables_get) | **GET** /projects/{project_name}/models/{model_name}/environment-variables/{id} | Get model environment variable
[**model_environment_variables_list**](CoreApi.md#model_environment_variables_list) | **GET** /projects/{project_name}/models/{model_name}/environment-variables | List model environment variables
[**model_environment_variables_update**](CoreApi.md#model_environment_variables_update) | **PATCH** /projects/{project_name}/models/{model_name}/environment-variables/{id} | Update model environment variable
[**model_requests_create**](CoreApi.md#model_requests_create) | **POST** /projects/{project_name}/models/{model_name}/versions/{version}/request | Create model requests
[**model_requests_create_blob**](CoreApi.md#model_requests_create_blob) | **POST** /projects/{project_name}/models/{model_name}/versions/{version}/request-blob | Create blob model requests
[**model_requests_create_bulk**](CoreApi.md#model_requests_create_bulk) | **POST** /projects/{project_name}/models/{model_name}/versions/{version}/request-bulk | Create bulk model requests
[**model_requests_get**](CoreApi.md#model_requests_get) | **GET** /projects/{project_name}/models/{model_name}/versions/{version}/requests/{request_id} | Get model request results
[**model_requests_get_bulk**](CoreApi.md#model_requests_get_bulk) | **POST** /projects/{project_name}/models/{model_name}/versions/{version}/request-collect-bulk | Get model request results bulk
[**model_requests_get_pending**](CoreApi.md#model_requests_get_pending) | **GET** /projects/{project_name}/models/{model_name}/versions/{version}/pending-requests | Get pending model requests
[**model_version_environment_variables_create**](CoreApi.md#model_version_environment_variables_create) | **POST** /projects/{project_name}/models/{model_name}/versions/{version}/environment-variables | Create model version environment variable
[**model_version_environment_variables_delete**](CoreApi.md#model_version_environment_variables_delete) | **DELETE** /projects/{project_name}/models/{model_name}/versions/{version}/environment-variables/{id} | Delete model version environment variable
[**model_version_environment_variables_get**](CoreApi.md#model_version_environment_variables_get) | **GET** /projects/{project_name}/models/{model_name}/versions/{version}/environment-variables/{id} | Get model version environment variable
[**model_version_environment_variables_list**](CoreApi.md#model_version_environment_variables_list) | **GET** /projects/{project_name}/models/{model_name}/versions/{version}/environment-variables | List model version environment variables
[**model_version_environment_variables_update**](CoreApi.md#model_version_environment_variables_update) | **PATCH** /projects/{project_name}/models/{model_name}/versions/{version}/environment-variables/{id} | Update model version environment variable
[**model_versions_create**](CoreApi.md#model_versions_create) | **POST** /projects/{project_name}/models/{model_name}/versions | Create model versions
[**model_versions_delete**](CoreApi.md#model_versions_delete) | **DELETE** /projects/{project_name}/models/{model_name}/versions/{version} | Delete model version
[**model_versions_file_download**](CoreApi.md#model_versions_file_download) | **GET** /projects/{project_name}/models/{model_name}/versions/{version}/download-model-file | Download model files
[**model_versions_file_upload**](CoreApi.md#model_versions_file_upload) | **PUT** /projects/{project_name}/models/{model_name}/versions/{version}/upload-model-file | Upload model files
[**model_versions_get**](CoreApi.md#model_versions_get) | **GET** /projects/{project_name}/models/{model_name}/versions/{version} | Get model version
[**model_versions_list**](CoreApi.md#model_versions_list) | **GET** /projects/{project_name}/models/{model_name}/versions | List model versions
[**model_versions_update**](CoreApi.md#model_versions_update) | **PATCH** /projects/{project_name}/models/{model_name}/versions/{version} | Update model version
[**models_create**](CoreApi.md#models_create) | **POST** /projects/{project_name}/models | Create a model
[**models_delete**](CoreApi.md#models_delete) | **DELETE** /projects/{project_name}/models/{model_name} | Delete a model
[**models_get**](CoreApi.md#models_get) | **GET** /projects/{project_name}/models/{model_name} | Get details of model
[**models_list**](CoreApi.md#models_list) | **GET** /projects/{project_name}/models | List models in project
[**models_update**](CoreApi.md#models_update) | **PATCH** /projects/{project_name}/models/{model_name} | Update a model
[**organization_invites_delete**](CoreApi.md#organization_invites_delete) | **DELETE** /organizations/{organization_name}/invites/{invite_id} | Delete an organization invitation of a user
[**organization_invites_get**](CoreApi.md#organization_invites_get) | **GET** /organizations/{organization_name}/invites/{invite_id} | Get details of an organization invitation of a user
[**organization_invites_list**](CoreApi.md#organization_invites_list) | **GET** /organizations/{organization_name}/invites | List the users invited to an organization
[**organization_users_create**](CoreApi.md#organization_users_create) | **POST** /organizations/{organization_name}/users | Add a user to an organization
[**organization_users_delete**](CoreApi.md#organization_users_delete) | **DELETE** /organizations/{organization_name}/users/{user_id} | Delete a user from an organization
[**organization_users_get**](CoreApi.md#organization_users_get) | **GET** /organizations/{organization_name}/users/{user_id} | Get details of a user in an organization
[**organization_users_list**](CoreApi.md#organization_users_list) | **GET** /organizations/{organization_name}/users | List the users in an organization
[**organization_users_update**](CoreApi.md#organization_users_update) | **PATCH** /organizations/{organization_name}/users/{user_id} | Update details of a user in an organization
[**organizations_create**](CoreApi.md#organizations_create) | **POST** /organizations | Create organizations
[**organizations_get**](CoreApi.md#organizations_get) | **GET** /organizations/{organization_name} | Get details of an organization
[**organizations_list**](CoreApi.md#organizations_list) | **GET** /organizations | List organizations
[**organizations_update**](CoreApi.md#organizations_update) | **PATCH** /organizations/{organization_name} | Update details of an organization
[**permissions_list**](CoreApi.md#permissions_list) | **GET** /permissions | List the available permissions
[**pipeline_insert_retrieve**](CoreApi.md#pipeline_insert_retrieve) | **GET** /projects/{project_name}/pipelines/{pipeline_name}/insert/{trace_id} | Retrieve pipeline insert results
[**pipeline_insert_retrieve_pending**](CoreApi.md#pipeline_insert_retrieve_pending) | **GET** /projects/{project_name}/pipelines/{pipeline_name}/pending-requests | Retrieve pending pipeline requests
[**pipeline_object_attachments_create**](CoreApi.md#pipeline_object_attachments_create) | **POST** /projects/{project_name}/pipelines/{pipeline_name}/attachments | Create object attachments
[**pipeline_object_attachments_delete**](CoreApi.md#pipeline_object_attachments_delete) | **DELETE** /projects/{project_name}/pipelines/{pipeline_name}/objects/{source_name}/attachments/{destination_name} | Delete attachment of a source and destination object
[**pipeline_object_attachments_get**](CoreApi.md#pipeline_object_attachments_get) | **GET** /projects/{project_name}/pipelines/{pipeline_name}/objects/{source_name}/attachments/{destination_name} | Get an attachment of a source and destination object
[**pipeline_object_attachments_list**](CoreApi.md#pipeline_object_attachments_list) | **GET** /projects/{project_name}/pipelines/{pipeline_name}/attachments | List object attachments
[**pipeline_object_attachments_source_get**](CoreApi.md#pipeline_object_attachments_source_get) | **GET** /projects/{project_name}/pipelines/{pipeline_name}/objects/{source_name}/attachments/ | List the attachments of a source object
[**pipeline_object_environment_variables_list**](CoreApi.md#pipeline_object_environment_variables_list) | **GET** /projects/{project_name}/pipelines/{pipeline_name}/objects/{name}/environment-variables | List pipeline object environment variables
[**pipeline_objects_create**](CoreApi.md#pipeline_objects_create) | **POST** /projects/{project_name}/pipelines/{pipeline_name}/objects | Add an object to a pipeline
[**pipeline_objects_delete**](CoreApi.md#pipeline_objects_delete) | **DELETE** /projects/{project_name}/pipelines/{pipeline_name}/objects/{name} | Delete object from pipeline
[**pipeline_objects_get**](CoreApi.md#pipeline_objects_get) | **GET** /projects/{project_name}/pipelines/{pipeline_name}/objects/{name} | Get an object in a pipeline
[**pipeline_objects_list**](CoreApi.md#pipeline_objects_list) | **GET** /projects/{project_name}/pipelines/{pipeline_name}/objects | List objects in a pipeline
[**pipeline_objects_update**](CoreApi.md#pipeline_objects_update) | **PATCH** /projects/{project_name}/pipelines/{pipeline_name}/objects/{name} | Update an object in a pipeline
[**pipelines_create**](CoreApi.md#pipelines_create) | **POST** /projects/{project_name}/pipelines | Create pipelines
[**pipelines_delete**](CoreApi.md#pipelines_delete) | **DELETE** /projects/{project_name}/pipelines/{pipeline_name} | Delete pipeline
[**pipelines_get**](CoreApi.md#pipelines_get) | **GET** /projects/{project_name}/pipelines/{pipeline_name} | Get pipeline
[**pipelines_insert**](CoreApi.md#pipelines_insert) | **POST** /projects/{project_name}/pipelines/{pipeline_name}/insert | Insert data in pipelines
[**pipelines_insert_blob**](CoreApi.md#pipelines_insert_blob) | **POST** /projects/{project_name}/pipelines/{pipeline_name}/insert-blob | Insert blobs in pipelines
[**pipelines_insert_bulk**](CoreApi.md#pipelines_insert_bulk) | **POST** /projects/{project_name}/pipelines/{pipeline_name}/insert-bulk | Insert data in bulk to pipelines
[**pipelines_list**](CoreApi.md#pipelines_list) | **GET** /projects/{project_name}/pipelines | List pipelines
[**pipelines_update**](CoreApi.md#pipelines_update) | **PATCH** /projects/{project_name}/pipelines/{pipeline_name} | Update pipeline
[**project_environment_variables_create**](CoreApi.md#project_environment_variables_create) | **POST** /projects/{project_name}/environment-variables | Create project environment variable
[**project_environment_variables_delete**](CoreApi.md#project_environment_variables_delete) | **DELETE** /projects/{project_name}/environment-variables/{id} | Delete project environment variable
[**project_environment_variables_get**](CoreApi.md#project_environment_variables_get) | **GET** /projects/{project_name}/environment-variables/{id} | Get project environment variable
[**project_environment_variables_list**](CoreApi.md#project_environment_variables_list) | **GET** /projects/{project_name}/environment-variables | List project environment variables
[**project_environment_variables_update**](CoreApi.md#project_environment_variables_update) | **PATCH** /projects/{project_name}/environment-variables/{id} | Update project environment variable
[**projects_create**](CoreApi.md#projects_create) | **POST** /projects | Create projects
[**projects_delete**](CoreApi.md#projects_delete) | **DELETE** /projects/{project_name} | Delete a project
[**projects_get**](CoreApi.md#projects_get) | **GET** /projects/{project_name} | Get details of a project
[**projects_list**](CoreApi.md#projects_list) | **GET** /projects | List projects
[**projects_log_list**](CoreApi.md#projects_log_list) | **POST** /projects/{project_name}/logs | List logs for a project
[**projects_user_list**](CoreApi.md#projects_user_list) | **GET** /projects/{project_name}/users | List the users in the organization of a project
[**role_assignments_create**](CoreApi.md#role_assignments_create) | **POST** /projects/{project_name}/role-assignments | Assign a role to a user in a project
[**role_assignments_delete**](CoreApi.md#role_assignments_delete) | **DELETE** /projects/{project_name}/role-assignments/{id} | Delete a role from a user with the given role assignment id
[**role_assignments_get**](CoreApi.md#role_assignments_get) | **GET** /projects/{project_name}/role-assignments/{id} | Get details of a role assignment
[**role_assignments_per_user_list**](CoreApi.md#role_assignments_per_user_list) | **GET** /projects/{project_name}/users/{user_id}/role-assignments | List the roles assigned to a specific user in a project
[**roles_create**](CoreApi.md#roles_create) | **POST** /projects/{project_name}/roles | Create a custom role scoped in a project
[**roles_delete**](CoreApi.md#roles_delete) | **DELETE** /projects/{project_name}/roles/{role_name} | Delete a role from a project
[**roles_get**](CoreApi.md#roles_get) | **GET** /projects/{project_name}/roles/{role_name} | Get details of a role
[**roles_list**](CoreApi.md#roles_list) | **GET** /projects/{project_name}/roles | List the available roles in a project
[**roles_update**](CoreApi.md#roles_update) | **PATCH** /projects/{project_name}/roles/{role_name} | Update a role in a project
[**service_status**](CoreApi.md#service_status) | **GET** /status | Service status
[**service_users_create**](CoreApi.md#service_users_create) | **POST** /projects/{project_name}/service-users | Create a new service user
[**service_users_delete**](CoreApi.md#service_users_delete) | **DELETE** /projects/{project_name}/service-users/{service_user_id} | Delete service user
[**service_users_get**](CoreApi.md#service_users_get) | **GET** /projects/{project_name}/service-users/{service_user_id} | Retrieve details of a service user
[**service_users_list**](CoreApi.md#service_users_list) | **GET** /projects/{project_name}/service-users | List service users
[**service_users_token**](CoreApi.md#service_users_token) | **PUT** /projects/{project_name}/service-users/{service_user_id}/token | Reset the token of a service user
[**service_users_update**](CoreApi.md#service_users_update) | **PATCH** /projects/{project_name}/service-users/{service_user_id} | Update service user details
[**subscriptions_list**](CoreApi.md#subscriptions_list) | **GET** /subscriptions | List subscriptions
[**user_create**](CoreApi.md#user_create) | **POST** /user | Create a new user
[**user_delete**](CoreApi.md#user_delete) | **DELETE** /user | Delete user
[**user_get**](CoreApi.md#user_get) | **GET** /user | Get user details


# **configurations_list**
> list[ConfigurationList] configurations_list()

List available connector configurations


### Description
Get the details of available connectors. The configuration parameters for both the connectors and their corresponding credentials are returned with the required names and data types. These parameters must be provided when creating credentials and connectors.

If a new connector is supported, the necessary configuration parameters can be accessed with this method.

### Response Structure
Details of the available connectors and their credentials

- `connector`: The name of the connector
- `connector_type`: The type of the connector. It can be either structured or blob depending on what type of data is supported by the connector.
- `connector_configuration`: A dictionary with the following keys:
    - `parameter`: The name of the parameter necessary for the connector configuration
    - `name`: descriptive name of the parameter
    - `description`: a description of the parameter
    - `input_field`: the HTML input field type for the UI
    - `default`: the default value for the parameter
    - `protected`: a boolean field to indicate if the parameter should be kept as hidden.
    - `regex`: the regex that is used to validate the parameter
- `credentials_configuration`: A dictionary with the following keys:
    - `parameter`: The name of the parameter necessary for the credentials configuration
    - `name`: descriptive name of the parameter
    - `description`: a description of the parameter
    - `input_field`: the HTML input field type for the UI
    - `default`: the default value for the parameter
    - `protected`: a boolean field to indicate if the parameter should be kept as hidden.
    - `regex`: the regex that is used to validate the parameter


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import xenia_python_client_library
from xenia_python_client_library.rest import ApiException
from pprint import pprint
configuration = xenia_python_client_library.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.dutchanalytics.net/v1.1
configuration.host = "https://api.dutchanalytics.net/v1.1"
# Create an instance of the API class
api_instance = xenia_python_client_library.CoreApi(xenia_python_client_library.ApiClient(configuration))

try:
    # List available connector configurations
    api_response = api_instance.configurations_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CoreApi->configurations_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ConfigurationList]**](ConfigurationList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **connectors_create**
> ConnectorList connectors_create(project_name, data)

Create a connector


### Description
Create a connector by defining its necessary configuration parameters. Connectors use a reference to credentials which will be used in authentication.

The type of a connector can be either a blob or structured. This type is inferred from the given type field. For example, an s3 connector is of type blob while a postgresql connector is structured.

### Required Parameters
- `name`: Name of the credentials. It is unique within a project.
- `type`: Type of the connector. It should be one of the supported connectors such as s3, postgresql and gcs.
- `credentials`: The name of referenced credentials
- `configuration`: A dictionary which should contain the fields necessary for the given type

### Optional Parameters
- `input_fields`: A list of connector fields with name and data_type. For example, for postgresql type of connector, these fields correspond to the columns in a table. In case of blob connectors, the input_fields should be omitted or given as an empty list. For structured connectors, they must be provided.

#### Request Examples
A postgresql connector
```
{
  "name": "postgresql-connector",
  "type": "postgresql",
  "credentials": "postgresql-credentials",
  "configuration": {
    "database": "database-1",
    "schema": "public",
    "table": "table-1"
  },
  "input_fields": [
    {
      "name": "field-1",
      "data_type": "int"
    },
     {
      "name": "field-2",
      "data_type": "double"
    }
  ]
}
```

### Response Structure
Details of the created connector

- `id`:Unique identifier for the connector (UUID)
- `name`:Name of the connector
- `type`:Type of the connector
- `input_type`:Type of the connector according to type field. It can be either structured or blob.
- `project`:Project name in which the connector is created
- `credentials`:The name of referenced credentials
- `configuration`:The dictionary which contains the fields necessary for the given type with provided values. Values are not shown in response if the parameter has the protected field True.
- `input_fields`:A list of connector fields with name and data_type

#### Response Examples
```
{
  "id": "e0342249-853c-4879-bd08-5cd1af572d7e",
  "name": "postgresql-connector",
  "type": "postgresql",
  "input_type": "structured",
  "project": "project-1",
  "credentials": "postgresql-credentials",
  "configuration": {
    "database": "database-1",
    "schema": "public",
    "table": "table-1"
  },
  "input_fields": [
    {
      "name": "field-1",
      "data_type": "int"
    },
     {
      "name": "field-2",
      "data_type": "double"
    }
  ]
}
```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import xenia_python_client_library
from xenia_python_client_library.rest import ApiException
from pprint import pprint
configuration = xenia_python_client_library.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.dutchanalytics.net/v1.1
configuration.host = "https://api.dutchanalytics.net/v1.1"
# Create an instance of the API class
api_instance = xenia_python_client_library.CoreApi(xenia_python_client_library.ApiClient(configuration))
project_name = 'project_name_example' # str | 
data = xenia_python_client_library.ConnectorCreate() # ConnectorCreate | 

try:
    # Create a connector
    api_response = api_instance.connectors_create(project_name, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CoreApi->connectors_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **data** | [**ConnectorCreate**](ConnectorCreate.md)|  | 

### Return type

[**ConnectorList**](ConnectorList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **connectors_delete**
> connectors_delete(project_name, connector_name)

Delete connectors

Delete a connector in a project.

### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import xenia_python_client_library
from xenia_python_client_library.rest import ApiException
from pprint import pprint
configuration = xenia_python_client_library.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.dutchanalytics.net/v1.1
configuration.host = "https://api.dutchanalytics.net/v1.1"
# Create an instance of the API class
api_instance = xenia_python_client_library.CoreApi(xenia_python_client_library.ApiClient(configuration))
project_name = 'project_name_example' # str | 
connector_name = 'connector_name_example' # str | 

try:
    # Delete connectors
    api_instance.connectors_delete(project_name, connector_name)
except ApiException as e:
    print("Exception when calling CoreApi->connectors_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **connector_name** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **connectors_get**
> ConnectorList connectors_get(project_name, connector_name)

Get connectors


### Description
Get the details of a single connector

### Response Structure
Details of the connector
- `id`:  Unique identifier for the connector (UUID)
- `name`:  Name of the connector
- `type`:  Type of the connector
- `input_type`:  Type of the connector according to type field. It can be either structured or blob.
- `project`:  Project name in which the connector is
- `credentials`:  The name of referenced credentials
- `configuration`:  The dictionary which contains the fields necessary for the given type with provided values. Values are not shown in response if the parameter has the protected field True.
- `input_fields`:  A list of connector fields with name and data_type

#### Response Examples

```
{
  "id": "662c326c-a560-4322-8ed3-1229224257c43",
  "name": "s3-connector",
  "type": "s3",
  "input_type": "blob",
  "project": "project-1",
  "credentials": "s3-credentials",
  "configuration": {
    "bucket": "bucket-name",
    "path_prefix": "blob"
  }
}
```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import xenia_python_client_library
from xenia_python_client_library.rest import ApiException
from pprint import pprint
configuration = xenia_python_client_library.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.dutchanalytics.net/v1.1
configuration.host = "https://api.dutchanalytics.net/v1.1"
# Create an instance of the API class
api_instance = xenia_python_client_library.CoreApi(xenia_python_client_library.ApiClient(configuration))
project_name = 'project_name_example' # str | 
connector_name = 'connector_name_example' # str | 

try:
    # Get connectors
    api_response = api_instance.connectors_get(project_name, connector_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CoreApi->connectors_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **connector_name** | **str**|  | 

### Return type

[**ConnectorList**](ConnectorList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **connectors_list**
> list[ConnectorList] connectors_list(project_name)

List connectors


### Description
List the connectors in a project.

### Response Structure
A list of details of the connectors in the project
- `id`: Unique identifier for the connector (UUID)
- `name`: Name of the connector
- `type`: Type of the connector
- `input_type`: Type of the connector according to type field. It can be either structured or blob.
- `project`: Project name in which the connector is
- `credentials`: The name of referenced credentials
- `configuration`: The dictionary which contains the fields necessary for the given type with provided values. Values are not shown in response if the parameter has the protected field True.
- `input_fields`: A list of connector fields with name and data_type

#### Response Examples
```
[
  {
    "id": "662c326c-a560-4322-8ed3-1229224257c43",
    "name": "s3-connector",
    "type": "s3",
    "input_type": "blob",
    "project": "project-1",
    "credentials": "s3-credentials",
    "configuration": {
      "bucket": "bucket-name",
      "path_prefix": "blob"
    }
  },
  {
    "id": "e0342249-853c-4879-bd08-5cd1af572d7e",
    "name": "postgresql-connector",
    "type": "postgresql",
    "input_type": "structured",
    "project": "project-1",
    "credentials": "postgresql-credentials",
    "configuration": {
      "database": "database-1",
      "schema": "public",
      "table": "table-1"
    },
    "input_fields": [
      {
        "name": "field-1",
        "data_type": "int"
      },
      {
        "name": "field-2",
        "data_type": "double"
      }
    ]
  }
]
```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import xenia_python_client_library
from xenia_python_client_library.rest import ApiException
from pprint import pprint
configuration = xenia_python_client_library.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.dutchanalytics.net/v1.1
configuration.host = "https://api.dutchanalytics.net/v1.1"
# Create an instance of the API class
api_instance = xenia_python_client_library.CoreApi(xenia_python_client_library.ApiClient(configuration))
project_name = 'project_name_example' # str | 

try:
    # List connectors
    api_response = api_instance.connectors_list(project_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CoreApi->connectors_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 

### Return type

[**list[ConnectorList]**](ConnectorList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **connectors_update**
> ConnectorList connectors_update(project_name, connector_name, data)

Update connectors


### Description
When updating a connector, all necessary fields are validated again. It is not possible to update the type of a connector.

### Optional Parameters
- `name`: New name for the connector
- `credentials`: A new credentials name to be referenced
- `configuration`: A new dictionary with new values for credentials configuration. This dictionary may contain a subset of the necessary parameters for the credentials type. Only the given parameters is updated and the rest is kept at their old values.
- `input_fields`: The old fields are changed with the new ones. If one or more old fields wanted to be kept for the connector, they must be provided again. In case an error occurs while creating the new fields, the connector will still have the old fields.

#### Request Examples
```	
{
  "name": "new-connector-name"
}
```

```
{
  "configuration": {
    "bucket": "new-bucket-name",
    "path_prefix": "new-blob"
  }
}
```

```
{
  "credentials": "new-credentials-name"
}
```

```
{
  "input_fields": [
    {
      "name": "new-connector-field-1",
      "data_type": "double"
    },
    {
      "name": "new-connector-field-2",
      "data_type": "array_int"
    }
  ]
}
```

### Response Structure
Details of the updated connector
- `id`: Unique identifier for the connector (UUID)
- `name`: Name of the connector
- `type`: Type of the connector
- `input_type`: Type of the connector according to type field. It can be either structured or blob.
- `project`: Project name in which the connector is
- `credentials`: The name of referenced credentials
- `configuration`: The dictionary which contains the fields necessary for the given type with provided values. Values are not shown in response if the parameter has the protected field True.
- `input_fields`: A list of connector fields with name and data_type

#### Response Examples
```	
{
  "id": "662c326c-a560-4322-8ed3-1229224257c43",
  "name": "new-s3-connector",
  "type": "s3",
  "input_type": "blob",
  "project": "project-1",
  "credentials": "s3-credentials",
  "configuration": {
    "bucket": "new-bucket-name",
    "path_prefix": "blob"
  }
}
```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import xenia_python_client_library
from xenia_python_client_library.rest import ApiException
from pprint import pprint
configuration = xenia_python_client_library.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.dutchanalytics.net/v1.1
configuration.host = "https://api.dutchanalytics.net/v1.1"
# Create an instance of the API class
api_instance = xenia_python_client_library.CoreApi(xenia_python_client_library.ApiClient(configuration))
project_name = 'project_name_example' # str | 
connector_name = 'connector_name_example' # str | 
data = xenia_python_client_library.ConnectorUpdate() # ConnectorUpdate | 

try:
    # Update connectors
    api_response = api_instance.connectors_update(project_name, connector_name, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CoreApi->connectors_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **connector_name** | **str**|  | 
 **data** | [**ConnectorUpdate**](ConnectorUpdate.md)|  | 

### Return type

[**ConnectorList**](ConnectorList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **credentials_create**
> CredentialsList credentials_create(project_name, data)

Create credentials


### Description 
Create a new credentials by defining its necessary configuration parameters.

### Required Parameters 
- `name`: Name of the credentials. It is unique within a project.
 - `type`: Type of the credentials. It should be one of the supported connectors such as s3, postgresql and gcs.
 - `configuration`: A dictionary which should contain the fields necessary for the given type

#### Request Examples
```
{
  "name": "s3-credentials",
  "type": "s3",
  "configuration": {
    "access_key": "access_key",
    "secret_key": "secret_key",
    "region": "eu-central-1"
  }
}
```

### Response Structure 
Details of the created credentials
 - `id`: Unique identifier for the credentials (UUID)
 - `name`: Name of the credentials
 - `project`: Project name in which the credentials is created
 - `type`: Type of the credentials
 - `reference_count`: The number of connectors using this credentials. It is initialised as 0 when it is created.
 - `configuration`: The dictionary which contains the fields necessary for the given type with provided values. Values are not shown in response if the parameter has the protected field True.

#### Response Examples 
```
{
  "id": "da4da757-373c-4cab-948e-90ff4ab2e9c3",
  "name": "s3-credentials",
  "project": "project-1",
  "type": "s3",
  "reference_count": 0,
  "configuration": {
    "access_key": null,
    "secret_key": null,
    "region": "eu-central-1"
  }
}
```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import xenia_python_client_library
from xenia_python_client_library.rest import ApiException
from pprint import pprint
configuration = xenia_python_client_library.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.dutchanalytics.net/v1.1
configuration.host = "https://api.dutchanalytics.net/v1.1"
# Create an instance of the API class
api_instance = xenia_python_client_library.CoreApi(xenia_python_client_library.ApiClient(configuration))
project_name = 'project_name_example' # str | 
data = xenia_python_client_library.CredentialsCreate() # CredentialsCreate | 

try:
    # Create credentials
    api_response = api_instance.credentials_create(project_name, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CoreApi->credentials_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **data** | [**CredentialsCreate**](CredentialsCreate.md)|  | 

### Return type

[**CredentialsList**](CredentialsList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **credentials_delete**
> credentials_delete(project_name, credentials_name)

Delete credentials

 
### Description 
Delete a credentials. If there is a reference to the credentials from a connector, it is __not possible to delete__ the credentials. The reference should be removed first.


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import xenia_python_client_library
from xenia_python_client_library.rest import ApiException
from pprint import pprint
configuration = xenia_python_client_library.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.dutchanalytics.net/v1.1
configuration.host = "https://api.dutchanalytics.net/v1.1"
# Create an instance of the API class
api_instance = xenia_python_client_library.CoreApi(xenia_python_client_library.ApiClient(configuration))
project_name = 'project_name_example' # str | 
credentials_name = 'credentials_name_example' # str | 

try:
    # Delete credentials
    api_instance.credentials_delete(project_name, credentials_name)
except ApiException as e:
    print("Exception when calling CoreApi->credentials_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **credentials_name** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **credentials_get**
> CredentialsListWithConfig credentials_get(project_name, credentials_name)

Get credentials


### Description 
Get the details of a single credentials

### Response Structure 
Details of the credentials
 - `id`: Unique identifier for the credentials (UUID)
 - `name`: Name of the credentials
 - `project`: Project name in which the credentials is
 - `type`: Type of the credentials
 - `reference_count`: The number of connectors using the credentials
 - `configuration`: The dictionary which contains the fields necessary for the given type with provided values. Values are not shown in response if the parameter has the protected field True.

#### Response Examples
```
{ 
  "id": "e07b3715-71c9-4a49-a8e5-179cf4778086",
  "name": "postgresql-credentials",
  "project": "project-1",
  "type": "postgresql",
  "reference_count": 2,
  "configuration": {
    "username": "user",
    "password": null,
    "host": "host",
    "port": "1234"
  }
}
```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import xenia_python_client_library
from xenia_python_client_library.rest import ApiException
from pprint import pprint
configuration = xenia_python_client_library.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.dutchanalytics.net/v1.1
configuration.host = "https://api.dutchanalytics.net/v1.1"
# Create an instance of the API class
api_instance = xenia_python_client_library.CoreApi(xenia_python_client_library.ApiClient(configuration))
project_name = 'project_name_example' # str | 
credentials_name = 'credentials_name_example' # str | 

try:
    # Get credentials
    api_response = api_instance.credentials_get(project_name, credentials_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CoreApi->credentials_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **credentials_name** | **str**|  | 

### Return type

[**CredentialsListWithConfig**](CredentialsListWithConfig.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **credentials_list**
> list[CredentialsList] credentials_list(project_name)

List credentials

 
### Description
List all the sets of credentials in a project.

### Response Structure:

A list of details of the credentials in the project
- `id`: Unique identifier for the credentials (UUID)
- `name`: Name of the credentials
- `project`: Project name in which the credentials is
- `type`: Type of the credentials
- `reference_count`: The number of connectors using the credentials
- `configuration`: The dictionary which contains the fields necessary for the given type with provided values. Values are not shown in response if the parameter has the protected field True.

#### Response Examples

```
[
  {
    "id": "da4da757-373c-4cab-948e-90ff4ab2e9c3",
    "name": "s3-credentials",
    "project": "project-1",
    "type": "s3",
    "reference_count": 1,
    "configuration": {
      "access_key": null,
      "secret_key": null,
      "region": "eu-central-1"
    }
  },
  {
    "id": "e07b3715-71c9-4a49-a8e5-179cf4778086",
    "name": "postgresql-credentials",
    "project": "project-1",
    "type": "postgresql",
    "reference_count": 2,
    "configuration": {
      "username": "user",
      "password": null,
      "host": "host",
      "port": "1234"
    }
  }
]
```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import xenia_python_client_library
from xenia_python_client_library.rest import ApiException
from pprint import pprint
configuration = xenia_python_client_library.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.dutchanalytics.net/v1.1
configuration.host = "https://api.dutchanalytics.net/v1.1"
# Create an instance of the API class
api_instance = xenia_python_client_library.CoreApi(xenia_python_client_library.ApiClient(configuration))
project_name = 'project_name_example' # str | 

try:
    # List credentials
    api_response = api_instance.credentials_list(project_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CoreApi->credentials_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 

### Return type

[**list[CredentialsList]**](CredentialsList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **credentials_update**
> CredentialsListWithConfig credentials_update(project_name, credentials_name, data)

Update credentials

 
### Description
Update a credentials. It is not possible to update the type of a credentials. All necessary fields are validated again.

### Optional Parameters 
 - `name`: New name for the credentials
 - `configuration`: A new dictionary with new values for credentials configuration. This dictionary may contain a subset of the necessary parameters for the credentials type. Only the given parameters is updated and the rest is kept at their old values.

#### Request Examples
```
{
  "name": "new-credentials-name"
}
```

```
{
  "configuration": {
    "username": "new_user",
    "password": "new_secret_password",
    "host": "new_host",
    "port": "1234"
  }
}
```

### Response Structure 
Details of the updated credentials
 - `id`: Unique identifier for the credentials (UUID)
 - `name`: Name of the credentials
 - `project`: Project name in which the credentials is
 - `type`: Type of the credentials
 - `reference_count`: The number of connectors using the credentials
 - `configuration`: The dictionary which contains the fields necessary for the given type with provided values. Values are not shown in response if the parameter has the protected field True.

#### Response Examples
```
{ 
  "id": "e07b3715-71c9-4a49-a8e5-179cf4778086",
  "name": "postgresql-credentials",
  "project": "project-1",
  "type": "postgresql",
  "reference_count": 2,
  "configuration": {
    "username": "new_user",
    "password": null,
    "host": "new_host",
    "port": "1234"
  }
}
```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import xenia_python_client_library
from xenia_python_client_library.rest import ApiException
from pprint import pprint
configuration = xenia_python_client_library.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.dutchanalytics.net/v1.1
configuration.host = "https://api.dutchanalytics.net/v1.1"
# Create an instance of the API class
api_instance = xenia_python_client_library.CoreApi(xenia_python_client_library.ApiClient(configuration))
project_name = 'project_name_example' # str | 
credentials_name = 'credentials_name_example' # str | 
data = xenia_python_client_library.CredentialsUpdate() # CredentialsUpdate | 

try:
    # Update credentials
    api_response = api_instance.credentials_update(project_name, credentials_name, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CoreApi->credentials_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **credentials_name** | **str**|  | 
 **data** | [**CredentialsUpdate**](CredentialsUpdate.md)|  | 

### Return type

[**CredentialsListWithConfig**](CredentialsListWithConfig.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **metrics_get**
> list[Metrics] metrics_get(project_name, metric, start_time, end_time, object_type, interval=interval, object_id=object_id)

Get metrics


### Description 
Get metrics for the project or a specified object

### Required Parameters 
 - `start_time`: Starting time for the metric values to be returned. It should be provided in datetime isoformat.
 - `end_time`: Ending time for the metric values to be returned. It should be provided in datetime isoformat.
 - `object_type`: The type of the object for which the metrics are requested. It can be either `model_version`, `connector` or `pipeline`.

### Optional Parameters 
 - `interval`: Interval for the metric value. It can be minute, hour, day or month. The metric values will be aggregated according to this interval. The default value is hour.
 - `object_id`: Uuid of the specific object for which the metrics are requested. When it is not provided, the metrics are aggregated for the given `object_type`.

### Response Structure 
 - `start_time`: Timestamp denoting the start of the period over which the metric was measured
 - `end_time`: Timestamp denoting the end of the period over which the metric was measured
 - `value`: Aggregated metric value for the given unit

#### Response Examples
With unit as minute, start_time as 2019-11-13 12:00:00 and end_time as 2019-11-13 12:03:00
```
[
  {
    "start_time": "2019-11-13T12:00:00+00:00",
    "end_time": "2019-11-13T12:01:00+00:00",
    "value": 100
  },
  {
    "start_time": "2019-11-13T12:01:00+00:00",
    "end_time": "2019-11-13T12:02:00+00:00",
    "value": 134
  },
  {
    "start_time": "2019-11-13T12:02:00+00:00",
    "end_time": "2019-11-13T12:03:00+00:00",
    "value": 112
  }
]

```

With unit as hour, start_time as 2019-11-13 12:00:00 and end_time as 2019-11-13 14:00:00
```
[
  {
   "start_time": "2019-11-13T12:00:00+00:00",
   "end_time": "2019-11-13T13:00:00+00:00",
   "value": 92
  },
  {
    "start_time": "2019-11-13T13:00:00+00:00",
    "end_time": "2019-11-13T14:00:00+00:00",
    "value": 120
  },
  {
    "start_time": "2019-11-13T14:00:00+00:00",
    "end_time": "2019-11-13T15:00:00+00:00",
    "value": 0
  }
]
```
 
With unit as day, start_time as 2019-11-13 12:00:00 and end_time as 2019-11-14 12:00:00
```
[
  {
   "start_time": "2019-11-13T00:00:00+00:00",
   "end_time": "2019-11-14T00:00:00+00:00",
   "value": 528
  },
  {
    "start_time": "2019-11-14T00:00:00+00:00",
    "end_time": "2019-11-15T00:00:00+00:00",
    "value": 342
  }
]
```
 
With unit as month, start_time as 2019-11-13 12:00:00 and end_time as 2019-12-13 12:00:00
```
[
  {
   "start_time": "2019-11-01T00:00:00+00:00",
   "end_time": "2019-12-01T00:00:00+00:00",
   "value": 1983
  }
]
```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import xenia_python_client_library
from xenia_python_client_library.rest import ApiException
from pprint import pprint
configuration = xenia_python_client_library.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.dutchanalytics.net/v1.1
configuration.host = "https://api.dutchanalytics.net/v1.1"
# Create an instance of the API class
api_instance = xenia_python_client_library.CoreApi(xenia_python_client_library.ApiClient(configuration))
project_name = 'project_name_example' # str | 
metric = 'metric_example' # str | 
start_time = 'start_time_example' # str | 
end_time = 'end_time_example' # str | 
object_type = 'object_type_example' # str | 
interval = 'interval_example' # str |  (optional)
object_id = 'object_id_example' # str |  (optional)

try:
    # Get metrics
    api_response = api_instance.metrics_get(project_name, metric, start_time, end_time, object_type, interval=interval, object_id=object_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CoreApi->metrics_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **metric** | **str**|  | 
 **start_time** | **str**|  | 
 **end_time** | **str**|  | 
 **object_type** | **str**|  | 
 **interval** | **str**|  | [optional] 
 **object_id** | **str**|  | [optional] 

### Return type

[**list[Metrics]**](Metrics.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **model_blob_requests_get**
> ModelRequestResultList model_blob_requests_get(project_name, model_name, request_id, version)

Get blob model request results


### Description 
Retrieve the result of a blob model request using the request_id. All users with permission to the project are able to collect the request result, not only the user that created the request.
If the model request is still 'pending' or 'failed', the response will be a JSON dict. If the model request has ended with 'success', the blob is attached.  

### Response Structure 
A successful blob model request
- `file`: The blob that was outputted by the model

A pending/failed blob model request
 - `time_created`: Server time that the request was made (current time)
 - `time_last_updated`: Server time that the request was last updated (current time)
 - `status`: Status of the request. May be pending or failed.
 - `request_id`: Unique identifier for the model request, to be used when collecting the result
 - `result`: Model request result value. NULL if not (yet) available or if the request failed.
 - `error_message`: An error message explaining why the request has failed. NULL if the request was successful.
 - `prediction_duration`: The time it took for the model request to complete in seconds.

#### Response Examples 
A successful model request
```
The blob file
```

A failed model request
```
{
  "request_id": "5b65e27e-25ea-4be0-86c7-54e94f22dab0",
  "time_created": "2019-02-22T09:19:51.919276Z",
  "time_last_updated": "2019-02-22T09:19:52.532876Z",
  "status": "failed",
  "result": null,
  "error_message": "Asset ID not supported",
  "prediction_duration": 0
}
```

A pending model request
```
{
  "request_id": "5b65e27e-25ea-4be0-86c7-54e94f22dab0",
  "time_created": "2019-02-22T09:19:51.919276Z",
  "time_last_updated": "2019-02-22T09:19:51.919276Z",
  "status": "pending",
  "result": null,
  "error_message": null,
  "prediction_duration": 0
}
```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import xenia_python_client_library
from xenia_python_client_library.rest import ApiException
from pprint import pprint
configuration = xenia_python_client_library.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.dutchanalytics.net/v1.1
configuration.host = "https://api.dutchanalytics.net/v1.1"
# Create an instance of the API class
api_instance = xenia_python_client_library.CoreApi(xenia_python_client_library.ApiClient(configuration))
project_name = 'project_name_example' # str | 
model_name = 'model_name_example' # str | 
request_id = 'request_id_example' # str | 
version = 'version_example' # str | 

try:
    # Get blob model request results
    api_response = api_instance.model_blob_requests_get(project_name, model_name, request_id, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CoreApi->model_blob_requests_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **model_name** | **str**|  | 
 **request_id** | **str**|  | 
 **version** | **str**|  | 

### Return type

[**ModelRequestResultList**](ModelRequestResultList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **model_environment_variables_create**
> EnvironmentVariableList model_environment_variables_create(project_name, model_name, data)

Create model environment variable


### Description
Create an environment variable for the model. This variable will be inherited by all versions of this model. Variables inherited from the project can be shadowed by creating a variable with the same name.

### Required Parameters
 - `name`: The name of the variable. The variable will have this name when accessed from your model code. The variable name should contain only letters and underscores, and not start or end with an underscore.
 - `value`: The value of the variable as a string. It may be an empty string ("").
 - `secret`: If this variable contains sensitive information, set this to true to hide it from other users.

#### Request Examples
```
{
  "name": "model_variable_a",
  "value": "some_value",
  "secret": false
}
```

### Response Structure 
 A list of variables described by the following fields:
 - `id`: Unique identifier for the environment variable
 - `name`: Variable name
 - `value`: Variable value (will be null for secret variables)
 - `secret`: Boolean that indicates if this variable contains sensitive information

#### Response Examples 
```
{
"id": "7c28a2be-507e-4fae-981d-54e94f22dab0",
"name": "model_variable_a",
"value": "some_value",
"secret": false
}
```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import xenia_python_client_library
from xenia_python_client_library.rest import ApiException
from pprint import pprint
configuration = xenia_python_client_library.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.dutchanalytics.net/v1.1
configuration.host = "https://api.dutchanalytics.net/v1.1"
# Create an instance of the API class
api_instance = xenia_python_client_library.CoreApi(xenia_python_client_library.ApiClient(configuration))
project_name = 'project_name_example' # str | 
model_name = 'model_name_example' # str | 
data = xenia_python_client_library.EnvironmentVariableCreate() # EnvironmentVariableCreate | 

try:
    # Create model environment variable
    api_response = api_instance.model_environment_variables_create(project_name, model_name, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CoreApi->model_environment_variables_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **model_name** | **str**|  | 
 **data** | [**EnvironmentVariableCreate**](EnvironmentVariableCreate.md)|  | 

### Return type

[**EnvironmentVariableList**](EnvironmentVariableList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **model_environment_variables_delete**
> model_environment_variables_delete(project_name, id, model_name)

Delete model environment variable


### Description

Delete an environment variable of the model.

### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import xenia_python_client_library
from xenia_python_client_library.rest import ApiException
from pprint import pprint
configuration = xenia_python_client_library.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.dutchanalytics.net/v1.1
configuration.host = "https://api.dutchanalytics.net/v1.1"
# Create an instance of the API class
api_instance = xenia_python_client_library.CoreApi(xenia_python_client_library.ApiClient(configuration))
project_name = 'project_name_example' # str | 
id = 'id_example' # str | 
model_name = 'model_name_example' # str | 

try:
    # Delete model environment variable
    api_instance.model_environment_variables_delete(project_name, id, model_name)
except ApiException as e:
    print("Exception when calling CoreApi->model_environment_variables_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **id** | **str**|  | 
 **model_name** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **model_environment_variables_get**
> EnvironmentVariableList model_environment_variables_get(project_name, id, model_name)

Get model environment variable


### Description
Retrieve details of a model environment variable. This cannot be used to retrieve details of inherited variables.

### Response Structure 
 A list of variables described by the following fields:
 - `id`: Unique identifier for the environment variable
 - `name`: Variable name
 - `value`: Variable value (will be null for secret variables)
 - `secret`: Boolean that indicates if this variable contains sensitive information

#### Response Examples 
```
[
  {
    "id": "4c15a27e-25ea-4be0-86c7-f4790389d061",
    "name": "database_schema",
    "value": "public",
    "secret": false
  }
]
```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import xenia_python_client_library
from xenia_python_client_library.rest import ApiException
from pprint import pprint
configuration = xenia_python_client_library.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.dutchanalytics.net/v1.1
configuration.host = "https://api.dutchanalytics.net/v1.1"
# Create an instance of the API class
api_instance = xenia_python_client_library.CoreApi(xenia_python_client_library.ApiClient(configuration))
project_name = 'project_name_example' # str | 
id = 'id_example' # str | 
model_name = 'model_name_example' # str | 

try:
    # Get model environment variable
    api_response = api_instance.model_environment_variables_get(project_name, id, model_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CoreApi->model_environment_variables_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **id** | **str**|  | 
 **model_name** | **str**|  | 

### Return type

[**EnvironmentVariableList**](EnvironmentVariableList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **model_environment_variables_list**
> list[InheritedEnvironmentVariableList] model_environment_variables_list(project_name, model_name)

List model environment variables


### Description
List the environment variables defined for the model. Includes environment variables defined at project level.
 
### Response Structure 
 A list of variables described by the following fields:
 - `id`: Unique identifier for the environment variable
 - `name`: Variable name
 - `value`: Variable value (will be null for secret variables)
 - `secret`: Boolean that indicates if this variable contains sensitive information
 - `inheritance_type`: Type of parent object that this variable is inherited from - can be `project` or empty if the variable was defined for the model directly
 - `inheritance_name`: Name of the parent object that this variable is inherited from - will be empty if the variable was defined for the model directly

#### Response Examples 
```
[
  {
    "id": "4c15a27e-25ea-4be0-86c7-f4790389d061",
    "name": "database_schema",
    "value": "public",
    "secret": false,
    "inheritance_type": "",
    "inheritance_name": ""
  },
  {
    "id": "06c2c8be-507e-4fae-981d-54e94f22dab0",
    "name": "database_password",
    "value": null,
    "secret": true,
    "inheritance_type": "project",
    "inheritance_name": "project_name"
  }
]
```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import xenia_python_client_library
from xenia_python_client_library.rest import ApiException
from pprint import pprint
configuration = xenia_python_client_library.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.dutchanalytics.net/v1.1
configuration.host = "https://api.dutchanalytics.net/v1.1"
# Create an instance of the API class
api_instance = xenia_python_client_library.CoreApi(xenia_python_client_library.ApiClient(configuration))
project_name = 'project_name_example' # str | 
model_name = 'model_name_example' # str | 

try:
    # List model environment variables
    api_response = api_instance.model_environment_variables_list(project_name, model_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CoreApi->model_environment_variables_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **model_name** | **str**|  | 

### Return type

[**list[InheritedEnvironmentVariableList]**](InheritedEnvironmentVariableList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **model_environment_variables_update**
> EnvironmentVariableList model_environment_variables_update(project_name, id, model_name, data)

Update model environment variable


### Description
Update an environment variable for the model. This cannot be used to update inherited variables; to change an inherited variable for a specific model you can create a variable with the same name for the model.

### Required Parameters
 - `name`: The name of the variable. The variable will have this name when accessed from your model code. The variable name should contain only letters and underscores, and not start or end with an underscore.
 - `value`: The value of the variable as a string. It may be an empty string ("").
 - `secret`: If this variable contains sensitive information, set this to true to hide it from other users. Can be updated from false to true, but not from true to false (i.e. secrets will stay secrets).

#### Request Examples
```
{
  "name": "model_variable_a",
  "value": "some new value",
  "secret": false
}
```

### Response Structure 
 A list of variables described by the following fields:
 - `id`: Unique identifier for the environment variable
 - `name`: Variable name
 - `value`: Variable value (will be null for secret variables)
 - `secret`: Boolean that indicates if this variable contains sensitive information

#### Response Examples 
```
{
"id": "7c28a2be-507e-4fae-981d-54e94f22dab0",
"name": "model_variable_a",
"value": "some new value",
"secret": false
}
```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import xenia_python_client_library
from xenia_python_client_library.rest import ApiException
from pprint import pprint
configuration = xenia_python_client_library.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.dutchanalytics.net/v1.1
configuration.host = "https://api.dutchanalytics.net/v1.1"
# Create an instance of the API class
api_instance = xenia_python_client_library.CoreApi(xenia_python_client_library.ApiClient(configuration))
project_name = 'project_name_example' # str | 
id = 'id_example' # str | 
model_name = 'model_name_example' # str | 
data = xenia_python_client_library.EnvironmentVariableCreate() # EnvironmentVariableCreate | 

try:
    # Update model environment variable
    api_response = api_instance.model_environment_variables_update(project_name, id, model_name, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CoreApi->model_environment_variables_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **id** | **str**|  | 
 **model_name** | **str**|  | 
 **data** | [**EnvironmentVariableCreate**](EnvironmentVariableCreate.md)|  | 

### Return type

[**EnvironmentVariableList**](EnvironmentVariableList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **model_requests_create**
> ModelRequestList model_requests_create(project_name, model_name, version, data)

Create model requests


### Description 
Request a prediction from a model. Asynchronous method, as the request is queued in our back-end and can be collected at a later time using the model request collect methods. Model requests are made for a specific version of a model. It is only possible to make a model request if a model file is uploaded for that model version and the model build has succeeded (meaning that the model version is in available state).

This type of requests can only be made to models with structured input type.

### Required Parameters
A dictionary which contains the input fields of the model as keys.
- `data`: Request data. It should contain the input fields of the model as keys.

#### Request Examples 
```
{
  "data": {
    "model-input-field-1": 5.0,
    "model-input-field-2": "N",
    "model-input-field-3": [0.25, 0.25, 2.1, 16.3]
  }
}
```

### Response Structure 
Details of the created model request
 - `time_created`: Server time that the request was made (current time)
 - `status`: Status of the request. Always pending when initialised, later it can be in success or failed.
 - `request_id`: Unique identifier for the model request, which can be used to collect the result

#### Response Examples
```
{
  "time_created": "2019-02-22T09:19:51.919276Z",
  "status": "pending",
  "request_id": "5b65e27e-25ea-4be0-86c7-54e94f22dab0"
}
```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import xenia_python_client_library
from xenia_python_client_library.rest import ApiException
from pprint import pprint
configuration = xenia_python_client_library.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.dutchanalytics.net/v1.1
configuration.host = "https://api.dutchanalytics.net/v1.1"
# Create an instance of the API class
api_instance = xenia_python_client_library.CoreApi(xenia_python_client_library.ApiClient(configuration))
project_name = 'project_name_example' # str | 
model_name = 'model_name_example' # str | 
version = 'version_example' # str | 
data = xenia_python_client_library.ModelRequestCreate() # ModelRequestCreate | 

try:
    # Create model requests
    api_response = api_instance.model_requests_create(project_name, model_name, version, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CoreApi->model_requests_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **model_name** | **str**|  | 
 **version** | **str**|  | 
 **data** | [**ModelRequestCreate**](ModelRequestCreate.md)|  | 

### Return type

[**ModelRequestList**](ModelRequestList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **model_requests_create_blob**
> ModelRequestList model_requests_create_blob(project_name, model_name, version, file)

Create blob model requests


### Description 
Make a blob request to a model. Asynchronous method, as the request is queued in our back-end and can be collected at a later time using the model request collect methods. Model requests are made for a specific version of a model. It is only possible to make a model request if a model file is uploaded for that model version and the model build has succeeded (meaning that the model version is in available state).

This type of request can only be made to models with blob input type.

### Required Parameters 
- `file`: Blob file

### Response Structure 
Details of the created model request
 - `time_created`: Server time that the request was made (current time)
 - `status`: Status of the request. Always pending when initialised, later it can be in success or failed.
 - `request_id`: Unique identifier for the model request, which can be used to collect the result
 
#### Response Examples 
```
{
  "time_created": "2019-02-22T09:19:51.919276Z",
  "status": "pending",
  "request_id": "5b65e27e-25ea-4be0-86c7-54e94f22dab0"
}
```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import xenia_python_client_library
from xenia_python_client_library.rest import ApiException
from pprint import pprint
configuration = xenia_python_client_library.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.dutchanalytics.net/v1.1
configuration.host = "https://api.dutchanalytics.net/v1.1"
# Create an instance of the API class
api_instance = xenia_python_client_library.CoreApi(xenia_python_client_library.ApiClient(configuration))
project_name = 'project_name_example' # str | 
model_name = 'model_name_example' # str | 
version = 'version_example' # str | 
file = '/path/to/file' # file | 

try:
    # Create blob model requests
    api_response = api_instance.model_requests_create_blob(project_name, model_name, version, file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CoreApi->model_requests_create_blob: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **model_name** | **str**|  | 
 **version** | **str**|  | 
 **file** | **file**|  | 

### Return type

[**ModelRequestList**](ModelRequestList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **model_requests_create_bulk**
> list[ModelRequestList] model_requests_create_bulk(project_name, model_name, version, data)

Create bulk model requests


### Description
Request multiple predictions from a model. The request follows an asynchronous method, as the requests are queued in our back-end and can be collected at a later time using the model request collect methods. It is only possible to make a model request if a model file is uploaded for that model version and the model build has succeeded (meaning that the model version is in available state).

This type of request can only be made to models with structured input type. 

If one of the requests is faulty, all requests are denied. It is also possible to do a single model request with this method. The maximum number of requests per bulk call is 250.

### Required Parameters 
A list of dictionaries, with each dictionary being a model request that contains the required parameters.
- `data`: Request data. It should contain the input fields of the model as keys.

#### Request Examples 
```
[
  {
    "data": {
      "model-input-field-1": 5.0,
      "model-input-field-2": "N",
      "model-input-field-3": [0.25, 0.25, 2.1, 16.3]
    }
  },
  {
    "data": {
      "model-input-field-1": 3.0,
      "model-input-field-2": "S",
      "model-input-field-3": [4.23, 3.27, 2.41, 12.4]
    }
  }
]
```
 
### Response Structure 
 A list of dictionaries containing the details of the created model requests with the following fields:
 - `time_created`: Server time that the request was made (current time)
 - `status`: Status of the request. Always pending when initialised, later it can be in success or failed.
 - `request_id`: Unique identifier for the model request, which can be used to collect the result

#### Response Examples 
```
[
  {
    "time_created": "2019-02-22T09:19:51.919276Z",
    "status": "pending",
    "request_id": "5b65e27e-25ea-4be0-86c7-54e94f22dab0"
  },
  {
    "time_created": "2019-02-22T09:19:51.919308Z",
    "status": "pending",
    "request_id": "06c2c8be-507e-4fae-981d-f4790389d061"
  }
]
```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import xenia_python_client_library
from xenia_python_client_library.rest import ApiException
from pprint import pprint
configuration = xenia_python_client_library.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.dutchanalytics.net/v1.1
configuration.host = "https://api.dutchanalytics.net/v1.1"
# Create an instance of the API class
api_instance = xenia_python_client_library.CoreApi(xenia_python_client_library.ApiClient(configuration))
project_name = 'project_name_example' # str | 
model_name = 'model_name_example' # str | 
version = 'version_example' # str | 
data = [xenia_python_client_library.ModelRequestCreate()] # list[ModelRequestCreate] | 

try:
    # Create bulk model requests
    api_response = api_instance.model_requests_create_bulk(project_name, model_name, version, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CoreApi->model_requests_create_bulk: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **model_name** | **str**|  | 
 **version** | **str**|  | 
 **data** | [**list[ModelRequestCreate]**](ModelRequestCreate.md)|  | 

### Return type

[**list[ModelRequestList]**](ModelRequestList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **model_requests_get**
> ModelRequestResultList model_requests_get(project_name, model_name, request_id, version)

Get model request results


### Description 
Retrieve the result of a model request with status, result and error message using the request_id. All users with permission to the project are able to collect the request result, not only the user that created the request.

### Response Structure 
Details of the model request
 - `time_created`: Server time that the request was made (current time)
 - `time_last_updated`: Server time that the request was last updated (current time)
 - `status`: Status of the request. Always pending when initialised, later it can be in success or failed.
 - `request_id`: Unique identifier for the model request, to be used when collecting the result
 - `result`: Model request result value. NULL if not (yet) available or if the request failed.
 - `error_message`: An error message explaining why the request has failed. NULL if the request was successful.
 - `prediction_duration`: The time it took for the model request to complete in seconds.

#### Response Examples 
A successful model request
```
{
  "request_id": "5b65e27e-25ea-4be0-86c7-54e94f22dab0",
  "time_created": "2019-02-22T09:19:51.919276Z",
  "time_last_updated": "2019-02-22T09:19:52.532876Z",
  "status": "success",
  "result": "2.1369",
  "error_message": null,
  "prediction_duration": 0.1
}
```
 
A failed model request
```
{
  "request_id": "5b65e27e-25ea-4be0-86c7-54e94f22dab0",
  "time_created": "2019-02-22T09:19:51.919276Z",
  "time_last_updated": "2019-02-22T09:19:52.532876Z",
  "status": "failed",
  "result": null,
  "error_message": "Asset ID not supported",
  "prediction_duration": 0
}
```
 
A pending model request
```
{
  "request_id": "5b65e27e-25ea-4be0-86c7-54e94f22dab0",
  "time_created": "2019-02-22T09:19:51.919276Z",
  "time_last_updated": "2019-02-22T09:19:51.919276Z",
  "status": "pending",
  "result": null,
  "error_message": null,
  "prediction_duration": 0
}
```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import xenia_python_client_library
from xenia_python_client_library.rest import ApiException
from pprint import pprint
configuration = xenia_python_client_library.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.dutchanalytics.net/v1.1
configuration.host = "https://api.dutchanalytics.net/v1.1"
# Create an instance of the API class
api_instance = xenia_python_client_library.CoreApi(xenia_python_client_library.ApiClient(configuration))
project_name = 'project_name_example' # str | 
model_name = 'model_name_example' # str | 
request_id = 'request_id_example' # str | 
version = 'version_example' # str | 

try:
    # Get model request results
    api_response = api_instance.model_requests_get(project_name, model_name, request_id, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CoreApi->model_requests_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **model_name** | **str**|  | 
 **request_id** | **str**|  | 
 **version** | **str**|  | 

### Return type

[**ModelRequestResultList**](ModelRequestResultList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **model_requests_get_bulk**
> list[ModelRequestResultList] model_requests_get_bulk(project_name, model_name, version, data)

Get model request results bulk


### Description
Get the results of multiple model requests with status, result and error message using their request_id. All users with permission to the project are able to collect the request results, not only the user that created the request.

If one of the requests ids doesn't exist, the entire request fails returning a 404 error. The maximum number of requests per bulk call is 250.

### Required Parameters 
 A list of one or more dictionaries with id as the key.
- `id`: Request ids to collect

#### Request Examples 
A single request to collect

```
[
  {
    "id": "5b65e27e-25ea-4be0-86c7-54e94f22dab0"
  },
  {
    "id": "fb1a0c98-f6e1-4271-8fdf-97425e7876a8"
  }
]
```

### Response Structure 
A list of dictionaries containing the details of the requests
 - `time_created`: Server time that the request was made (current time)
 - `time_last_updated`: Server time that the request was last updated (current time)
 - `status`: Status of the request. Always pending when initialised, later it can be in success or failed.
 - `request_id`: Unique identifier for the model request, to be used when collecting the result
 - `result`: Model request result value. NULL if not (yet) available or if the request failed.
 - `error_message`: An error message explaining why the request has failed. NULL if the request was successful.
 - `prediction_duration`: The time it took for the model request to complete in seconds.

#### Response Examples 
```
[
  {
    "request_id": "5b65e27e-25ea-4be0-86c7-54e94f22dab0",
    "time_created": "2019-02-22T09:19:51.919276Z",
    "time_last_updated": "2019-02-22T09:19:52.532876Z",
    "status": "success",
    "result": "2.1369",
    "error_message": null,
    "prediction_duration": 0.1
  },
  {
    "request_id": "fb1a0c98-f6e1-4271-8fdf-97425e7876a8",
    "time_created": "2019-02-22T09:19:51.919276Z",
    "time_last_updated": "2019-02-22T09:19:52.532876Z",
    "status": "failed",
    "result": null,
    "error_message": "Asset ID not supported",
    "prediction_duration": 0
  }
]
```                      


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import xenia_python_client_library
from xenia_python_client_library.rest import ApiException
from pprint import pprint
configuration = xenia_python_client_library.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.dutchanalytics.net/v1.1
configuration.host = "https://api.dutchanalytics.net/v1.1"
# Create an instance of the API class
api_instance = xenia_python_client_library.CoreApi(xenia_python_client_library.ApiClient(configuration))
project_name = 'project_name_example' # str | 
model_name = 'model_name_example' # str | 
version = 'version_example' # str | 
data = [xenia_python_client_library.ModelRequestResultCreate()] # list[ModelRequestResultCreate] | 

try:
    # Get model request results bulk
    api_response = api_instance.model_requests_get_bulk(project_name, model_name, version, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CoreApi->model_requests_get_bulk: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **model_name** | **str**|  | 
 **version** | **str**|  | 
 **data** | [**list[ModelRequestResultCreate]**](ModelRequestResultCreate.md)|  | 

### Return type

[**list[ModelRequestResultList]**](ModelRequestResultList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **model_requests_get_pending**
> list[ModelRequestResultList] model_requests_get_pending(project_name, model_name, version)

Get pending model requests


### Description 
Retrieve a list of all pending requests for a specific version of a model. All users with permission to the project are able to collect the pending model requests, not just the user that created the request.

### Response Structure 
List of details of all model requests
 - `time_created`: Server time that the request was made (current time)
 - `time_last_updated`: Server time that the request was last updated (current time)
 - `status`: Status of the request, which will always be pending in this case.
 - `request_id`: Unique identifier for the model request, to be used when collecting the result
 - `result`: Model request result value, which will always be NULL in this case.
 - `error_message`: An error message explaining why the request has failed, which will always be NULL in this case.
 - `prediction_duration`: The time it took for the model request to complete in seconds.

#### Response Examples 
A list of pending model requests

```
[
  {
    "time_created": "2020-02-03T13:19:45.310+00:00",
    "time_last_updated": "2020-02-03T13:19:45.310+00:00",
    "status": "pending",
    "request_id": "b91857ac-f48c-49a0-a26c-36f07df43a56",
    "result": null,
    "error_message": null,
    "prediction_duration": 0
  },
  {
    "time_created": "2020-02-03T13:19:46.909+00:00",
    "time_last_updated": "2020-02-03T13:19:46.909+00:00",
    "status": "pending",
    "request_id": "4c3abed9-5149-42c9-8768-5c66209c4fb3",
    "result": null,
    "error_message": null,
    "prediction_duration": 0
  }
]


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import xenia_python_client_library
from xenia_python_client_library.rest import ApiException
from pprint import pprint
configuration = xenia_python_client_library.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.dutchanalytics.net/v1.1
configuration.host = "https://api.dutchanalytics.net/v1.1"
# Create an instance of the API class
api_instance = xenia_python_client_library.CoreApi(xenia_python_client_library.ApiClient(configuration))
project_name = 'project_name_example' # str | 
model_name = 'model_name_example' # str | 
version = 'version_example' # str | 

try:
    # Get pending model requests
    api_response = api_instance.model_requests_get_pending(project_name, model_name, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CoreApi->model_requests_get_pending: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **model_name** | **str**|  | 
 **version** | **str**|  | 

### Return type

[**list[ModelRequestResultList]**](ModelRequestResultList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **model_version_environment_variables_create**
> EnvironmentVariableList model_version_environment_variables_create(project_name, model_name, version, data)

Create model version environment variable


### Description
Create an environment variable for the model version. Variables inherited from the project or model can be shadowed by creating a variable with the same name.

### Required Parameters
 - `name`: The name of the variable. The variable will have this name when accessed from your model code. The variable name should contain only letters and underscores, and not start or end with an underscore.
 - `value`: The value of the variable as a string. It may be an empty string ("").
 - `secret`: If this variable contains sensitive information, set this to true to hide it from other users.

#### Request Examples
```
{
  "name": "version_variable",
  "value": "another one",
  "secret": false
}
```

### Response Structure 
 A list of variables described by the following fields:
 - `id`: Unique identifier for the environment variable
 - `name`: Variable name
 - `value`: Variable value (will be null for secret variables)
 - `secret`: Boolean that indicates if this variable contains sensitive information

#### Response Examples 
```
{
"id": "54e94fbe-507e-4fae-981d-227c28a2dab0",
"name": "version_variable",
"value": "another one",
"secret": false
}
```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import xenia_python_client_library
from xenia_python_client_library.rest import ApiException
from pprint import pprint
configuration = xenia_python_client_library.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.dutchanalytics.net/v1.1
configuration.host = "https://api.dutchanalytics.net/v1.1"
# Create an instance of the API class
api_instance = xenia_python_client_library.CoreApi(xenia_python_client_library.ApiClient(configuration))
project_name = 'project_name_example' # str | 
model_name = 'model_name_example' # str | 
version = 'version_example' # str | 
data = xenia_python_client_library.EnvironmentVariableCreate() # EnvironmentVariableCreate | 

try:
    # Create model version environment variable
    api_response = api_instance.model_version_environment_variables_create(project_name, model_name, version, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CoreApi->model_version_environment_variables_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **model_name** | **str**|  | 
 **version** | **str**|  | 
 **data** | [**EnvironmentVariableCreate**](EnvironmentVariableCreate.md)|  | 

### Return type

[**EnvironmentVariableList**](EnvironmentVariableList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **model_version_environment_variables_delete**
> model_version_environment_variables_delete(project_name, id, model_name, version)

Delete model version environment variable


### Description

Delete an environment variable of the model version.

### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import xenia_python_client_library
from xenia_python_client_library.rest import ApiException
from pprint import pprint
configuration = xenia_python_client_library.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.dutchanalytics.net/v1.1
configuration.host = "https://api.dutchanalytics.net/v1.1"
# Create an instance of the API class
api_instance = xenia_python_client_library.CoreApi(xenia_python_client_library.ApiClient(configuration))
project_name = 'project_name_example' # str | 
id = 'id_example' # str | 
model_name = 'model_name_example' # str | 
version = 'version_example' # str | 

try:
    # Delete model version environment variable
    api_instance.model_version_environment_variables_delete(project_name, id, model_name, version)
except ApiException as e:
    print("Exception when calling CoreApi->model_version_environment_variables_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **id** | **str**|  | 
 **model_name** | **str**|  | 
 **version** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **model_version_environment_variables_get**
> EnvironmentVariableList model_version_environment_variables_get(project_name, id, model_name, version)

Get model version environment variable


### Description
Retrieve details of a model version environment variable. This cannot be used to retrieve details of inherited variables.

### Response Structure 
 A list of variables described by the following fields:
 - `id`: Unique identifier for the environment variable
 - `name`: Variable name
 - `value`: Variable value (will be null for secret variables)
 - `secret`: Boolean that indicates if this variable contains sensitive information

#### Response Examples 
```
[
  {
    "id": "4c15a27e-25ea-4be0-86c7-f4790389d061",
    "name": "database_schema",
    "value": "public",
    "secret": false
  }
]
```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import xenia_python_client_library
from xenia_python_client_library.rest import ApiException
from pprint import pprint
configuration = xenia_python_client_library.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.dutchanalytics.net/v1.1
configuration.host = "https://api.dutchanalytics.net/v1.1"
# Create an instance of the API class
api_instance = xenia_python_client_library.CoreApi(xenia_python_client_library.ApiClient(configuration))
project_name = 'project_name_example' # str | 
id = 'id_example' # str | 
model_name = 'model_name_example' # str | 
version = 'version_example' # str | 

try:
    # Get model version environment variable
    api_response = api_instance.model_version_environment_variables_get(project_name, id, model_name, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CoreApi->model_version_environment_variables_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **id** | **str**|  | 
 **model_name** | **str**|  | 
 **version** | **str**|  | 

### Return type

[**EnvironmentVariableList**](EnvironmentVariableList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **model_version_environment_variables_list**
> list[InheritedEnvironmentVariableList] model_version_environment_variables_list(project_name, model_name, version)

List model version environment variables


### Description
List the environment variables defined for the model version. Includes environment variables defined at project level and model level.
 
### Response Structure 
 A list of variables described by the following fields:
 - `id`: Unique identifier for the environment variable
 - `name`: Variable name
 - `value`: Variable value (will be null for secret variables)
 - `secret`: Boolean that indicates if this variable contains sensitive information
 - `inheritance_type`: Type of parent object that this variable is inherited from - can be `project`, `model`, or empty if the variable was defined for the model version directly
 - `inheritance_name`: Name of the parent object that this variable is inherited from - will be empty if the variable was defined for the model version directly

#### Response Examples 
```
[
  {
    "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
    "name": "version_specific_variable",
    "value": "some_value",
    "secret": false,
    "inheritance_type": "",
    "inheritance_name": ""
  },
  {
    "id": "4c15a27e-25ea-4be0-86c7-f4790389d061",
    "name": "database_schema",
    "value": "public",
    "secret": false,
    "inheritance_type": "model",
    "inheritance_name": "model_name"
  },
  {
    "id": "06c2c8be-507e-4fae-981d-54e94f22dab0",
    "name": "database_password",
    "value": null,
    "secret": true,
    "inheritance_type": "project",
    "inheritance_name": "project_name"
  }
]
```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import xenia_python_client_library
from xenia_python_client_library.rest import ApiException
from pprint import pprint
configuration = xenia_python_client_library.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.dutchanalytics.net/v1.1
configuration.host = "https://api.dutchanalytics.net/v1.1"
# Create an instance of the API class
api_instance = xenia_python_client_library.CoreApi(xenia_python_client_library.ApiClient(configuration))
project_name = 'project_name_example' # str | 
model_name = 'model_name_example' # str | 
version = 'version_example' # str | 

try:
    # List model version environment variables
    api_response = api_instance.model_version_environment_variables_list(project_name, model_name, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CoreApi->model_version_environment_variables_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **model_name** | **str**|  | 
 **version** | **str**|  | 

### Return type

[**list[InheritedEnvironmentVariableList]**](InheritedEnvironmentVariableList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **model_version_environment_variables_update**
> EnvironmentVariableList model_version_environment_variables_update(project_name, id, model_name, version, data)

Update model version environment variable


### Description
Update an environment variable for the model version. This cannot be used to update inherited variables; to change an inherited variable for a specific version you can create a variable with the same name for the version.

### Required Parameters
 - `name`: The name of the variable. The variable will have this name when accessed from your model code. The variable name should contain only letters and underscores, and not start or end with an underscore.
 - `value`: The value of the variable as a string. It may be an empty string ("").
 - `secret`: If this variable contains sensitive information, set this to true to hide it from other users. Can be updated from false to true, but not from true to false (i.e. secrets will stay secrets).

#### Request Examples
```
{
  "name": "version_variable",
  "value": "yet another one",
  "secret": false
}
```

### Response Structure 
 A list of variables described by the following fields:
 - `id`: Unique identifier for the environment variable
 - `name`: Variable name
 - `value`: Variable value (will be null for secret variables)
 - `secret`: Boolean that indicates if this variable contains sensitive information

#### Response Examples 
```
{
"id": "54e94fbe-507e-4fae-981d-227c28a2dab0",
"name": "version_variable",
"value": "yet another one",
"secret": false
}
```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import xenia_python_client_library
from xenia_python_client_library.rest import ApiException
from pprint import pprint
configuration = xenia_python_client_library.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.dutchanalytics.net/v1.1
configuration.host = "https://api.dutchanalytics.net/v1.1"
# Create an instance of the API class
api_instance = xenia_python_client_library.CoreApi(xenia_python_client_library.ApiClient(configuration))
project_name = 'project_name_example' # str | 
id = 'id_example' # str | 
model_name = 'model_name_example' # str | 
version = 'version_example' # str | 
data = xenia_python_client_library.EnvironmentVariableCreate() # EnvironmentVariableCreate | 

try:
    # Update model version environment variable
    api_response = api_instance.model_version_environment_variables_update(project_name, id, model_name, version, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CoreApi->model_version_environment_variables_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **id** | **str**|  | 
 **model_name** | **str**|  | 
 **version** | **str**|  | 
 **data** | [**EnvironmentVariableCreate**](EnvironmentVariableCreate.md)|  | 

### Return type

[**EnvironmentVariableList**](EnvironmentVariableList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **model_versions_create**
> ModelVersionList model_versions_create(project_name, model_name, data)

Create model versions


### Description 
Create a version for a model by defining the version and language.

### Required Parameters 
- `version`: Name of the version of the model

### Optional Parameters 
 - `language`: Language in which the model version is provided. It can be python2.7, python3.5, python3.6 or python3.7. The default value is python3.7
 - `memory_allocation`: The reserved memory for the version in mb. This value determines the memory allocated to the model version: it should to be enough to encompass the model file and all requirements that need to be installed. The default value is 2048. The minimum and maximum values are 256 and 32768 respectively.
 - `maximum_deployments`: Upper bound of number of model pods running in parallel. The default value is 5. Indicator of resource capacity: if many model requests need to be handled in a short time, this number can be set higher to avoid long waiting times.
 - `minimum_deployments`: Lower bound of number of model pods running in parallel. The default value is 0. Set this value higher than 0 to always have a model pod available, but keep in mind that this may be costly.
 - `unused_shutdown_time`: Maximum time in minutes a model pod stays active after a model request. A higher value means a model pod stays active longer, but this can also get costly. Sending requests to an active model pod means it will be already initialized and thus take a shorter timer. If the time a request takes to be handled does not matter, keep the default values.

#### Request Examples 
```
{
  "version": "version-1",
  "language": "python3"
}
```
 
```
{
  "version": "version-1",
  "language": "python3",
  "memory_allocation": 512
}
```
 
```
{
  "version": "version-1",
  "language": "python3",
  "maximum_deployments": 4,
  "minimum_deployments": 1
}
```

### Response Structure 
Details of the created version
 - `id`: Unique identifier for the model (UUID)
 - `model`: Model name to which the version is associated
 - `version`: Version name
 - `language`: Language in which the model version is provided
 - `state`: The state of the version. It is set to initialised state on creation.
 - `memory_allocation`: The reserved memory for the version in mb  
 - `maximum_deployments`: Upper bound of number of model pods running in parallel 
 - `minimum_deployments`: Lower bound of number of model pods running in parallel
 - `unused_shutdown_time`: Maximum time in minutes a model pod stays active after a model request
 
#### Response Examples 
```
{
  "id": "4ae7d14b-4803-4e16-b96d-3b18caa4b605",
  "model": "model-1",
  "version": "version-1",
  "language": "python3.7",
  "state": "initialised",
  "memory_allocation": 2048,
  "maximum_deployments": 5,
  "minimum_deployments": 0,
  "unused_shutdown_time": 5,
}
```
 
```
{
  "id": "4ae7d14b-4803-4e16-b96d-3b18caa4b605",
  "model": "model-1",
  "version": "version-1",
  "language": "python3.7",
  "state": "initialised",
  "memory_allocation": 512,
  "maximum_deployments": 5,
  "minimum_deployments": 0,
  "unused_shutdown_time": 5,
}
```
 
```
{
  "id": "4ae7d14b-4803-4e16-b96d-3b18caa4b605",
  "model": "model-1",
  "version": "version-1",
  "language": "python3.7",
  "state": "initialised",
  "memory_allocation": 2048,
  "maximum_deployments": 4,
  "minimum_deployments": 1,
  "unused_shutdown_time": 5,
}
```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import xenia_python_client_library
from xenia_python_client_library.rest import ApiException
from pprint import pprint
configuration = xenia_python_client_library.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.dutchanalytics.net/v1.1
configuration.host = "https://api.dutchanalytics.net/v1.1"
# Create an instance of the API class
api_instance = xenia_python_client_library.CoreApi(xenia_python_client_library.ApiClient(configuration))
project_name = 'project_name_example' # str | 
model_name = 'model_name_example' # str | 
data = xenia_python_client_library.ModelVersionCreate() # ModelVersionCreate | 

try:
    # Create model versions
    api_response = api_instance.model_versions_create(project_name, model_name, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CoreApi->model_versions_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **model_name** | **str**|  | 
 **data** | [**ModelVersionCreate**](ModelVersionCreate.md)|  | 

### Return type

[**ModelVersionList**](ModelVersionList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **model_versions_delete**
> model_versions_delete(project_name, model_name, version)

Delete model version

 
### Description 
Delete a version. The state of the version is set to deactivated. If the model version is referenced from a pipeline, it cannot be deleted, it must be removed from the pipeline first.

If the model version has a model file uploaded, it is also deleted from the storage on deletion.


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import xenia_python_client_library
from xenia_python_client_library.rest import ApiException
from pprint import pprint
configuration = xenia_python_client_library.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.dutchanalytics.net/v1.1
configuration.host = "https://api.dutchanalytics.net/v1.1"
# Create an instance of the API class
api_instance = xenia_python_client_library.CoreApi(xenia_python_client_library.ApiClient(configuration))
project_name = 'project_name_example' # str | 
model_name = 'model_name_example' # str | 
version = 'version_example' # str | 

try:
    # Delete model version
    api_instance.model_versions_delete(project_name, model_name, version)
except ApiException as e:
    print("Exception when calling CoreApi->model_versions_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **model_name** | **str**|  | 
 **version** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **model_versions_file_download**
> ModelVersionFileUpload model_versions_file_download(project_name, model_name, version)

Download model files


### Description 
Download a model file for a specific version of a model

### Response Structure 
 - `file`: Model file of the version


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import xenia_python_client_library
from xenia_python_client_library.rest import ApiException
from pprint import pprint
configuration = xenia_python_client_library.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.dutchanalytics.net/v1.1
configuration.host = "https://api.dutchanalytics.net/v1.1"
# Create an instance of the API class
api_instance = xenia_python_client_library.CoreApi(xenia_python_client_library.ApiClient(configuration))
project_name = 'project_name_example' # str | 
model_name = 'model_name_example' # str | 
version = 'version_example' # str | 

try:
    # Download model files
    api_response = api_instance.model_versions_file_download(project_name, model_name, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CoreApi->model_versions_file_download: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **model_name** | **str**|  | 
 **version** | **str**|  | 

### Return type

[**ModelVersionFileUpload**](ModelVersionFileUpload.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **model_versions_file_upload**
> Success model_versions_file_upload(project_name, model_name, version, file)

Upload model files


### Description 
Upload a file for the version. This file should contain the model that will be run. It should be provided as a zip and a template can be found on https://github.com/DutchAnalytics/xenia-model-template. The file is saved under a model directory in the storage specified in the settings.

### Required Parameters
- `file`: Model file

### Response Structure
- `success`: Boolean indicating whether the model file upload succeeded or not. An exception is raised if the upload of the file fails and the error message is displayed instead.



### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import xenia_python_client_library
from xenia_python_client_library.rest import ApiException
from pprint import pprint
configuration = xenia_python_client_library.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.dutchanalytics.net/v1.1
configuration.host = "https://api.dutchanalytics.net/v1.1"
# Create an instance of the API class
api_instance = xenia_python_client_library.CoreApi(xenia_python_client_library.ApiClient(configuration))
project_name = 'project_name_example' # str | 
model_name = 'model_name_example' # str | 
version = 'version_example' # str | 
file = '/path/to/file' # file | 

try:
    # Upload model files
    api_response = api_instance.model_versions_file_upload(project_name, model_name, version, file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CoreApi->model_versions_file_upload: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **model_name** | **str**|  | 
 **version** | **str**|  | 
 **file** | **file**|  | 

### Return type

[**Success**](Success.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **model_versions_get**
> ModelVersionList model_versions_get(project_name, model_name, version)

Get model version


### Description 
Retrieve details of a model version of a model in a project

### Response Structure 
Details of a version
 - `id`: Unique identifier for the model (UUID)
 - `model`: Model name to which the version is associated
 - `version`: Version name
 - `language`: Language in which the model version is provided
 - `state`: The state of the version
 - `memory_allocation`: The reserved memory for the version in mb 
 - `maximum_deployments`: Upper bound of number of model pods running in parallel
 - `minimum_deployments`: Lower bound of number of model pods running in parallel
 - `unused_shutdown_time`: Maximum time in minutes a model pod stays active after a model request

#### Response Examples
```
{
  "id": "4ae7d14b-4803-4e16-b96d-3b18caa4b605",
  "model": "model-1",
  "version": "version-1",
  "memory_allocation": 512,
  "language": "python3.7",
  "state": "active",
  "maximum_deployments": 4,
  "minimum_deployments": 1,
  "unused_shutdown_time": 5,
}
```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import xenia_python_client_library
from xenia_python_client_library.rest import ApiException
from pprint import pprint
configuration = xenia_python_client_library.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.dutchanalytics.net/v1.1
configuration.host = "https://api.dutchanalytics.net/v1.1"
# Create an instance of the API class
api_instance = xenia_python_client_library.CoreApi(xenia_python_client_library.ApiClient(configuration))
project_name = 'project_name_example' # str | 
model_name = 'model_name_example' # str | 
version = 'version_example' # str | 

try:
    # Get model version
    api_response = api_instance.model_versions_get(project_name, model_name, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CoreApi->model_versions_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **model_name** | **str**|  | 
 **version** | **str**|  | 

### Return type

[**ModelVersionList**](ModelVersionList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **model_versions_list**
> list[ModelVersionList] model_versions_list(project_name, model_name)

List model versions


### Description 
List all the model versions of a model in a project

### Response Structure 
A list of details of the versions
 - `id`: Unique identifier for the model (UUID)
 - `model`: Model name to which the version is associated
 - `version`: Version name
 - `language`: Language in which the model version is provided
 - `state`: The state of the version
 - `memory_allocation`: The reserved memory usage for the version
 - `maximum_deployments`: Upper bound of number of models running in parallel. 
 - `minimum_deployments`: Lower bound of number of versions running
 - `unused_shutdown_time`: Maximum time a version can stay unused before it is stopped in minutes.

#### Response Examples
```
[
  {
    "id": "4ae7d14b-4803-4e16-b96d-3b18caa4b605",
    "model": "model-1",
    "version": "version-1",
    "language": "python3.5",
    "state": "active",
    "memory_allocation": 512,
    "maximum_deployments": 4,
    "minimum_deployments": 1,
    "unused_shutdown_time": 5,
  },
  {
    "id": "24f6b80a-08c3-4d52-ac1a-2ea7e70f16a6",
    "model": "model-1",
    "version": "version-2",
    "language": "python3.6",
    "state": "initialised",
    "memory_allocation": 256,
    "maximum_deployments": 5,
    "minimum_deployments": 0,
    "unused_shutdown_time": 5,
  }
]
```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import xenia_python_client_library
from xenia_python_client_library.rest import ApiException
from pprint import pprint
configuration = xenia_python_client_library.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.dutchanalytics.net/v1.1
configuration.host = "https://api.dutchanalytics.net/v1.1"
# Create an instance of the API class
api_instance = xenia_python_client_library.CoreApi(xenia_python_client_library.ApiClient(configuration))
project_name = 'project_name_example' # str | 
model_name = 'model_name_example' # str | 

try:
    # List model versions
    api_response = api_instance.model_versions_list(project_name, model_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CoreApi->model_versions_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **model_name** | **str**|  | 

### Return type

[**list[ModelVersionList]**](ModelVersionList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **model_versions_update**
> ModelVersionList model_versions_update(project_name, model_name, version, data)

Update model version


### Description 
Update a model version of a model in a project. It is not possible to update the language field. All necessary fields are validated again.

### Optional Parameters 
 - `version`: New name for the version
 - `memory_allocation`: New reserved memory for the version in mb  
 - `maximum_deployments`: New upper bound of number of model pods running in parallel 
 - `minimum_deployments`: New lower bound of number of model pods running in parallel
 - `unused_shutdown_time`: New maximum time in minutes a model pod stays active after a model request

#### Request Examples 
```
{
  "version": "new-version"
}
```
 
```
{
  "memory_allocation": 512
}
```
 
```
{
  "maximum_deployments": 4,
  "minimum_deployments": 1
}
```

### Response Structure 
Details of the updated version
 - `id`: Unique identifier for the model (UUID)
 - `model`: Model name to which the version is associated
 - `version`: Version name
 - `language`: Language in which the model version is provided
 - `state`: The state of the version
 - `memory_allocation`: The reserved memory for the version in mb  
 - `maximum_deployments`: Upper bound of number of model pods running in parallel 
 - `minimum_deployments`: Lower bound of number of model pods running in parallel
 - `unused_shutdown_time`: Maximum time in minutes a model pod stays active after a model request

#### Response Examples 
```
{
  "id": "4ae7d14b-4803-4e16-b96d-3b18caa4b605",
  "model": "model-1",
  "version": "new-version",
  "language": "python3.5",
  "state": "initialised",
  "memory_allocation": 2048,
  "maximum_deployments": 5,
  "minimum_deployments": 0,
  "unused_shutdown_time": 5,
}
```
 
```
{
  "id": "4ae7d14b-4803-4e16-b96d-3b18caa4b605",
  "model": "model-1",
  "version": "version-1",
  "language": "python3.5",
  "state": "initialised",
  "memory_allocation": 512,
  "maximum_deployments": 5,
  "minimum_deployments": 0,
  "unused_shutdown_time": 5,
}
```
 
```
{
  "id": "4ae7d14b-4803-4e16-b96d-3b18caa4b605",
  "model": "model-1",
  "version": "version-1",
  "language": "python3.5",
  "state": "initialised",
  "memory_allocation": 2048,
  "maximum_deployments": 4,
  "minimum_deployments": 1,
  "unused_shutdown_time": 5,
}
```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import xenia_python_client_library
from xenia_python_client_library.rest import ApiException
from pprint import pprint
configuration = xenia_python_client_library.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.dutchanalytics.net/v1.1
configuration.host = "https://api.dutchanalytics.net/v1.1"
# Create an instance of the API class
api_instance = xenia_python_client_library.CoreApi(xenia_python_client_library.ApiClient(configuration))
project_name = 'project_name_example' # str | 
model_name = 'model_name_example' # str | 
version = 'version_example' # str | 
data = xenia_python_client_library.ModelVersionCreate() # ModelVersionCreate | 

try:
    # Update model version
    api_response = api_instance.model_versions_update(project_name, model_name, version, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CoreApi->model_versions_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **model_name** | **str**|  | 
 **version** | **str**|  | 
 **data** | [**ModelVersionCreate**](ModelVersionCreate.md)|  | 

### Return type

[**ModelVersionList**](ModelVersionList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **models_create**
> ModelList models_create(project_name, data)

Create a model


### Description 
Create a model by defining the input/output type and input/output fields. In case of blob type of input or output, input and output fields should not be given or passed as an empty list. Possible data types for the input and output fields are:
 - 'int' =  integers
 - 'string' = string
 - 'double' = double precision floating point
 - 'bool' = boolean value (False/True)
 - 'timestamp' = timestamp 
 - 'array_int' = an array of integers
 - 'array_double' = an array of double precision floating points
 - 'array_string' = an array of strings
 
### Required Parameters 
 - `name`: Name of the model. It is unique within a project.
 - `input_type`: Type of the input of the model. It can be either structured or blob.
 - `output_type`: Type of the output of the model. It can be either structured or blob.
 - `input_fields`: The list of required model input fields. It must contain the fields: name and data_type. The name of an input field is unique for a model.
 - `output_fields`: The list of required model output fields. It must contain the fields: name and data_type. The name of an output field is unique for a model.

#### Request Examples
A model with structured input and output type

```
{
  "name": "model-1",
  "input_type": "structured",
  "output_type": "structured",
  "input_fields": [
    {
      "name": "input-field-1",
      "data_type": "int"
    },
    {
      "name": "input-field-2",
      "data_type": "double"
    }
  ],
  "output_fields": [
    {
      "name": "output-field",
      "data_type": "double"
    }
  ]
}
```
 
 A model with blob input type

```
{
  "name": "model-1",
  "input_type": "blob",
  "output_type": "structured",
  "input_fields": [],
  "output_fields": [
    {
      "name": "output-field",
      "data_type": "double"
    }
  ]
}
```

```
{
  "name": "model-1",
  "input_type": "blob",
  "output_type": "structured",
  "output_fields": [
    {
      "name": "output-field",
      "data_type": "double"
    }
  ]
}
```
 
 A model with blob input and output type

```
{
  "name": "model-1",
  "input_type": "blob",
  "output_type": "blob",
  "input_fields": [],
  "output_fields": []
}
```

```
{
  "name": "model-1",
  "input_type": "blob",
  "output_type": "blob"
}
```

### Response Structure 
Details of the created model
 - `id`: Unique identifier for the model (UUID)
 - `name`: Name of the model
 - `project`: Project name in which the model is created
 - `input_type`: Type of the input of the model
 - `output_type`: Type of the output of the model
 - `input_fields`: The list of model input fields containing name and data_type
 - `output_fields`: The list of model output fields containing name and data_type

#### Response Examples
```
{
  "id": "903ccd12-81d1-46e1-9ac9-b9d70af118de",
  "name": "model-1",
  "project": "project-1",
  "input_type": "structured",
  "output_type": "structured",
  "input_fields": [
    {
      "name": "input-field-1",
      "data_type": "int"
    },
    {
      "name": "input-field-2",
      "data_type": "double"
    }
  ],
  "output_fields": [
    {
      "name": "output-field",
      "data_type": "double"
    }
  ]
}
```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import xenia_python_client_library
from xenia_python_client_library.rest import ApiException
from pprint import pprint
configuration = xenia_python_client_library.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.dutchanalytics.net/v1.1
configuration.host = "https://api.dutchanalytics.net/v1.1"
# Create an instance of the API class
api_instance = xenia_python_client_library.CoreApi(xenia_python_client_library.ApiClient(configuration))
project_name = 'project_name_example' # str | 
data = xenia_python_client_library.ModelCreate() # ModelCreate | 

try:
    # Create a model
    api_response = api_instance.models_create(project_name, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CoreApi->models_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **data** | [**ModelCreate**](ModelCreate.md)|  | 

### Return type

[**ModelList**](ModelList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **models_delete**
> models_delete(project_name, model_name)

Delete a model


### Description 
Delete a model. The state of the model and all its versions is set to inactive. If any of the model versions of the model are referenced in a pipeline, the model cannot be deleted.

After deletion, a model with the same name as the deleted model can be created with the same or different input/output type and fields.

### Required Parameters 
- None


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import xenia_python_client_library
from xenia_python_client_library.rest import ApiException
from pprint import pprint
configuration = xenia_python_client_library.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.dutchanalytics.net/v1.1
configuration.host = "https://api.dutchanalytics.net/v1.1"
# Create an instance of the API class
api_instance = xenia_python_client_library.CoreApi(xenia_python_client_library.ApiClient(configuration))
project_name = 'project_name_example' # str | 
model_name = 'model_name_example' # str | 

try:
    # Delete a model
    api_instance.models_delete(project_name, model_name)
except ApiException as e:
    print("Exception when calling CoreApi->models_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **model_name** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **models_get**
> ModelList models_get(project_name, model_name)

Get details of model


### Description 
Retrieve details of a single model in a project

### Required Parameters 
- None

### Response Structure 
Details of a model
 - `id`: Unique identifier for the model (UUID)
 - `name`: Name of the model
 - `project`: Project name in which the model is
 - `input_type`: Type of the input of the model
 - `output_type`: Type of the output of the model
 - `input_fields`: The list of model input fields containing name and data_type
 - `output_fields`: The list of model output fields containing name and data_type

#### Response Examples
```
{
  "id": "903ccd12-81d1-46e1-9ac9-b9d70af118de",
  "name": "model-1",
  "project": "project-1",
  "input_type": "structured",
  "output_type": "structured",
  "input_fields": [
    {
      "name": "input-field-1",
      "data_type": "int"
    },
    {
      "name": "input-field-2",
      "data_type": "double"
    }
  ],
  "output_fields": [
    {
      "name": "output-field",
      "data_type": "double"
    }
  ]
}
```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import xenia_python_client_library
from xenia_python_client_library.rest import ApiException
from pprint import pprint
configuration = xenia_python_client_library.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.dutchanalytics.net/v1.1
configuration.host = "https://api.dutchanalytics.net/v1.1"
# Create an instance of the API class
api_instance = xenia_python_client_library.CoreApi(xenia_python_client_library.ApiClient(configuration))
project_name = 'project_name_example' # str | 
model_name = 'model_name_example' # str | 

try:
    # Get details of model
    api_response = api_instance.models_get(project_name, model_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CoreApi->models_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **model_name** | **str**|  | 

### Return type

[**ModelList**](ModelList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **models_list**
> list[ModelList] models_list(project_name)

List models in project


### Description 
List all models and their details in a project

### Required Parameters 
- None

### Response Structure 
A list of details of the models in the project
 - `id`: Unique identifier for the model (UUID)
 - `name`: Name of the model
 - `project`: Project name in which the model is
 - `input_type`: Type of the input of the model
 - `output_type`: Type of the output of the model
 - `input_fields`: The list of model input fields containing name and data_type
 - `output_fields`: The list of model output fields containing name and data_type

#### Response Examples
```
[
  {
    "id": "903ccd12-81d1-46e1-9ac9-b9d70af118de",
    "name": "model-1",
    "project": "project-1",
    "input_type": "structured",
    "output_type": "structured",
    "input_fields": [
      {
        "name": "input-field-1",
        "data_type": "int"
      },
      {
        "name": "input-field-2",
        "data_type": "double"
      }
    ],
    "output_fields": [
      {
        "name": "output-field",
        "data_type": "double"
      }
    ]
  },
  {
    "id": "5f4e942f-d5b8-4d62-99b2-870c15a82127",
    "name": "model-2",
    "project": "project-1",
    "input_type": "structured",
    "output_type": "blob",
    "input_fields": [
      {
        "name": "input-field",
        "data_type": "int"
      }
    ],
    "output_fields": []
  },
  {
    "id": "bd3fae9d-aeec-4cf3-8ef0-5f9224d41904",
    "name": "model-2",
    "project": "project-1",
    "input_type": "blob",
    "output_type": "blob",
    "input_fields": [],
    "output_fields": []
  }
]
```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import xenia_python_client_library
from xenia_python_client_library.rest import ApiException
from pprint import pprint
configuration = xenia_python_client_library.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.dutchanalytics.net/v1.1
configuration.host = "https://api.dutchanalytics.net/v1.1"
# Create an instance of the API class
api_instance = xenia_python_client_library.CoreApi(xenia_python_client_library.ApiClient(configuration))
project_name = 'project_name_example' # str | 

try:
    # List models in project
    api_response = api_instance.models_list(project_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CoreApi->models_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 

### Return type

[**list[ModelList]**](ModelList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **models_update**
> ModelList models_update(project_name, model_name, data)

Update a model


### Description 
Update a model. It is only possible to update the name field. All necessary fields are validated again.

### Optional Parameters 
 - `name`: New name for the model

#### Request Examples
```
{
  "name": "new-model-name"
}
```

### Response Structure 
Details of the updated model
 - `id`: Unique identifier for the model (UUID)
 - `name`: Name of the model
 - `project`: Project name in which the model is
 - `input_type`: Type of the input of the model
 - `output_type`: Type of the output of the model
 - `input_fields`: The list of model input fields containing name and data_type
 - `output_fields`: The list of model output fields containing name and data_type

#### Response Examples
```
{
  "id": "903ccd12-81d1-46e1-9ac9-b9d70af118de",
  "name": "new-model-name",
  "project": "project-1",
  "input_type": "structured",
  "output_type": "structured",
  "input_fields": [
    {
      "name": "input-field-1",
      "data_type": "int"
    },
    {
      "name": "input-field-2",
      "data_type": "double"
    }
  ],
  "output_fields": [
    {
      "name": "output-field",
      "data_type": "double"
    }
  ]
}
```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import xenia_python_client_library
from xenia_python_client_library.rest import ApiException
from pprint import pprint
configuration = xenia_python_client_library.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.dutchanalytics.net/v1.1
configuration.host = "https://api.dutchanalytics.net/v1.1"
# Create an instance of the API class
api_instance = xenia_python_client_library.CoreApi(xenia_python_client_library.ApiClient(configuration))
project_name = 'project_name_example' # str | 
model_name = 'model_name_example' # str | 
data = xenia_python_client_library.ModelUpdate() # ModelUpdate | 

try:
    # Update a model
    api_response = api_instance.models_update(project_name, model_name, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CoreApi->models_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **model_name** | **str**|  | 
 **data** | [**ModelUpdate**](ModelUpdate.md)|  | 

### Return type

[**ModelList**](ModelList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organization_invites_delete**
> organization_invites_delete(invite_id, organization_name)

Delete an organization invitation of a user


### Description 
Delete the organization invitation of a user. The user making the request must be admin of the organization.


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import xenia_python_client_library
from xenia_python_client_library.rest import ApiException
from pprint import pprint
configuration = xenia_python_client_library.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.dutchanalytics.net/v1.1
configuration.host = "https://api.dutchanalytics.net/v1.1"
# Create an instance of the API class
api_instance = xenia_python_client_library.CoreApi(xenia_python_client_library.ApiClient(configuration))
invite_id = 'invite_id_example' # str | 
organization_name = 'organization_name_example' # str | 

try:
    # Delete an organization invitation of a user
    api_instance.organization_invites_delete(invite_id, organization_name)
except ApiException as e:
    print("Exception when calling CoreApi->organization_invites_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invite_id** | **str**|  | 
 **organization_name** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organization_invites_get**
> OrganizationUserInviteList organization_invites_get(invite_id, organization_name)

Get details of an organization invitation of a user


### Description 
Get the details of an organization invitation of a user in an organization. The user making the request must be admin of the organization.

### Response Structure 
Details of the invited user
 - `id`: Unique identifier for the user invitation (UUID) 

 - `email`: Email of the invited user 

- `admin`: Boolean value indicating whether the user is added as an admin of the organization or not 

 - `invitation_creation_time`: Date when the user is invited to the organization 


#### Response Examples 
```
{
  "id": "42879106-fb95-42d5-931a-8b94c85ba41e",
  "email": "user@example.com",
  "admin": false
  "invitation_creation_time": "2020-04-15 12:04:34.213309+02"
}
```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import xenia_python_client_library
from xenia_python_client_library.rest import ApiException
from pprint import pprint
configuration = xenia_python_client_library.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.dutchanalytics.net/v1.1
configuration.host = "https://api.dutchanalytics.net/v1.1"
# Create an instance of the API class
api_instance = xenia_python_client_library.CoreApi(xenia_python_client_library.ApiClient(configuration))
invite_id = 'invite_id_example' # str | 
organization_name = 'organization_name_example' # str | 

try:
    # Get details of an organization invitation of a user
    api_response = api_instance.organization_invites_get(invite_id, organization_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CoreApi->organization_invites_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invite_id** | **str**|  | 
 **organization_name** | **str**|  | 

### Return type

[**OrganizationUserInviteList**](OrganizationUserInviteList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organization_invites_list**
> list[OrganizationUserInviteList] organization_invites_list(organization_name)

List the users invited to an organization


### Description 
List pending user invitations for an organization. The user making the request must be admin of the organization.

### Response Structure 
List of details of invited users
 - `id`: Unique identifier for the user invitation (UUID) 

 - `email`: Email of the invited user 

 - `admin`: Boolean value indicating whether the user is added as an admin of the organization or not 

 - `invitation_creation_time`: Date when the user is invited to the organization 


#### Response Examples
```
[
  {
    "id": "42879106-fb95-42d5-931a-8b94c85ba41e",
    "email": "user@example.com",
    "admin": true,
    "invitation_creation_time": "2020-04-15 12:04:34.213309+02"
  },
  {
    "id": "90f09c91-789b-4dda-a0c2-18954ac49fcf",
    "email": "user@example.com",
    "admin": false
    "invitation_creation_time": "2020-04-15 12:04:34.213309+02"
  }
]
```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import xenia_python_client_library
from xenia_python_client_library.rest import ApiException
from pprint import pprint
configuration = xenia_python_client_library.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.dutchanalytics.net/v1.1
configuration.host = "https://api.dutchanalytics.net/v1.1"
# Create an instance of the API class
api_instance = xenia_python_client_library.CoreApi(xenia_python_client_library.ApiClient(configuration))
organization_name = 'organization_name_example' # str | 

try:
    # List the users invited to an organization
    api_response = api_instance.organization_invites_list(organization_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CoreApi->organization_invites_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_name** | **str**|  | 

### Return type

[**list[OrganizationUserInviteList]**](OrganizationUserInviteList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organization_users_create**
> OrganizationUserDetail organization_users_create(organization_name, data)

Add a user to an organization


### Description
Add a user to an organization as admin or normal user. The user making the request must be admin of the organization.
The user can later be assigned roles in the projects defined in the scope the organization, such as project-admin, project-viewer etc.

### Required Parameters
- `email`: Email of the user 

- `admin`: Boolean value indicating whether the user is added as an admin of the organization or not 


#### Request Examples 
```
{
  "email": "test@example.com",
  "admin": false
}
```

### Response Structure 
Details of the added user
 - `id`: Unique identifier for the user (UUID) 

 - `email`: Email of the user 

 - `name`: Name of the user 

 - `surname`: Surname of the user 

 - `admin`: Boolean value indicating whether the user is an admin of the organization or not 


#### Response Examples 
```
{
  "id": "332d7432-2742-4177-99a9-139e91e0110c",
  "email": "test@example.com",
  "name": "user",
  "surname": "name",
  "admin": false
}
```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import xenia_python_client_library
from xenia_python_client_library.rest import ApiException
from pprint import pprint
configuration = xenia_python_client_library.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.dutchanalytics.net/v1.1
configuration.host = "https://api.dutchanalytics.net/v1.1"
# Create an instance of the API class
api_instance = xenia_python_client_library.CoreApi(xenia_python_client_library.ApiClient(configuration))
organization_name = 'organization_name_example' # str | 
data = xenia_python_client_library.OrganizationUserCreate() # OrganizationUserCreate | 

try:
    # Add a user to an organization
    api_response = api_instance.organization_users_create(organization_name, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CoreApi->organization_users_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_name** | **str**|  | 
 **data** | [**OrganizationUserCreate**](OrganizationUserCreate.md)|  | 

### Return type

[**OrganizationUserDetail**](OrganizationUserDetail.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organization_users_delete**
> organization_users_delete(organization_name, user_id)

Delete a user from an organization


### Description 
Delete a user from an organization. The user making the request must be admin of the organization.
It is not possible to delete the last admin of an organization.

**When a user is deleted from an organization, all his roles from all projects defined in the scope of the organization are also deleted.**


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import xenia_python_client_library
from xenia_python_client_library.rest import ApiException
from pprint import pprint
configuration = xenia_python_client_library.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.dutchanalytics.net/v1.1
configuration.host = "https://api.dutchanalytics.net/v1.1"
# Create an instance of the API class
api_instance = xenia_python_client_library.CoreApi(xenia_python_client_library.ApiClient(configuration))
organization_name = 'organization_name_example' # str | 
user_id = 'user_id_example' # str | 

try:
    # Delete a user from an organization
    api_instance.organization_users_delete(organization_name, user_id)
except ApiException as e:
    print("Exception when calling CoreApi->organization_users_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_name** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organization_users_get**
> OrganizationUserDetail organization_users_get(organization_name, user_id)

Get details of a user in an organization


### Description 
Get the details of a user in an organization. The user making the request must be admin of the organization.

### Response Structure 
Details of the user
 - `id`: Unique identifier for the user (UUID) 

 - `email`: Email of the user 

 - `name`: Name of the user 

 - `surname`: Surname of the user 

 - `admin`: Boolean value indicating whether the user is an admin of the organization or not 


#### Response Examples 
```
{
  "id": "332d7432-2742-4177-99a9-139e91e0110c",
  "email": "test@example.com",
  "name": "user",
  "surname": "name",
  "admin": false
}
```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import xenia_python_client_library
from xenia_python_client_library.rest import ApiException
from pprint import pprint
configuration = xenia_python_client_library.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.dutchanalytics.net/v1.1
configuration.host = "https://api.dutchanalytics.net/v1.1"
# Create an instance of the API class
api_instance = xenia_python_client_library.CoreApi(xenia_python_client_library.ApiClient(configuration))
organization_name = 'organization_name_example' # str | 
user_id = 'user_id_example' # str | 

try:
    # Get details of a user in an organization
    api_response = api_instance.organization_users_get(organization_name, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CoreApi->organization_users_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_name** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**OrganizationUserDetail**](OrganizationUserDetail.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organization_users_list**
> list[OrganizationUserDetail] organization_users_list(organization_name)

List the users in an organization


### Description 
List users and their details in an organization. The user making the request must be admin of the organization.

### Response Structure 
List of details of users
 - `id`: Unique identifier for the user (UUID) 

 - `email`: Email of the user 

 - `name`: Name of the user 

 - `surname`: Surname of the user 

 - `admin`: Boolean value indicating whether the user is an admin of the organization or not 


#### Response Examples
```
[
  {
    "id": "54977bc3-2c3b-4d8f-97c7-aff89a95bf21",
    "email": "user@example.com",
    "name": "user",
    "surname": "name",
    "admin": true
  },
  {
    "id": "abe2e406-fae5-4bcf-a3bc-956d756e4ecb",
    "email": "user2@example.com",
    "name": "user",
    "surname": "name",
    "admin": false
  }
]
```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import xenia_python_client_library
from xenia_python_client_library.rest import ApiException
from pprint import pprint
configuration = xenia_python_client_library.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.dutchanalytics.net/v1.1
configuration.host = "https://api.dutchanalytics.net/v1.1"
# Create an instance of the API class
api_instance = xenia_python_client_library.CoreApi(xenia_python_client_library.ApiClient(configuration))
organization_name = 'organization_name_example' # str | 

try:
    # List the users in an organization
    api_response = api_instance.organization_users_list(organization_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CoreApi->organization_users_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_name** | **str**|  | 

### Return type

[**list[OrganizationUserDetail]**](OrganizationUserDetail.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organization_users_update**
> OrganizationUserDetail organization_users_update(organization_name, user_id, data)

Update details of a user in an organization


### Description 
Update the admin status of a user in an organization. The user making the request must be admin of the organization.
It is not possible to change the last admin of an organization to a regular user.

### Required Parameters
- `admin`: Boolean value indicating whether the user is added as an admin of the organization or not 


#### Request Examples 
```
{
  "admin": true
}
```

### Response Structure
Details of the user
 - `id`: Unique identifier for the user (UUID) 

 - `email`: Email of the user 

 - `name`: Name of the user 

 - `surname`: Surname of the user 

 - `admin`: Boolean value indicating whether the user is an admin of the organization or not 


#### Response Examples 
```
{
  "id": "332d7432-2742-4177-99a9-139e91e0110c",
  "email": "test@example.com",
  "name": "user",
  "surname": "name",
  "admin": true
}
```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import xenia_python_client_library
from xenia_python_client_library.rest import ApiException
from pprint import pprint
configuration = xenia_python_client_library.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.dutchanalytics.net/v1.1
configuration.host = "https://api.dutchanalytics.net/v1.1"
# Create an instance of the API class
api_instance = xenia_python_client_library.CoreApi(xenia_python_client_library.ApiClient(configuration))
organization_name = 'organization_name_example' # str | 
user_id = 'user_id_example' # str | 
data = xenia_python_client_library.OrganizationUserUpdate() # OrganizationUserUpdate | 

try:
    # Update details of a user in an organization
    api_response = api_instance.organization_users_update(organization_name, user_id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CoreApi->organization_users_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_name** | **str**|  | 
 **user_id** | **str**|  | 
 **data** | [**OrganizationUserUpdate**](OrganizationUserUpdate.md)|  | 

### Return type

[**OrganizationUserDetail**](OrganizationUserDetail.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organizations_create**
> OrganizationList organizations_create(data)

Create organizations


### Description 
Create a new organization with the provided name.
Any authenticated user can create a new organization and this user will automatically become organization admin.
Upon creating an organization, a **subscription** needs to be given. A license for this subscription should be purchased via dutchanalytics.com. 
- A **free_trial** subscription grants permission to one user and allows for a maximum of 2 projects to be created. 
- A **starter** subscription grants permission to 5 users and allows for a maximum of 10 projects to be created. 
- A **professional** subscription grants permission to an unlimited number of users and allows unlimited projects.

It is **mandatory** to agree with the Xenia Free SaaS Services Agreement and the Xenia SaaS Terms & Conditions to be able to create an organization.

### Required Parameters 
 - `name`: Name of the organization. The name is globally unique. It can only consist of lowercase letters, numbers and dashes (-), and must start with a lowercase letter. 

 - `subscription`: Name of the subscription: 'free_trial', 'starter' or 'professional'.
 - `subscription_agreed`: A boolean field indicating whether the Services Agreement and Terms & Conditions are accepted
 
#### Request Examples 
```
{
  "name": "test-organization",
  "subscription": "professional",
  "subscription_agreed": true
}
```

### Response Structure 
Details of the created organization
 - `id`: Unique identifier for the organization (UUID) 

 - `name`: Name of the organization 

 - `creation_date`: Date and time the organization was created 


#### Response Examples 
```
{
  "id": "abe2e406-fae5-4bcf-a3bc-956d756e4ecb",
  "name": "test-organization",
  "creation_date": "2020-03-25T15:43:46.101877Z"
}
```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import xenia_python_client_library
from xenia_python_client_library.rest import ApiException
from pprint import pprint
configuration = xenia_python_client_library.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.dutchanalytics.net/v1.1
configuration.host = "https://api.dutchanalytics.net/v1.1"
# Create an instance of the API class
api_instance = xenia_python_client_library.CoreApi(xenia_python_client_library.ApiClient(configuration))
data = xenia_python_client_library.OrganizationCreate() # OrganizationCreate | 

try:
    # Create organizations
    api_response = api_instance.organizations_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CoreApi->organizations_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**OrganizationCreate**](OrganizationCreate.md)|  | 

### Return type

[**OrganizationList**](OrganizationList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organizations_get**
> OrganizationDetail organizations_get(organization_name)

Get details of an organization


### Description 
Get the details of an organization. The user making the request must be admin of the organization.

### Response Structure 
Details of a organization
 - `id`: Unique identifier for the organization (UUID) 

 - `name`: Name of the organization 

 - `creation_date`: Time the organization was created 

 - `subscription`: Type of subscription 

 - `subscription_agreement_date`: Time the subscription agreement was accepted 

 - `subscription_agreement_user`: User who accepted the subscription agreement 


#### Response Examples 
```
{
  "id": "abe2e406-fae5-4bcf-a3bc-956d756e4ecb",
  "name": "test-organization",
  "creation_date": "2020-03-25T15:43:46.101877Z",
  "subscription": "professional",
  "subscription_agreement_date": "2020-03-25T15:43:46.101877Z",
  "subscription_agreement_user": "test-user@test.com"
}
```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import xenia_python_client_library
from xenia_python_client_library.rest import ApiException
from pprint import pprint
configuration = xenia_python_client_library.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.dutchanalytics.net/v1.1
configuration.host = "https://api.dutchanalytics.net/v1.1"
# Create an instance of the API class
api_instance = xenia_python_client_library.CoreApi(xenia_python_client_library.ApiClient(configuration))
organization_name = 'organization_name_example' # str | 

try:
    # Get details of an organization
    api_response = api_instance.organizations_get(organization_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CoreApi->organizations_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_name** | **str**|  | 

### Return type

[**OrganizationDetail**](OrganizationDetail.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organizations_list**
> list[OrganizationList] organizations_list()

List organizations


### Description 
List all organizations to which the user making the request belongs to.

### Response Structure
A list of details of the organizations
 - `id`: Unique identifier for the organization (UUID) 

 - `name`: Name of the organization 

 - `creation_date`: Date and time the organization was created 


#### Response Examples
```
[
  {
    "id": "45a1f903-4146-4f15-be4a-302455cd6f7e",
    "name": "organization-name",
    "creation_date": "2020-03-23T11:47:15.436240Z"
  }
]
```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import xenia_python_client_library
from xenia_python_client_library.rest import ApiException
from pprint import pprint
configuration = xenia_python_client_library.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.dutchanalytics.net/v1.1
configuration.host = "https://api.dutchanalytics.net/v1.1"
# Create an instance of the API class
api_instance = xenia_python_client_library.CoreApi(xenia_python_client_library.ApiClient(configuration))

try:
    # List organizations
    api_response = api_instance.organizations_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CoreApi->organizations_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[OrganizationList]**](OrganizationList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organizations_update**
> OrganizationDetail organizations_update(organization_name, data)

Update details of an organization


### Description 
Update an organization. The user making the request must be admin of the organization.

It is **mandatory** to agree with the Xenia Free SaaS Services Agreement and the Xenia SaaS Terms & Conditions to be able to upgrade the subscription of an organization.

### Optional Parameters 
 - `subscription`: New subscription
 - `subscription_agreed`: A boolean field indicating whether the Services Agreement and Terms & Conditions are accepted upon upgrading the subscriptions

#### Request Examples
```
{
  "subscription": "professional",
  "subscription_agreed": true
}
```

### Response Structure 
Details of a organization
 - `id`: Unique identifier for the organization (UUID) 

 - `name`: Name of the organization 

 - `creation_date`: Time the organization was created 

 - `subscription`: Type of subscription 

 - `subscription_agreement_date`: Time the subscription agreement was accepted 

 - `subscription_agreement_user`: User who accepted the subscription agreement 


#### Response Examples
```
{
  "id": "abe2e406-fae5-4bcf-a3bc-956d756e4ecb",
  "name": "test-organization",
  "creation_date": "2020-03-25T15:43:46.101877Z",
  "subscription": "professional",
  "subscription_agreement_date": "2020-04-25T12:26:18.976481Z",
  "subscription_agreement_user": "test-user-2@test.com"
}
```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import xenia_python_client_library
from xenia_python_client_library.rest import ApiException
from pprint import pprint
configuration = xenia_python_client_library.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.dutchanalytics.net/v1.1
configuration.host = "https://api.dutchanalytics.net/v1.1"
# Create an instance of the API class
api_instance = xenia_python_client_library.CoreApi(xenia_python_client_library.ApiClient(configuration))
organization_name = 'organization_name_example' # str | 
data = xenia_python_client_library.OrganizationUpdate() # OrganizationUpdate | 

try:
    # Update details of an organization
    api_response = api_instance.organizations_update(organization_name, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CoreApi->organizations_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_name** | **str**|  | 
 **data** | [**OrganizationUpdate**](OrganizationUpdate.md)|  | 

### Return type

[**OrganizationDetail**](OrganizationDetail.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **permissions_list**
> list[PermissionList] permissions_list()

List the available permissions


### Description 
List all the available permissions which can be used to create custom roles.

### Response Structure 
A list of available permissions
 - `name`: Name of the permission 



### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import xenia_python_client_library
from xenia_python_client_library.rest import ApiException
from pprint import pprint
configuration = xenia_python_client_library.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.dutchanalytics.net/v1.1
configuration.host = "https://api.dutchanalytics.net/v1.1"
# Create an instance of the API class
api_instance = xenia_python_client_library.CoreApi(xenia_python_client_library.ApiClient(configuration))

try:
    # List the available permissions
    api_response = api_instance.permissions_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CoreApi->permissions_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[PermissionList]**](PermissionList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pipeline_insert_retrieve**
> list[PipelineResultList] pipeline_insert_retrieve(project_name, pipeline_name, trace_id)

Retrieve pipeline insert results


### Description 
Retrieve the status, error message and result of a pipeline request using its trace id. All users with permission to the project are able to collect the pipeline request result, not just the user that created the request.

### Response Structure 
List of details of all model requests (success, failed and pending)
 - `model_name`: Name of model the request has been made to
 - `model_version`: Version of model the request has been made to
 - `request_id`: Unique identifier for the model request, to be used when collecting the result
 - `time_created`: Server time that the request was made 
 - `time_last_updated`: Server time that the request was last updated 
 - `status`: Status of the request. Always pending when initialised, later it can be success or failed.
 - `result`: Model request result value. NULL if not (yet) available or if the request failed.
 - `error_message`: An error message explaining why the request has failed. NULL if the request was successful.
 - `prediction_duration`: Time (in seconds) it took the model to predict. 0 if request is still pending or has failed.

#### Response Examples 
```
[
    {
      "request_id": "b91857ac-f48c-49a0-a26c-36f07df43a56",
      "model_name": "test-model",
      "model_version": "v1",
      "time_created": "2019-02-22T09:19:51.919276Z",
      "time_last_updated": "2019-02-22T09:19:52.532876Z",
      "status": "success",
      "result": "2.1369",
      "error_message": null
      "prediction_duration": 22.51
    },
    {
      "request_id": "d0d95961-9318-4757-b70a-5cfbd2ef2828",
      "model_name": "test-model",
      "model_version": "v1",
      "time_created": "2019-02-22T09:19:51.919276Z",
      "time_last_updated": "2019-02-22T09:19:52.532876Z",
      "status": "failed",
      "result": null,
      "error_message": "Data validation error for field int: Cannot cast 'result' to an integer",
      "prediction_duration": 22.51
    }
]
```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import xenia_python_client_library
from xenia_python_client_library.rest import ApiException
from pprint import pprint
configuration = xenia_python_client_library.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.dutchanalytics.net/v1.1
configuration.host = "https://api.dutchanalytics.net/v1.1"
# Create an instance of the API class
api_instance = xenia_python_client_library.CoreApi(xenia_python_client_library.ApiClient(configuration))
project_name = 'project_name_example' # str | 
pipeline_name = 'pipeline_name_example' # str | 
trace_id = 'trace_id_example' # str | 

try:
    # Retrieve pipeline insert results
    api_response = api_instance.pipeline_insert_retrieve(project_name, pipeline_name, trace_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CoreApi->pipeline_insert_retrieve: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **pipeline_name** | **str**|  | 
 **trace_id** | **str**|  | 

### Return type

[**list[PipelineResultList]**](PipelineResultList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pipeline_insert_retrieve_pending**
> list[PipelineResultList] pipeline_insert_retrieve_pending(project_name, pipeline_name)

Retrieve pending pipeline requests


### Description 
Retrieve a list of all pending pipeline requests. All users with permission to the project are able to collect the pipeline pending requests, not just the user that created the request.

### Response Structure 
List of details of all pending model requests in the pipeline
 - `request_id`: Unique identifier for the model request, to be used when collecting the result
 - `model_name`: Name of model the request has been made to
 - `model_version`: Version of model the request has been made to
 - `time_created`: Server time that the request was made (current time)
 - `time_last_updated`: Server time that the request was last updated (current time)
 - `status`: Status of the request. Always pending when initialised, later it can be success or failed.

#### Response Examples 
```
[
  {
    "request_id": "b91857ac-f48c-49a0-a26c-36f07df43a56",
    "model_name": "test-model",
    "model_version": "v1",
    "time_created": "2020-02-03T13:19:45.310+00:00",
    "time_last_updated": "2020-02-03T13:19:45.310+00:00",
    "status": "pending"
  }
]



### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import xenia_python_client_library
from xenia_python_client_library.rest import ApiException
from pprint import pprint
configuration = xenia_python_client_library.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.dutchanalytics.net/v1.1
configuration.host = "https://api.dutchanalytics.net/v1.1"
# Create an instance of the API class
api_instance = xenia_python_client_library.CoreApi(xenia_python_client_library.ApiClient(configuration))
project_name = 'project_name_example' # str | 
pipeline_name = 'pipeline_name_example' # str | 

try:
    # Retrieve pending pipeline requests
    api_response = api_instance.pipeline_insert_retrieve_pending(project_name, pipeline_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CoreApi->pipeline_insert_retrieve_pending: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **pipeline_name** | **str**|  | 

### Return type

[**list[PipelineResultList]**](PipelineResultList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pipeline_object_attachments_create**
> Attachments pipeline_object_attachments_create(project_name, pipeline_name, data)

Create object attachments


### Description 
Create an attachment between two pipeline objects. An attachment can only be made between two objects that have already been added to the pipeline. 
The object where the attachment starts is called the source object. The object that is linked is called the destination object. When attaching two objects, one must also define which source object output fields link to which destination object input fields.
All the input fields in the destination object must be provided in the mapping. In contrast, not all source object output fields need to be used in the mapping. This means that one source output field may link to multiple destination input fields.

A connector object can only be a destination object.

The pipeline_start object can only be a source object.

In case of blob type of objects, the mapping must be omitted or given as an empty list.

### Required Parameters 
- `source_name`: Name of the source pipeline object
 - `destination_name`: Name of the destination pipeline object
 - `mapping`: A list of dictionaries containing source_field_name and destination_field_name keys. The source and destination fields should match in data type. Integer source fields can only be mapped to integer type destination fields.

#### Request Examples 
An attachment between a model version and connector

```
{
  "source_name": "model-1-v1",
  "destination_name": "connector-1",
  "mapping": [
    {
      "source_field_name": "model-output-field-1",
      "destination_field_name": "connector-field-1"
    },
    {
      "source_field_name": "model-output-field-2",
      "destination_field_name": "connector-field-2"
    },
    {
      "source_field_name": "model-output-field-3",
      "destination_field_name": "connector-field-3"
    }
  ]
}
```

```
{
  "source_name": "blob-model-v3",
  "destination_name": "s3-connector",
  "mapping": []
}
```
 
 An attachment between a pipeline and model version

```
{
  "source_name": "pipeline_start",
  "destination_name": "model-2-v2",
  "mapping": [
    {
      "source_field_name": "pipeline-input-field-1",
      "destination_field_name": "model-input-field-1"
    },
    {
      "source_field_name": "pipeline-input-field-2",
      "destination_field_name": "model-input-field-2"
    }
  ]
}
```

### Response Structure 
Details of the created attachment
 - `source_name`: Name of the source pipeline object
 - `destination_name`: Name of the destination pipeline object
 - `mapping`: A list of dictionaries containing source_field_name and destination_field_name

#### Response Examples 
```
{
  "source_name": "pipeline-1",
  "destination_name": "model-2-v2",
  "mapping": [
    {
      "source_field_name": "pipeline-input-field-1",
      "destination_field_name": "model-input-field-1"
    },
    {
      "source_field_name": "pipeline-input-field-2",
      "destination_field_name": "model-input-field-2"
    }
  ]
}
```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import xenia_python_client_library
from xenia_python_client_library.rest import ApiException
from pprint import pprint
configuration = xenia_python_client_library.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.dutchanalytics.net/v1.1
configuration.host = "https://api.dutchanalytics.net/v1.1"
# Create an instance of the API class
api_instance = xenia_python_client_library.CoreApi(xenia_python_client_library.ApiClient(configuration))
project_name = 'project_name_example' # str | 
pipeline_name = 'pipeline_name_example' # str | 
data = xenia_python_client_library.AttachmentsCreate() # AttachmentsCreate | 

try:
    # Create object attachments
    api_response = api_instance.pipeline_object_attachments_create(project_name, pipeline_name, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CoreApi->pipeline_object_attachments_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **pipeline_name** | **str**|  | 
 **data** | [**AttachmentsCreate**](AttachmentsCreate.md)|  | 

### Return type

[**Attachments**](Attachments.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pipeline_object_attachments_delete**
> pipeline_object_attachments_delete(project_name, destination_name, pipeline_name, source_name)

Delete attachment of a source and destination object


### Description 
Delete an attachment in a pipeline. The referenced and original objects of the attachment still exist in the pipeline, only the link between them is deleted.
### Required Parameters 
- None


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import xenia_python_client_library
from xenia_python_client_library.rest import ApiException
from pprint import pprint
configuration = xenia_python_client_library.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.dutchanalytics.net/v1.1
configuration.host = "https://api.dutchanalytics.net/v1.1"
# Create an instance of the API class
api_instance = xenia_python_client_library.CoreApi(xenia_python_client_library.ApiClient(configuration))
project_name = 'project_name_example' # str | 
destination_name = 'destination_name_example' # str | 
pipeline_name = 'pipeline_name_example' # str | 
source_name = 'source_name_example' # str | 

try:
    # Delete attachment of a source and destination object
    api_instance.pipeline_object_attachments_delete(project_name, destination_name, pipeline_name, source_name)
except ApiException as e:
    print("Exception when calling CoreApi->pipeline_object_attachments_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **destination_name** | **str**|  | 
 **pipeline_name** | **str**|  | 
 **source_name** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pipeline_object_attachments_get**
> AttachmentsList pipeline_object_attachments_get(project_name, destination_name, pipeline_name, source_name)

Get an attachment of a source and destination object


### Description 
Get the details of a single attachment between a source and destination object in a pipeline

### Required Parameters 
- None

### Response Structure 
Details of the attachment
 - `source_name`: Name of the source pipeline object
 - `destination_name`: Name of the destination pipeline object
 - `mapping`: A list of dictionaries containing the link between the source object output field (source_field_name) and destination object input field (destination_field_name)

#### Response Examples 
```
{
  "source_name": "model-2-v2",
  "destination_name": "model-3-v1",
  "mapping": [
    {
      "source_field_name": "model-2-output-field-1",
      "destination_field_name": "model-3-input-field-1"
    },
    {
      "source_field_name": "model-2-output-field-2",
      "destination_field_name": "model-3-input-field-2"
    }
  ]
}
```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import xenia_python_client_library
from xenia_python_client_library.rest import ApiException
from pprint import pprint
configuration = xenia_python_client_library.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.dutchanalytics.net/v1.1
configuration.host = "https://api.dutchanalytics.net/v1.1"
# Create an instance of the API class
api_instance = xenia_python_client_library.CoreApi(xenia_python_client_library.ApiClient(configuration))
project_name = 'project_name_example' # str | 
destination_name = 'destination_name_example' # str | 
pipeline_name = 'pipeline_name_example' # str | 
source_name = 'source_name_example' # str | 

try:
    # Get an attachment of a source and destination object
    api_response = api_instance.pipeline_object_attachments_get(project_name, destination_name, pipeline_name, source_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CoreApi->pipeline_object_attachments_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **destination_name** | **str**|  | 
 **pipeline_name** | **str**|  | 
 **source_name** | **str**|  | 

### Return type

[**AttachmentsList**](AttachmentsList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pipeline_object_attachments_list**
> list[AttachmentsList] pipeline_object_attachments_list(project_name, pipeline_name)

List object attachments


### Description 
List all attachments in a pipeline

### Required Parameters 
- None

### Response Structure 
A list of details of the attachments in the pipeline
 - `source_name`: Name of the source pipeline object
 - `destination_name`: Name of the destination pipeline object
 - `mapping`: A list of dictionaries containing source_field_name and destination_field_name

#### Response Examples 
```
[
  {
    "source_name": "pipeline-1",
    "destination_name": "model-2-v2",
    "mapping": [
      {
        "source_field_name": "pipeline-input-field-1",
        "destination_field_name": "model-input-field-1"
      },
      {
        "source_field_name": "pipeline-input-field-2",
        "destination_field_name": "model-input-field-2"
      }
    ]
  },
  {
    "source_name": "model-2-v2",
    "destination_name": "connector-1",
    "mapping": [
      {
        "source_field_name": "model-output-field-1",
        "destination_field_name": "connector-field-1"
      },
      {
        "source_field_name": "model-output-field-2",
        "destination_field_name": "connector-field-2"
      },
      {
        "source_field_name": "model-output-field-3",
        "destination_field_name": "connector-field-3"
      }
    ]
  },
  {
    "source_name": "blob-model-v3",
    "destination_name": "s3-connector",
    "mapping": []
  }
]
```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import xenia_python_client_library
from xenia_python_client_library.rest import ApiException
from pprint import pprint
configuration = xenia_python_client_library.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.dutchanalytics.net/v1.1
configuration.host = "https://api.dutchanalytics.net/v1.1"
# Create an instance of the API class
api_instance = xenia_python_client_library.CoreApi(xenia_python_client_library.ApiClient(configuration))
project_name = 'project_name_example' # str | 
pipeline_name = 'pipeline_name_example' # str | 

try:
    # List object attachments
    api_response = api_instance.pipeline_object_attachments_list(project_name, pipeline_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CoreApi->pipeline_object_attachments_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **pipeline_name** | **str**|  | 

### Return type

[**list[AttachmentsList]**](AttachmentsList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pipeline_object_attachments_source_get**
> list[AttachmentsList] pipeline_object_attachments_source_get(project_name, pipeline_name, source_name)

List the attachments of a source object


### Description 
List attachments of one object in a pipeline

### Required Parameters 
- None

### Response Structure 
A list of details of the attachments of the given source object in the pipeline
 - `source_name`: Name of the source pipeline object
 - `destination_name`: Name of the destination pipeline object
 - `mapping`: A list of dictionaries containing the link between the source object output field (source_field_name) and destination object input field (destination_field_name)

#### Response Examples 
```
[
  {
    "source_name": "model-2-v2",
    "destination_name": "connector-1",
    "mapping": [
      {
        "source_field_name": "model-2-output-field-1",
        "destination_field_name": "connector-field-1"
      },
      {
        "source_field_name": "model-2-output-field-2",
        "destination_field_name": "connector-field-2"
      },
      {
        "source_field_name": "model-2-output-field-3",
        "destination_field_name": "connector-field-3"
      }
    ]
  },
  {
    "source_name": "model-2-v2",
    "destination_name": "model-3-v1",
    "mapping": [
      {
        "source_field_name": "model-2-output-field-1",
        "destination_field_name": "model-3-input-field-1"
      },
      {
        "source_field_name": "model-2-output-field-2",
        "destination_field_name": "model-3-input-field-2"
      }
    ]
  }
]
```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import xenia_python_client_library
from xenia_python_client_library.rest import ApiException
from pprint import pprint
configuration = xenia_python_client_library.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.dutchanalytics.net/v1.1
configuration.host = "https://api.dutchanalytics.net/v1.1"
# Create an instance of the API class
api_instance = xenia_python_client_library.CoreApi(xenia_python_client_library.ApiClient(configuration))
project_name = 'project_name_example' # str | 
pipeline_name = 'pipeline_name_example' # str | 
source_name = 'source_name_example' # str | 

try:
    # List the attachments of a source object
    api_response = api_instance.pipeline_object_attachments_source_get(project_name, pipeline_name, source_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CoreApi->pipeline_object_attachments_source_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **pipeline_name** | **str**|  | 
 **source_name** | **str**|  | 

### Return type

[**list[AttachmentsList]**](AttachmentsList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pipeline_object_environment_variables_list**
> list[InheritedEnvironmentVariableList] pipeline_object_environment_variables_list(project_name, name, pipeline_name)

List pipeline object environment variables


### Description
List environment variables accessible to objects in the pipeline.
 
### Response Structure 
 A list of variables described by the following fields:
 - `id`: Unique identifier for the environment variable
 - `name`: Variable name
 - `value`: Variable value (will be null for secret variables)
 - `secret`: Boolean that indicates if this variable contains sensitive information
 - `inheritance_type`: Type of parent object that this variable is inherited from - can be `project`, `model`, or `model_version`
 - `inheritance_name`: Name of the parent object that this variable is inherited from

#### Response Examples 
```
[
  {
    "id": "4c15a27e-25ea-4be0-86c7-f4790389d061",
    "name": "database_schema",
    "value": "public",
    "secret": false,
    "inheritance_type": "model",
    "inheritance_name": "model_name"
  },
  {
    "id": "06c2c8be-507e-4fae-981d-54e94f22dab0",
    "name": "database_password",
    "value": null,
    "secret": true,
    "inheritance_type": "project",
    "inheritance_name": "project_name"
  }
]
```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import xenia_python_client_library
from xenia_python_client_library.rest import ApiException
from pprint import pprint
configuration = xenia_python_client_library.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.dutchanalytics.net/v1.1
configuration.host = "https://api.dutchanalytics.net/v1.1"
# Create an instance of the API class
api_instance = xenia_python_client_library.CoreApi(xenia_python_client_library.ApiClient(configuration))
project_name = 'project_name_example' # str | 
name = 'name_example' # str | 
pipeline_name = 'pipeline_name_example' # str | 

try:
    # List pipeline object environment variables
    api_response = api_instance.pipeline_object_environment_variables_list(project_name, name, pipeline_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CoreApi->pipeline_object_environment_variables_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **name** | **str**|  | 
 **pipeline_name** | **str**|  | 

### Return type

[**list[InheritedEnvironmentVariableList]**](InheritedEnvironmentVariableList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pipeline_objects_create**
> PipelineObjectList pipeline_objects_create(project_name, pipeline_name, data)

Add an object to a pipeline


### Description 
Create a pipeline object, which can be a connector or model. The pipeline object that is added is a reference to the real object. In this way, multiple references to the same object may be added to a pipeline.
In case of model reference_type, the reference_name refers to the model name and the version is the version of the model which will be added to the pipeline as an object.

### Required Parameters 
- `name`: Name of the pipeline object. It is unique within a pipeline
- `reference_type`: Type of the object it will reference. It can either be a model or connector
- `reference_name`: Name of the object it will reference

### Optional Parameters 
 - `version`: Version name. If the reference_type model is given, this field must be given too. If the reference_type is connector, this field should be omitted in the request.

#### Request Examples 
An object referencing a model version

```
{
  "name": "model-1-v1",
  "reference_type": "model",
  "reference_name": "model-1",
  "version": "version-1"
}
```
 
An object referencing a connector

```
{
  "name": "s3-connector",
  "reference_type": "connector",
  "reference_name": "s3-connector"
}
```

### Response Structure 
Details of the created pipeline object
 - `id`: Unique identifier for the pipeline object (UUID)
 - `name`: Name of the pipeline object
 - `reference_type`: Type of the object it will reference
 - `reference_name`: Name of the object it will reference
 - `version`: Version name in case of model reference_type

#### Response Examples 
```
{
  "id": "c91724b6-d73c-4933-b2aa-aefd9e34ce3e",
  "name": "model-1-v1",
  "reference_type": "model",
  "reference_name": "model-1",
  "version": "version-1"
}
```
 
```
{
  "id": "1a4b0e28-3de1-442a-b1eb-947f22a69381",
  "name": "s3-connector",
  "reference_type": "connector",
  "reference_name": "s3-connector"
}
```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import xenia_python_client_library
from xenia_python_client_library.rest import ApiException
from pprint import pprint
configuration = xenia_python_client_library.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.dutchanalytics.net/v1.1
configuration.host = "https://api.dutchanalytics.net/v1.1"
# Create an instance of the API class
api_instance = xenia_python_client_library.CoreApi(xenia_python_client_library.ApiClient(configuration))
project_name = 'project_name_example' # str | 
pipeline_name = 'pipeline_name_example' # str | 
data = xenia_python_client_library.PipelineObjectCreate() # PipelineObjectCreate | 

try:
    # Add an object to a pipeline
    api_response = api_instance.pipeline_objects_create(project_name, pipeline_name, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CoreApi->pipeline_objects_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **pipeline_name** | **str**|  | 
 **data** | [**PipelineObjectCreate**](PipelineObjectCreate.md)|  | 

### Return type

[**PipelineObjectList**](PipelineObjectList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pipeline_objects_delete**
> pipeline_objects_delete(project_name, name, pipeline_name)

Delete object from pipeline

  
### Description 
Delete a pipeline object. Only the reference in the pipeline is deleted. The original object (model, model version and connector) still exists.
If the object is attached to another object, it cannot be deleted, all attachments of the object must be removed first.

### Required Parameters 
- None


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import xenia_python_client_library
from xenia_python_client_library.rest import ApiException
from pprint import pprint
configuration = xenia_python_client_library.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.dutchanalytics.net/v1.1
configuration.host = "https://api.dutchanalytics.net/v1.1"
# Create an instance of the API class
api_instance = xenia_python_client_library.CoreApi(xenia_python_client_library.ApiClient(configuration))
project_name = 'project_name_example' # str | 
name = 'name_example' # str | 
pipeline_name = 'pipeline_name_example' # str | 

try:
    # Delete object from pipeline
    api_instance.pipeline_objects_delete(project_name, name, pipeline_name)
except ApiException as e:
    print("Exception when calling CoreApi->pipeline_objects_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **name** | **str**|  | 
 **pipeline_name** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pipeline_objects_get**
> PipelineObjectList pipeline_objects_get(project_name, name, pipeline_name)

Get an object in a pipeline


### Description 
Retrieve the details of a single pipeline object

### Required Parameters 
- None

### Response Structure 
Details of the pipeline object
 - `id`: Unique identifier for the pipeline object (UUID)
 - `name`: Name of the pipeline object
 - `reference_type`: Type of the object it references
 - `reference_name`: Name of the object it references
 - `version`: Version name in case of model reference_type

#### Response Examples 
A dictionary containing details of the pipeline object
```
{
  "id": "1a4b0e28-3de1-442a-b1eb-947f22a69381",
  "name": "s3-connector",
  "reference_type": "connector",
  "reference_name": "s3-connector"
}
```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import xenia_python_client_library
from xenia_python_client_library.rest import ApiException
from pprint import pprint
configuration = xenia_python_client_library.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.dutchanalytics.net/v1.1
configuration.host = "https://api.dutchanalytics.net/v1.1"
# Create an instance of the API class
api_instance = xenia_python_client_library.CoreApi(xenia_python_client_library.ApiClient(configuration))
project_name = 'project_name_example' # str | 
name = 'name_example' # str | 
pipeline_name = 'pipeline_name_example' # str | 

try:
    # Get an object in a pipeline
    api_response = api_instance.pipeline_objects_get(project_name, name, pipeline_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CoreApi->pipeline_objects_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **name** | **str**|  | 
 **pipeline_name** | **str**|  | 

### Return type

[**PipelineObjectList**](PipelineObjectList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pipeline_objects_list**
> list[PipelineObjectList] pipeline_objects_list(project_name, pipeline_name)

List objects in a pipeline


### Description 
List all pipeline objects (connectors/models) in a pipeline

### Required Parameters 
- None

### Response Structure 
A list of details of the pipeline objects in the pipeline
 - `id`: Unique identifier for the pipeline object (UUID)
 - `name`: Name of the pipeline object
 - `reference_type`: Type of the object it references
 - `reference_name`: Name of the object it references
 - `version`: Version name in case of model reference_type

#### Response Examples 
```
A list of pipeline objects
[
  {
    "id": "c91724b6-d73c-4933-b2aa-aefd9e34ce3e",
    "name": "model-1-v1",
    "reference_type": "model",
    "reference_name": "model-1",
    "version": "version-1"
  },
  {
    "id": "1a4b0e28-3de1-442a-b1eb-947f22a69381",
    "name": "s3-connector",
    "reference_type": "connector",
    "reference_name": "s3-connector"
  }
]
```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import xenia_python_client_library
from xenia_python_client_library.rest import ApiException
from pprint import pprint
configuration = xenia_python_client_library.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.dutchanalytics.net/v1.1
configuration.host = "https://api.dutchanalytics.net/v1.1"
# Create an instance of the API class
api_instance = xenia_python_client_library.CoreApi(xenia_python_client_library.ApiClient(configuration))
project_name = 'project_name_example' # str | 
pipeline_name = 'pipeline_name_example' # str | 

try:
    # List objects in a pipeline
    api_response = api_instance.pipeline_objects_list(project_name, pipeline_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CoreApi->pipeline_objects_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **pipeline_name** | **str**|  | 

### Return type

[**list[PipelineObjectList]**](PipelineObjectList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pipeline_objects_update**
> PipelineObjectList pipeline_objects_update(project_name, name, pipeline_name, data)

Update an object in a pipeline


### Description 
Update a pipeline object. It is not possible to update the reference_name and reference_type. All necessary fields are validated again.

### Optional Parameters 
 - `name`: New name for the pipeline object
 - `version`: New version for the pipeline object. Since the input and output fields of different model versions are the same, the version of a model pipeline object can be changed with another version of the same model.

#### Request Examples 
```
{
  "name": "new-pipeline-object-name"
}
```
 
```
{
  "name": "model-1-v2"
  "version": "version-2"
}
```

### Response Structure 
Details of the updated pipeline object
 - `id`: Unique identifier for the pipeline object (UUID)
 - `name`: Name of the pipeline object
 - `reference_type`: Type of the object it references
 - `reference_name`: Name of the object it references
 - `version`: Version name in case of model reference_type

#### Response Examples 
```
{
  "id": "c91724b6-d73c-4933-b2aa-aefd9e34ce3e",
  "name": "model-1-v2",
  "reference_type": "model",
  "reference_name": "model-1",
  "version": "version-2"
}
```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import xenia_python_client_library
from xenia_python_client_library.rest import ApiException
from pprint import pprint
configuration = xenia_python_client_library.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.dutchanalytics.net/v1.1
configuration.host = "https://api.dutchanalytics.net/v1.1"
# Create an instance of the API class
api_instance = xenia_python_client_library.CoreApi(xenia_python_client_library.ApiClient(configuration))
project_name = 'project_name_example' # str | 
name = 'name_example' # str | 
pipeline_name = 'pipeline_name_example' # str | 
data = xenia_python_client_library.PipelineObjectUpdate() # PipelineObjectUpdate | 

try:
    # Update an object in a pipeline
    api_response = api_instance.pipeline_objects_update(project_name, name, pipeline_name, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CoreApi->pipeline_objects_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **name** | **str**|  | 
 **pipeline_name** | **str**|  | 
 **data** | [**PipelineObjectUpdate**](PipelineObjectUpdate.md)|  | 

### Return type

[**PipelineObjectList**](PipelineObjectList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pipelines_create**
> PipelineList pipelines_create(project_name, data)

Create pipelines


    
### Description 
Create a pipeline in a project. The input_fields represent the fields that the input data should contain. When an object is attached to the pipeline, it means that the input data will be forwarded to these objects.

### Required Parameters 
- `name`: Name of the pipeline. It is unique within a project.
- `input_type`: Type of the connector. It can be either structured or blob.
- `input_fields`: A list of fields with name and data_type. In case of blob pipelines, the input_fields should be omitted or given as an empty list. For structured pipelines, they must be provided.

### Optional Parameters
- `description`: Description of the pipeline

#### Request Examples 
A structured pipeline

```
{
  "name": "pipeline-1",
  "input_type": "structured",
  "input_fields": [
    {
      "name": "field-1",
      "data_type": "int"
    },
    {
      "name": "field-2",
      "data_type": "double"
    }
  ]
}
```
 
 A blob pipeline

```
{
  "name": "pipeline-2",
  "input_type": "blob",
  "description": "my description"
}
```

```
{
  "name": "pipeline-2",
  "input_type": "blob",
  "input_fields": []
}
```

### Response Structure 
Details of the created pipeline
 - `id`: Unique identifier for the pipeline (UUID)
 - `name`: Name of the pipeline
 - `description`: Description of the pipeline
 - `project`: Project name in which the pipeline is created
 - `input_type`: Type of the pipeline
 - `input_fields`: A list of pipeline fields with name and data_type

#### Response Examples 
```
{
  "id": "6b0cea21-2657-4fa3-a331-de646e3cfdc4",
  "name": "pipeline-1",
  "project": "project-1",
  "description": "my description",
  "input_type": "structured",
  "input_fields": [
    {
      "name": "field-1",
      "data_type": "int"
    },
    {
      "name": "field-2",
      "data_type": "double"
    }
  ]
}
```
 
```
{
  "id": "b6f60ebf-48ef-4084-9fbb-9ac0f934093e",
  "name": "pipeline-2",
  "project": "project-1",
  "description": "my description",
  "input_type": "blob",
  "input_fields": []
}
```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import xenia_python_client_library
from xenia_python_client_library.rest import ApiException
from pprint import pprint
configuration = xenia_python_client_library.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.dutchanalytics.net/v1.1
configuration.host = "https://api.dutchanalytics.net/v1.1"
# Create an instance of the API class
api_instance = xenia_python_client_library.CoreApi(xenia_python_client_library.ApiClient(configuration))
project_name = 'project_name_example' # str | 
data = xenia_python_client_library.PipelineCreate() # PipelineCreate | 

try:
    # Create pipelines
    api_response = api_instance.pipelines_create(project_name, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CoreApi->pipelines_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **data** | [**PipelineCreate**](PipelineCreate.md)|  | 

### Return type

[**PipelineList**](PipelineList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pipelines_delete**
> pipelines_delete(project_name, pipeline_name)

Delete pipeline


### Description 
Delete a pipeline. This will also delete all objects and attachments contained in the pipeline.


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import xenia_python_client_library
from xenia_python_client_library.rest import ApiException
from pprint import pprint
configuration = xenia_python_client_library.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.dutchanalytics.net/v1.1
configuration.host = "https://api.dutchanalytics.net/v1.1"
# Create an instance of the API class
api_instance = xenia_python_client_library.CoreApi(xenia_python_client_library.ApiClient(configuration))
project_name = 'project_name_example' # str | 
pipeline_name = 'pipeline_name_example' # str | 

try:
    # Delete pipeline
    api_instance.pipelines_delete(project_name, pipeline_name)
except ApiException as e:
    print("Exception when calling CoreApi->pipelines_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **pipeline_name** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pipelines_get**
> PipelineList pipelines_get(project_name, pipeline_name)

Get pipeline


### Description 
Get the details of a single pipeline

### Response Structure 
Details of the pipeline
 - `id`: Unique identifier for the pipeline (UUID)
 - `name`: Name of the pipeline
 - `description` Description of the pipeline
 - `project`: Project name in which the pipeline is
 - `input_type`: Type of the pipeline
 - `input_fields`: A list of pipeline fields with name and data_type

#### Response Examples 
```
{
  "id": "b6f60ebf-48ef-4084-9fbb-9ac0f934093e",
  "name": "pipeline-2",
  "project": "project-1",
  "description": "my description",
  "input_type": "blob",
  "input_fields": []
}
```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import xenia_python_client_library
from xenia_python_client_library.rest import ApiException
from pprint import pprint
configuration = xenia_python_client_library.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.dutchanalytics.net/v1.1
configuration.host = "https://api.dutchanalytics.net/v1.1"
# Create an instance of the API class
api_instance = xenia_python_client_library.CoreApi(xenia_python_client_library.ApiClient(configuration))
project_name = 'project_name_example' # str | 
pipeline_name = 'pipeline_name_example' # str | 

try:
    # Get pipeline
    api_response = api_instance.pipelines_get(project_name, pipeline_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CoreApi->pipelines_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **pipeline_name** | **str**|  | 

### Return type

[**PipelineList**](PipelineList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pipelines_insert**
> PipelineInsertList pipelines_insert(project_name, pipeline_name, data)

Insert data in pipelines


### Description 
Insert a single data point into a pipeline. A trace_id specific for the insert is returned. With this trace_id, it is possible to:
- filter the logs to see the whole flow of the pipeline 

- retrieve the results of the pipeline 


This type of insert can only be made to pipelines with structured input type.

### Required Parameters 
- `data`: Request data. It should contain the input fields of the pipeline as keys.

#### Request Examples
```
{
  "data": {
    "pipeline-input-field-1": 5.0,
    "pipeline-input-field-2": "N"
  }
}
```

### Response Structure 
- `success`: Boolean field to indicate if the insert was successful
- `trace_id`: Unique identifier for the insert

#### Response Examples
```
{
  "success": "true",
  "trace_id": "668cdb12-f3cc-4d47-97ca-818698e490bd"
}
```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import xenia_python_client_library
from xenia_python_client_library.rest import ApiException
from pprint import pprint
configuration = xenia_python_client_library.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.dutchanalytics.net/v1.1
configuration.host = "https://api.dutchanalytics.net/v1.1"
# Create an instance of the API class
api_instance = xenia_python_client_library.CoreApi(xenia_python_client_library.ApiClient(configuration))
project_name = 'project_name_example' # str | 
pipeline_name = 'pipeline_name_example' # str | 
data = xenia_python_client_library.PipelineInsertCreate() # PipelineInsertCreate | 

try:
    # Insert data in pipelines
    api_response = api_instance.pipelines_insert(project_name, pipeline_name, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CoreApi->pipelines_insert: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **pipeline_name** | **str**|  | 
 **data** | [**PipelineInsertCreate**](PipelineInsertCreate.md)|  | 

### Return type

[**PipelineInsertList**](PipelineInsertList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pipelines_insert_blob**
> PipelineInsertList pipelines_insert_blob(project_name, pipeline_name, file)

Insert blobs in pipelines


### Description 
Insert a blob to a pipeline. 

This type of insert can only be made to pipelines with blob input type.

### Required Parameters 
- `file`: The blob file to be inserted to the pipeline

### Response Structure 
- `success`: Boolean field to indicate if the insert was successful
- `trace_id`: Unique identifier for the insert

#### Response Examples 
```
{
  "success": "true",
  "trace_id": "1000882e-95b0-47e9-80dc-f8bb42057647"
}
```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import xenia_python_client_library
from xenia_python_client_library.rest import ApiException
from pprint import pprint
configuration = xenia_python_client_library.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.dutchanalytics.net/v1.1
configuration.host = "https://api.dutchanalytics.net/v1.1"
# Create an instance of the API class
api_instance = xenia_python_client_library.CoreApi(xenia_python_client_library.ApiClient(configuration))
project_name = 'project_name_example' # str | 
pipeline_name = 'pipeline_name_example' # str | 
file = '/path/to/file' # file | 

try:
    # Insert blobs in pipelines
    api_response = api_instance.pipelines_insert_blob(project_name, pipeline_name, file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CoreApi->pipelines_insert_blob: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **pipeline_name** | **str**|  | 
 **file** | **file**|  | 

### Return type

[**PipelineInsertList**](PipelineInsertList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pipelines_insert_bulk**
> PipelineInsertList pipelines_insert_bulk(project_name, pipeline_name, data)

Insert data in bulk to pipelines


    
### Description 
Insert multiple data points to a pipeline. A trace_id specific for the insert is returned. With this trace_id, it is possible to:
- filter the logs to see the whole flow of the pipeline 

- retrieve the results of the pipeline 


The trace_id is the same for all data points in the request.

This type of insert can only be made to pipelines with structured input type. If one of the data is faulty, the whole insert is denied. 

The maximum number of data points per bulk call is 250.

### Required Parameters 
A list of one or more dictionaries, with each dictionary being a pipeline request containing the required parameters.
- `data`: Request data. It should contain the input fields of the pipeline as keys.

#### Request Examples 
```
[
  {
    "data": {
      "pipeline-input-field-1": 5.0,
      "pipeline-input-field-2": "N"
    }
  },
  {
    "data": {
      "pipeline-input-field-1": 4.0,
      "pipeline-input-field-2": "S"
    }
  }
]
```

### Response Structure 
 - `success`: Boolean field to indicate if the insert was successful
 - `trace_id`: Unique identifier for the insert

#### Response Examples 
```
[
  {
    "success": "true",
    "trace_id": "668cdb12-f3cc-4d47-97ca-818698e490bd"
  },
  {
    "success": "true",
    "trace_id": "a661554b-cd22-4d5d-9515-c7badbfc3133"
  }
]
```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import xenia_python_client_library
from xenia_python_client_library.rest import ApiException
from pprint import pprint
configuration = xenia_python_client_library.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.dutchanalytics.net/v1.1
configuration.host = "https://api.dutchanalytics.net/v1.1"
# Create an instance of the API class
api_instance = xenia_python_client_library.CoreApi(xenia_python_client_library.ApiClient(configuration))
project_name = 'project_name_example' # str | 
pipeline_name = 'pipeline_name_example' # str | 
data = xenia_python_client_library.PipelineInsertCreate() # PipelineInsertCreate | 

try:
    # Insert data in bulk to pipelines
    api_response = api_instance.pipelines_insert_bulk(project_name, pipeline_name, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CoreApi->pipelines_insert_bulk: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **pipeline_name** | **str**|  | 
 **data** | [**PipelineInsertCreate**](PipelineInsertCreate.md)|  | 

### Return type

[**PipelineInsertList**](PipelineInsertList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pipelines_list**
> list[PipelineList] pipelines_list(project_name)

List pipelines


### Description 
List all pipelines in a project

### Response Structure 
A list of details of the pipelines in the project
 - `id`: Unique identifier for the pipeline (UUID)
 - `name`: Name of the pipeline
 - `project`: Project name in which the pipeline is
 - `description`: Description of the pipeline
 - `input_type`: Type of the pipeline
 - `input_fields`: A list of pipeline fields with name and data_type

#### Response Examples 
```
[
  {
    "id": "6b0cea21-2657-4fa3-a331-de646e3cfdc4",
    "name": "pipeline-1",
    "project": "project-1",
    "description": "my description",
    "input_type": "structured",
    "input_fields": [
      {
        "name": "field-1",
        "data_type": "int"
      },
      {
        "name": "field-2",
        "data_type": "double"
      }
    ]
  },
  {
    "id": "b6f60ebf-48ef-4084-9fbb-9ac0f934093e",
    "name": "pipeline-2",
    "project": "project-1",
    "description": "my description",
    "input_type": "blob",
    "input_fields": []
  }
]
```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import xenia_python_client_library
from xenia_python_client_library.rest import ApiException
from pprint import pprint
configuration = xenia_python_client_library.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.dutchanalytics.net/v1.1
configuration.host = "https://api.dutchanalytics.net/v1.1"
# Create an instance of the API class
api_instance = xenia_python_client_library.CoreApi(xenia_python_client_library.ApiClient(configuration))
project_name = 'project_name_example' # str | 

try:
    # List pipelines
    api_response = api_instance.pipelines_list(project_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CoreApi->pipelines_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 

### Return type

[**list[PipelineList]**](PipelineList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pipelines_update**
> PipelineList pipelines_update(project_name, pipeline_name, data)

Update pipeline


    
### Description 
Update a pipeline. All necessary fields are validated again.

### Optional Parameters 
 - `name`: New name for the pipeline
 - `description`: New description for the pipeline
 - `input_type`: New type for the pipeline. It is possible to change the type from blob to structured and vice versa.
 - `input_fields`: New input fields for the pipeline.

If the type of pipeline was blob, the given fields are created for the pipeline.
If the type of pipeline was structured, the old fields are replaced with the new ones. If one or more old fields need to be kept, they must be provided again. In case an error occurs while creating the new fields, the pipeline will still have the old fields.
If the pipeline is updated to have blob type, input_fields should be provided as en empty list or should not be provided.

#### Request Examples 
```
{
  "name": "new-pipeline-name"
}
```

```
{
  "description": "New pipeline description"
}
```

```
{
  "input_type": "blob"
}
```

```
{
  "input_type": "blob",
  "input_fields": []
}
```
 
```
{
  "input_type": "structured",
  "input_fields": [
    {
      "name": "new-field-1",
      "data_type": "array_double"
    },
    {
      "name": "new-field-2",
      "data_type": "array_string"
    }
  ]
}
```

### Response Structure 
Details of the updated pipeline
 - `id`: Unique identifier for the pipeline (UUID)
 - `name`: Name of the pipeline
 - `project`: Project name in which the pipeline is
 - `description`: Description for the pipeline
 - `input_type`: Type of the pipeline
 - `input_fields`: A list of pipeline fields with name and data_type

#### Response Examples 
```
{
  "id": "b6f60ebf-48ef-4084-9fbb-9ac0f934093e",
  "name": "new-pipeline-name",
  "project": "project-1",
  "description": "my description",
  "input_type": "structured",
  "input_fields": [
    {
      "name": "new-field-1",
      "data_type": "array_double"
    },
    {
      "name": "new-field-2",
      "data_type": "array_string"
    }
  ]
}
```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import xenia_python_client_library
from xenia_python_client_library.rest import ApiException
from pprint import pprint
configuration = xenia_python_client_library.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.dutchanalytics.net/v1.1
configuration.host = "https://api.dutchanalytics.net/v1.1"
# Create an instance of the API class
api_instance = xenia_python_client_library.CoreApi(xenia_python_client_library.ApiClient(configuration))
project_name = 'project_name_example' # str | 
pipeline_name = 'pipeline_name_example' # str | 
data = xenia_python_client_library.PipelineCreate() # PipelineCreate | 

try:
    # Update pipeline
    api_response = api_instance.pipelines_update(project_name, pipeline_name, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CoreApi->pipelines_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **pipeline_name** | **str**|  | 
 **data** | [**PipelineCreate**](PipelineCreate.md)|  | 

### Return type

[**PipelineList**](PipelineList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **project_environment_variables_create**
> EnvironmentVariableList project_environment_variables_create(project_name, data)

Create project environment variable


### Description
Create an environment variable for the project. This variable will be inherited by all models in this project.

### Required Parameters
 - `name`: The name of the variable. The variable will have this name when accessed from your model code. The variable name should contain only letters and underscores, and not start or end with an underscore.
 - `value`: The value of the variable as a string. It may be an empty string ("").
 - `secret`: If this variable contains sensitive information, set this to true to hide it from other users.

#### Request Examples
```
{
  "name": "database_schema",
  "value": "public",
  "secret": false
}
```
```
{
  "name": "database_password",
  "value": "password",
  "secret": true
}
```

### Response Structure 
 A list of variables described by the following fields:
 - `id`: Unique identifier for the environment variable
 - `name`: Variable name
 - `value`: Variable value (will be null for secret variables)
 - `secret`: Boolean that indicates if this variable contains sensitive information

#### Response Examples 
```
{
  "id": "4c15a27e-25ea-4be0-86c7-f4790389d061",
  "name": "database_schema",
  "value": "public",
  "secret": false
}
```
```
{
  "id": "06c2c8be-507e-4fae-981d-54e94f22dab0",
  "name": "database_password",
  "value": null,
  "secret": true
}
```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import xenia_python_client_library
from xenia_python_client_library.rest import ApiException
from pprint import pprint
configuration = xenia_python_client_library.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.dutchanalytics.net/v1.1
configuration.host = "https://api.dutchanalytics.net/v1.1"
# Create an instance of the API class
api_instance = xenia_python_client_library.CoreApi(xenia_python_client_library.ApiClient(configuration))
project_name = 'project_name_example' # str | 
data = xenia_python_client_library.EnvironmentVariableCreate() # EnvironmentVariableCreate | 

try:
    # Create project environment variable
    api_response = api_instance.project_environment_variables_create(project_name, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CoreApi->project_environment_variables_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **data** | [**EnvironmentVariableCreate**](EnvironmentVariableCreate.md)|  | 

### Return type

[**EnvironmentVariableList**](EnvironmentVariableList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **project_environment_variables_delete**
> project_environment_variables_delete(project_name, id)

Delete project environment variable


### Description

Delete an environment variable of the project.

### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import xenia_python_client_library
from xenia_python_client_library.rest import ApiException
from pprint import pprint
configuration = xenia_python_client_library.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.dutchanalytics.net/v1.1
configuration.host = "https://api.dutchanalytics.net/v1.1"
# Create an instance of the API class
api_instance = xenia_python_client_library.CoreApi(xenia_python_client_library.ApiClient(configuration))
project_name = 'project_name_example' # str | 
id = 'id_example' # str | 

try:
    # Delete project environment variable
    api_instance.project_environment_variables_delete(project_name, id)
except ApiException as e:
    print("Exception when calling CoreApi->project_environment_variables_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **project_environment_variables_get**
> EnvironmentVariableList project_environment_variables_get(project_name, id)

Get project environment variable


### Description
Retrieve details of a project environment variable.

### Response Structure 
 A list of variables described by the following fields:
 - `id`: Unique identifier for the environment variable
 - `name`: Variable name
 - `value`: Variable value (will be null for secret variables)
 - `secret`: Boolean that indicates if this variable contains sensitive information

#### Response Examples 
```
[
  {
    "id": "4c15a27e-25ea-4be0-86c7-f4790389d061",
    "name": "database_schema",
    "value": "public",
    "secret": false
  }
]
```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import xenia_python_client_library
from xenia_python_client_library.rest import ApiException
from pprint import pprint
configuration = xenia_python_client_library.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.dutchanalytics.net/v1.1
configuration.host = "https://api.dutchanalytics.net/v1.1"
# Create an instance of the API class
api_instance = xenia_python_client_library.CoreApi(xenia_python_client_library.ApiClient(configuration))
project_name = 'project_name_example' # str | 
id = 'id_example' # str | 

try:
    # Get project environment variable
    api_response = api_instance.project_environment_variables_get(project_name, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CoreApi->project_environment_variables_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **id** | **str**|  | 

### Return type

[**EnvironmentVariableList**](EnvironmentVariableList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **project_environment_variables_list**
> list[EnvironmentVariableList] project_environment_variables_list(project_name)

List project environment variables


### Description
List the environment variables defined for the project. These are the variables that are inherited by all models in this project.
 
### Response Structure 
 A list of variables described by the following fields:
 - `id`: Unique identifier for the environment variable
 - `name`: Variable name
 - `value`: Variable value (will be null for secret variables)
 - `secret`: Boolean that indicates if this variable contains sensitive information

#### Response Examples 
```
[
  {
    "id": "4c15a27e-25ea-4be0-86c7-f4790389d061",
    "name": "database_schema",
    "value": "public",
    "secret": false
  },
  {
    "id": "06c2c8be-507e-4fae-981d-54e94f22dab0",
    "name": "database_password",
    "value": null,
    "secret": true
  }
]
```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import xenia_python_client_library
from xenia_python_client_library.rest import ApiException
from pprint import pprint
configuration = xenia_python_client_library.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.dutchanalytics.net/v1.1
configuration.host = "https://api.dutchanalytics.net/v1.1"
# Create an instance of the API class
api_instance = xenia_python_client_library.CoreApi(xenia_python_client_library.ApiClient(configuration))
project_name = 'project_name_example' # str | 

try:
    # List project environment variables
    api_response = api_instance.project_environment_variables_list(project_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CoreApi->project_environment_variables_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 

### Return type

[**list[EnvironmentVariableList]**](EnvironmentVariableList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **project_environment_variables_update**
> EnvironmentVariableList project_environment_variables_update(project_name, id, data)

Update project environment variable


### Description
Update an environment variable for the project.

### Required Parameters
 - `name`: The name of the variable. The variable will have this name when accessed from your model code. The variable name should contain only letters and underscores, and not start or end with an underscore.
 - `value`: The value of the variable as a string. It may be an empty string ("").
 - `secret`: If this variable contains sensitive information, set this to true to hide it from other users. Can be updated from false to true, but not from true to false (i.e. secrets will stay secrets).

#### Request Examples
```
{
  "name": "database_schema",
  "value": "new+schema",
  "secret": false
}
```

### Response Structure 
 A list of variables described by the following fields:
 - `id`: Unique identifier for the environment variable
 - `name`: Variable name
 - `value`: Variable value (will be null for secret variables)
 - `secret`: Boolean that indicates if this variable contains sensitive information

#### Response Examples 
```
{
"id": "4c15a27e-25ea-4be0-86c7-f4790389d061",
"name": "database_schema",
"value": "new_schema",
"secret": false
}
```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import xenia_python_client_library
from xenia_python_client_library.rest import ApiException
from pprint import pprint
configuration = xenia_python_client_library.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.dutchanalytics.net/v1.1
configuration.host = "https://api.dutchanalytics.net/v1.1"
# Create an instance of the API class
api_instance = xenia_python_client_library.CoreApi(xenia_python_client_library.ApiClient(configuration))
project_name = 'project_name_example' # str | 
id = 'id_example' # str | 
data = xenia_python_client_library.EnvironmentVariableCreate() # EnvironmentVariableCreate | 

try:
    # Update project environment variable
    api_response = api_instance.project_environment_variables_update(project_name, id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CoreApi->project_environment_variables_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **id** | **str**|  | 
 **data** | [**EnvironmentVariableCreate**](EnvironmentVariableCreate.md)|  | 

### Return type

[**EnvironmentVariableList**](EnvironmentVariableList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_create**
> ProjectList projects_create(data)

Create projects


### Description 
Create a new project with the provided name.
**Only the organization admins have permission to make this request.** When a new project is created, the current organization admins are assigned project-admin role for the created project.

### Required Parameters 
 - `name`: Name of the project. The name is globally unique. It can only consist of lowercase letters, numbers and dashes (-), and must start with a lowercase letter. 

 - `organization_name`: Name of the organization in which the project is going to be created
 
#### Request Examples 
```
{
  "name": "project-1",
  "organization_name": "organization-1"
}
```

### Response Structure 
Details of the created project
 - `id`: Unique identifier for the project (UUID) 

 - `name`: Name of the project 

 - `creation_date`: Time the project was created 

 - `organization_name`: Name of the organization in which the project is created

#### Response Examples 
```
{
  "id": "e988ddc0-3ef1-42d2-ab30-9f810a5e7063",
  "name": "project-1",
  "creation_date": "2018-10-26",
  "organization_name": "organization-1"
}
```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import xenia_python_client_library
from xenia_python_client_library.rest import ApiException
from pprint import pprint
configuration = xenia_python_client_library.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.dutchanalytics.net/v1.1
configuration.host = "https://api.dutchanalytics.net/v1.1"
# Create an instance of the API class
api_instance = xenia_python_client_library.CoreApi(xenia_python_client_library.ApiClient(configuration))
data = xenia_python_client_library.ProjectCreate() # ProjectCreate | 

try:
    # Create projects
    api_response = api_instance.projects_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CoreApi->projects_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**ProjectCreate**](ProjectCreate.md)|  | 

### Return type

[**ProjectList**](ProjectList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_delete**
> projects_delete(project_name)

Delete a project


### Description 
Delete a project. The user making the request must have appropriate permissions.
**When project is deleted, all the models, connectors and pipelines defined in it are also deleted.**


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import xenia_python_client_library
from xenia_python_client_library.rest import ApiException
from pprint import pprint
configuration = xenia_python_client_library.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.dutchanalytics.net/v1.1
configuration.host = "https://api.dutchanalytics.net/v1.1"
# Create an instance of the API class
api_instance = xenia_python_client_library.CoreApi(xenia_python_client_library.ApiClient(configuration))
project_name = 'project_name_example' # str | 

try:
    # Delete a project
    api_instance.projects_delete(project_name)
except ApiException as e:
    print("Exception when calling CoreApi->projects_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_get**
> ProjectList projects_get(project_name)

Get details of a project


### Description 
Get the details of a single project. The user making the request must have appropriate permissions.

### Response Structure 
Details of a project
 - `id`: Unique identifier for the project (UUID) 

 - `name`: Name of the project 

 - `creation_date`: Time the project was created 

 - `organization_name`: Name of the organization in which the project is created

#### Response Examples 
```
{
  "id": "e988ddc0-3ef1-42d2-ab30-9f810a5e7063",
  "name": "project-1",
  "creation_date": "2018-10-26",
  "organization_name": "organization-1"
}
```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import xenia_python_client_library
from xenia_python_client_library.rest import ApiException
from pprint import pprint
configuration = xenia_python_client_library.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.dutchanalytics.net/v1.1
configuration.host = "https://api.dutchanalytics.net/v1.1"
# Create an instance of the API class
api_instance = xenia_python_client_library.CoreApi(xenia_python_client_library.ApiClient(configuration))
project_name = 'project_name_example' # str | 

try:
    # Get details of a project
    api_response = api_instance.projects_get(project_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CoreApi->projects_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 

### Return type

[**ProjectList**](ProjectList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_list**
> list[ProjectList] projects_list()

List projects


### Description 
List all projects to which the user making request has access. The projects in organizations to which the user belongs are shown.

### Response Structure
A list of details of the projects
 - `id`: Unique identifier for the project (UUID) 

 - `name`: Name of the project 

 - `creation_date`: Time the project was created 

 - `organization_name`: Name of the organization in which the project is created

#### Response Examples
```
[
  {
    "id": "e988ddc0-3ef1-42d2-ab30-9f810a5e7063",
    "name": "project-1",
    "creation_date": "2018-10-26",
    "organization_name": "organization-1"
  },
  {
    "id": "e6a85cd7-94cc-44cf-9fa0-4b462d5a71ab",
    "name": "project-2",
    "creation_date": "2019-06-20",
    "organization_name": "organization-2"
  }
]
```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import xenia_python_client_library
from xenia_python_client_library.rest import ApiException
from pprint import pprint
configuration = xenia_python_client_library.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.dutchanalytics.net/v1.1
configuration.host = "https://api.dutchanalytics.net/v1.1"
# Create an instance of the API class
api_instance = xenia_python_client_library.CoreApi(xenia_python_client_library.ApiClient(configuration))

try:
    # List projects
    api_response = api_instance.projects_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CoreApi->projects_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ProjectList]**](ProjectList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_log_list**
> list[Logs] projects_log_list(project_name, data)

List logs for a project


### Description 
Get the logs of connectors, models, model versions, pipelines and pipeline inserts

### Required Parameters 
- `log_objects`: A dictionary containing the objects for which the logs need to be retrieved. It may contain zero or more of the following fields: 

    - `model_name`: name of a model 

    - `model_version`: a version name. If this field is present in the request, model_name must also be given. The versions are only meaningful in combination with the models they are defined for. 

    - `connector_name`: name of a connector 

    - `pipeline_name`: name of a pipeline 

    - `pipeline_object_name`: name of a pipeline object. If this field is present in the request, pipeline_name must also be given. The pipeline objects are only meaningful in combination with the pipelines they are defined in. 

    - `pipeline_trace_id`: a uuid obtained by a pipeline insert 


Any combination may be given in the request. For example, if only a model_name is provided, all logs for that model are returned. These logs can contain information from all the pipelines that model is referenced in.
If log_objects dictionary is empty, all logs for all objects in the project are returned.

### Optional Parameters 
 - `date`: Starting date for the logs. If it is not provided, the most recent logs are returned. It should be provided in year-month-day hour:minute:second format. 

 - `range`: Number of logs to be returned. It may be a positive or a negative value. If it is positive, logs starting from the date towards the present time are returned. Otherwise, logs towards the past are returned. The default value is -50. 

 - `object_id`: Internal id for the logs. Does not need to be provided when a range of logs is requested.

#### Request Examples 
```
{
  "log_objects": {
    "model_name": "model-1",
    "model_version": "v1"
  }
  "date": "2019-11-12 12:00:00"
}
```
 
```
{
  "log_objects": {
    "connector_name": "s3-connector",
    "pipeline_name": "pipeline-1"
  }
  "range": 100
}
```

### Response Structure 
A list of log details
 - `log`: Log message 

 - `date`: Time for the log
 
 The following fields can be returned on response if they are present for the log in the database. Any other additional field in the database is also returned.
 - `id`: Unique UUID of the log 

 - `connector_name`:  The connector which the log is related to 

 - `model_name`:  The model which the log is related to 

 - `model_version`:  The model version which the log is related to 

 - `pipeline_name`:  The pipeline which the log is related to 

 - `pipeline_object_name`: The pipeline object which the log is related to 

 - `pipeline_trace_id`:  The pipeline insert which the log is related to

#### Response Examples 
Logs for a specific model and version
```
[
  {
    "id": "5dcad12ba76a2c6e4331f180",
    "model_name": "model-1",
    "model_version": "v1",
    "date": "2019-11-11 15:15:07.050000",
    "log": "[Info] Prediction result 0.14981"
  },
  {
    "id": "5dcad12ba76a2c6e4331f181",
    "model_name": "model-1",
    "model_version": "v1",
    "pipeline_name": "pipeline-2",
    "pipeline_object_name": "model-1-v1-object",
    "pipeline_trace_id": "8bb6ed79-8606-4acf-acd2-90507130523c",
    "date": "2019-11-13 13:18:19.05100",
    "log": "[Error] Model call result (failed)"
  }
]
```
 
Logs for a specific pipeline
```
[
  {
    "id": "5dcad12ba76a2c6e4331f192",
    "model_name": "model-2",
    "model_version": "v2",
    "pipeline_name": "pipeline-1",
    "pipeline_object_name": "model-2-v2-object",
    "pipeline_trace_id": "4f75b10d-6012-47ab-ae68-cc9e69f35841",
    "date": "2019-11-13 12:03:00.56283",
    "log": "[Info] Model call result (success): 0.2316"
  },
  {
    "id": "5dcad12ba76a2c6e4331f193",
    "connector_name": "s3-connector",
    "pipeline_name": "pipeline-1",
    "pipeline_object_name": "s3-connector-object",
    "pipeline_trace_id": "4f75b10d-6012-47ab-ae68-cc9e69f35841",
    "date": "2019-11-13 12:03:20.02346",
    "log": "Could not connect to database: connection timed out"
  }
]
```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import xenia_python_client_library
from xenia_python_client_library.rest import ApiException
from pprint import pprint
configuration = xenia_python_client_library.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.dutchanalytics.net/v1.1
configuration.host = "https://api.dutchanalytics.net/v1.1"
# Create an instance of the API class
api_instance = xenia_python_client_library.CoreApi(xenia_python_client_library.ApiClient(configuration))
project_name = 'project_name_example' # str | 
data = xenia_python_client_library.LogsCreate() # LogsCreate | 

try:
    # List logs for a project
    api_response = api_instance.projects_log_list(project_name, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CoreApi->projects_log_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **data** | [**LogsCreate**](LogsCreate.md)|  | 

### Return type

[**list[Logs]**](Logs.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_user_list**
> list[OrganizationUserList] projects_user_list(project_name)

List the users in the organization of a project


### Description 
List users in an organization. The reason that this method is available is that users with **roles.create** permission should be able to get the ids of the users to be able to assign roles to them.
Therefore, only users who have roles.create permission are allowed to make this request.

### Response Structure 
List of details of users
 - `id`: Unique identifier for the user (UUID) 

 - `email`: Email of the user 

 - `name`: Name of the user 

 - `surname`: Surname of the user 


#### Response Examples
```
[
  {
    "id": "54977bc3-2c3b-4d8f-97c7-aff89a95bf21",
    "email": "user@example.com",
    "name": "user",
    "surname": "name"
  },
  {
    "id": "abe2e406-fae5-4bcf-a3bc-956d756e4ecb",
    "email": "user2@example.com",
    "name": "user",
    "surname": "name"
  }
]
```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import xenia_python_client_library
from xenia_python_client_library.rest import ApiException
from pprint import pprint
configuration = xenia_python_client_library.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.dutchanalytics.net/v1.1
configuration.host = "https://api.dutchanalytics.net/v1.1"
# Create an instance of the API class
api_instance = xenia_python_client_library.CoreApi(xenia_python_client_library.ApiClient(configuration))
project_name = 'project_name_example' # str | 

try:
    # List the users in the organization of a project
    api_response = api_instance.projects_user_list(project_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CoreApi->projects_user_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 

### Return type

[**list[OrganizationUserList]**](OrganizationUserList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **role_assignments_create**
> RoleAssignmentList role_assignments_create(project_name, data)

Assign a role to a user in a project


### Description 
Assign a role to a user in the scope of a project. This role can be assigned on either project level or on object level, which can be a model, credentials, connector or pipeline.
The user making the request must have appropriate permissions.

### Required Parameters 
 - `user_id`: Unique identifier for the user (UUID) 

 - `role`: Name of the role to be assigned to the user 


### Optional Parameters
 - `object_name`: Name of the object for which the role will be assigned 

 - `object_type`: Type of the object for which the role will be assigned. It can be project, model, credentials, connector or pipeline.

**object_name and object_type must be provided together. If neither of them is provided, the role is set on project level.**

#### Request Examples
Setting the role model-admin on project level for user with id 02b77d8f-b312-47ef-990f-4685a7ab9363
```
{
  "user_id": "02b77d8f-b312-47ef-990f-4685a7ab9363",
  "role": "model-admin"
}
```

Setting the role model-viewer on model-1 for user with id 02b77d8f-b312-47ef-990f-4685a7ab9363
```
{
  "user_id": "02b77d8f-b312-47ef-990f-4685a7ab9363",
  "role": "model-viewer",
  "object_name": "model-1",
  "object_type": "model"
}
```

### Response Structure 
Details of the created role assignment
 - `id`: Unique identifier for the role assignment (UUID) 

 - `user_id`: Unique identifier for the user (UUID) 

 - `role`: Name of the role assigned to the user 

 - `object_name`: Name of the object for which the role is assigned 

 - `object_type`: Type of the object for which the role is assigned. It can be project, model, credentials, connector or pipeline.


#### Response Examples
```
{
  "id": "e988ddc0-3ef1-42d2-ab30-9f810a5e7063",
  "user_id": "02b77d8f-b312-47ef-990f-4685a7ab9363",
  "role": "model-admin",
  "object_name": "project-1",
  "object_type": "project"
}
```

```
{
  "id": "e988ddc0-3ef1-42d2-ab30-9f810a5e7063",
  "user_id": "02b77d8f-b312-47ef-990f-4685a7ab9363",
  "role": "model-viewer",
  "object_name": "model-1",
  "object_type": "model"
}
```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import xenia_python_client_library
from xenia_python_client_library.rest import ApiException
from pprint import pprint
configuration = xenia_python_client_library.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.dutchanalytics.net/v1.1
configuration.host = "https://api.dutchanalytics.net/v1.1"
# Create an instance of the API class
api_instance = xenia_python_client_library.CoreApi(xenia_python_client_library.ApiClient(configuration))
project_name = 'project_name_example' # str | 
data = xenia_python_client_library.RoleAssignmentCreate() # RoleAssignmentCreate | 

try:
    # Assign a role to a user in a project
    api_response = api_instance.role_assignments_create(project_name, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CoreApi->role_assignments_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **data** | [**RoleAssignmentCreate**](RoleAssignmentCreate.md)|  | 

### Return type

[**RoleAssignmentList**](RoleAssignmentList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **role_assignments_delete**
> role_assignments_delete(project_name, id)

Delete a role from a user with the given role assignment id


### Description 
Delete a role of a user. The user making the request must have appropriate permissions. It is possible for a user to delete their own role if they have permissions to do so.
**The role project-admin of an organization admin cannot be deleted.**    


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import xenia_python_client_library
from xenia_python_client_library.rest import ApiException
from pprint import pprint
configuration = xenia_python_client_library.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.dutchanalytics.net/v1.1
configuration.host = "https://api.dutchanalytics.net/v1.1"
# Create an instance of the API class
api_instance = xenia_python_client_library.CoreApi(xenia_python_client_library.ApiClient(configuration))
project_name = 'project_name_example' # str | 
id = 'id_example' # str | 

try:
    # Delete a role from a user with the given role assignment id
    api_instance.role_assignments_delete(project_name, id)
except ApiException as e:
    print("Exception when calling CoreApi->role_assignments_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **role_assignments_get**
> RoleAssignmentList role_assignments_get(project_name, id)

Get details of a role assignment


### Description 
Get the details of a role assignment of a user. The user making the request must have appropriate permissions.

### Response Structure 
Details of the role assignment
 - `id`: Unique identifier for the role assignment (UUID) 

 - `user_id`: Unique identifier for the user (UUID) 

 - `role`: Name of the role assigned to the user 

 - `object_name`: Name of the object for which the role is assigned 

 - `object_type`: Type of the object for which the role is assigned. It can be project, model, credentials, connector or pipeline.

#### Response Examples 
```
{
  "id": "e988ddc0-3ef1-42d2-ab30-9f810a5e7063",
  "user_id": "02b77d8f-b312-47ef-990f-4685a7ab9363",
  "role": "model-viewer",
  "object_name": "model-1",
  "object_type": "model"
}
```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import xenia_python_client_library
from xenia_python_client_library.rest import ApiException
from pprint import pprint
configuration = xenia_python_client_library.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.dutchanalytics.net/v1.1
configuration.host = "https://api.dutchanalytics.net/v1.1"
# Create an instance of the API class
api_instance = xenia_python_client_library.CoreApi(xenia_python_client_library.ApiClient(configuration))
project_name = 'project_name_example' # str | 
id = 'id_example' # str | 

try:
    # Get details of a role assignment
    api_response = api_instance.role_assignments_get(project_name, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CoreApi->role_assignments_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **id** | **str**|  | 

### Return type

[**RoleAssignmentList**](RoleAssignmentList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **role_assignments_per_user_list**
> list[RoleAssignmentList] role_assignments_per_user_list(project_name, user_id)

List the roles assigned to a specific user in a project


### Description 
List the roles assigned to a user in the scope of a project. 

### Response Structure
 - `id`: Unique identifier for the role assignment (UUID) 

 - `user_id`: Unique identifier for the user (UUID) 

 - `role`: Name of the role assigned to the user 

 - `object_name`: Name of the object for which the role is assigned 

 - `object_type`: Type of the object for which the role is assigned. It can be project, model, credentials, connector or pipeline.

#### Response Examples
```
[
  {
    "id": "e988ddc0-3ef1-42d2-ab30-9f810a5e7063",
    "user_id": "02b77d8f-b312-47ef-990f-4685a7ab9363",
    "role": "model-viewer",
    "object_name": "model-1",
    "object_type": "model"
  },
  {
    "id": "13cf9dd7-7356-4797-b453-e0cb6b416162",
    "user_id": "02b77d8f-b312-47ef-990f-4685a7ab9363",
    "role": "connector-admin",
    "object_name": "connector-1",
    "object_type": "connector"
  }
]
```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import xenia_python_client_library
from xenia_python_client_library.rest import ApiException
from pprint import pprint
configuration = xenia_python_client_library.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.dutchanalytics.net/v1.1
configuration.host = "https://api.dutchanalytics.net/v1.1"
# Create an instance of the API class
api_instance = xenia_python_client_library.CoreApi(xenia_python_client_library.ApiClient(configuration))
project_name = 'project_name_example' # str | 
user_id = 'user_id_example' # str | 

try:
    # List the roles assigned to a specific user in a project
    api_response = api_instance.role_assignments_per_user_list(project_name, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CoreApi->role_assignments_per_user_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**list[RoleAssignmentList]**](RoleAssignmentList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **roles_create**
> RoleDetailList roles_create(project_name, data)

Create a custom role scoped in a project


### Description 
Create a custom role in the scope of a project. This role is not accessible from other projects. 
The user making the request must have appropriate permissions.

### Required Parameters 
 - `name`: Name of the role which will be created. It can only consist of lowercase letters, numbers and dashes (-), and must start with a lowercase letter. 

 - `permissions`: A list of permission names which the role will have. The list of available permissions can be obtained with */permissions* endpoint. 


#### Request Examples
```
{
  "name": "custom-model-editor-role",
  "permissions": [
    "models.list",
    "models.get",
    "models.delete"
  ]
}
```

### Response Structure 
Details of the created role
 - `name`: Name of the created role 

 - `permissions`: A list of permission names which the role has

#### Response Examples
```
{
  "name": "custom-model-editor-role",
  "permissions": [
    "models.list",
    "models.get",
    "models.delete"
  ]
}
```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import xenia_python_client_library
from xenia_python_client_library.rest import ApiException
from pprint import pprint
configuration = xenia_python_client_library.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.dutchanalytics.net/v1.1
configuration.host = "https://api.dutchanalytics.net/v1.1"
# Create an instance of the API class
api_instance = xenia_python_client_library.CoreApi(xenia_python_client_library.ApiClient(configuration))
project_name = 'project_name_example' # str | 
data = xenia_python_client_library.RoleCreate() # RoleCreate | 

try:
    # Create a custom role scoped in a project
    api_response = api_instance.roles_create(project_name, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CoreApi->roles_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **data** | [**RoleCreate**](RoleCreate.md)|  | 

### Return type

[**RoleDetailList**](RoleDetailList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **roles_delete**
> roles_delete(project_name, role_name)

Delete a role from a project


### Description 
Delete a role from a project. The user making the request must have appropriate permissions.
**Default roles cannot be deleted.**


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import xenia_python_client_library
from xenia_python_client_library.rest import ApiException
from pprint import pprint
configuration = xenia_python_client_library.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.dutchanalytics.net/v1.1
configuration.host = "https://api.dutchanalytics.net/v1.1"
# Create an instance of the API class
api_instance = xenia_python_client_library.CoreApi(xenia_python_client_library.ApiClient(configuration))
project_name = 'project_name_example' # str | 
role_name = 'role_name_example' # str | 

try:
    # Delete a role from a project
    api_instance.roles_delete(project_name, role_name)
except ApiException as e:
    print("Exception when calling CoreApi->roles_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **role_name** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **roles_get**
> RoleDetailList roles_get(project_name, role_name)

Get details of a role


### Description 
Get the details of a role. The user making the request must have appropriate permissions.

### Response Structure
Details of the role
 - `name`: Name of the role 

 - `permissions`: A list of permission names which the role has

#### Response Examples
```
{
  "name": "custom-model-editor-role",
  "permissions": [
    "models.list",
    "models.get",
    "models.delete"
  ]
}
```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import xenia_python_client_library
from xenia_python_client_library.rest import ApiException
from pprint import pprint
configuration = xenia_python_client_library.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.dutchanalytics.net/v1.1
configuration.host = "https://api.dutchanalytics.net/v1.1"
# Create an instance of the API class
api_instance = xenia_python_client_library.CoreApi(xenia_python_client_library.ApiClient(configuration))
project_name = 'project_name_example' # str | 
role_name = 'role_name_example' # str | 

try:
    # Get details of a role
    api_response = api_instance.roles_get(project_name, role_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CoreApi->roles_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **role_name** | **str**|  | 

### Return type

[**RoleDetailList**](RoleDetailList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **roles_list**
> list[RoleList] roles_list(project_name)

List the available roles in a project


### Description 
List the roles available in the scope of a project. This method only returns the names of the roles. Detailed information, such as which permissions each role contains, can be obtained with a call to get details of a single role.

### Response Structure
 - `name`: Name of the role

#### Response Examples
```
[
  {
    "name": "project-admin"
  },
  {
    "name": "project-editor"
  },
  {
    "name": "project-viewer"
  }
]
```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import xenia_python_client_library
from xenia_python_client_library.rest import ApiException
from pprint import pprint
configuration = xenia_python_client_library.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.dutchanalytics.net/v1.1
configuration.host = "https://api.dutchanalytics.net/v1.1"
# Create an instance of the API class
api_instance = xenia_python_client_library.CoreApi(xenia_python_client_library.ApiClient(configuration))
project_name = 'project_name_example' # str | 

try:
    # List the available roles in a project
    api_response = api_instance.roles_list(project_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CoreApi->roles_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 

### Return type

[**list[RoleList]**](RoleList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **roles_update**
> RoleDetailList roles_update(project_name, role_name, data)

Update a role in a project


### Description 
Update a role in a project. The user making the request must have appropriate permissions.
**Default roles cannot be updated.**

### Optional Parameters 
 - `name`: New name for the role. It can only consist of lowercase letters, numbers and dashes (-), and must start with a lowercase letter. 

 - `permissions`: A new list of permission names which the role will have. The previous permissions will be replaced with the given ones. The list of available permissions can be obtained with */permissions* endpoint. 


#### Request Examples
```
{
  "name": "new-model-editor-role"
}
```

```
{
  "permissions": [
    "models.list",
    "models.get"
  ]
}
```

### Response Structure 
Details of the created role
 - `name`: Name of the updated role 

 - `permissions`: A list of permission names which the role has

#### Response Examples
```
{
  "name": "new-model-editor-role",
  "permissions": [
    "models.list",
    "models.get"
  ]
}
```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import xenia_python_client_library
from xenia_python_client_library.rest import ApiException
from pprint import pprint
configuration = xenia_python_client_library.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.dutchanalytics.net/v1.1
configuration.host = "https://api.dutchanalytics.net/v1.1"
# Create an instance of the API class
api_instance = xenia_python_client_library.CoreApi(xenia_python_client_library.ApiClient(configuration))
project_name = 'project_name_example' # str | 
role_name = 'role_name_example' # str | 
data = xenia_python_client_library.RoleUpdate() # RoleUpdate | 

try:
    # Update a role in a project
    api_response = api_instance.roles_update(project_name, role_name, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CoreApi->roles_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **role_name** | **str**|  | 
 **data** | [**RoleUpdate**](RoleUpdate.md)|  | 

### Return type

[**RoleDetailList**](RoleDetailList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **service_status**
> Status service_status()

Service status


### Description
Request the API status. It can be used to determine whether the API is online. You do not have to be authenticated to access this method.

### Response Structure
- `status`: API status, either ok or fail. The database connection is tested at each status request, to make sure that the API is online.

#### Response Examples
```	
{
  "status": "ok"
}
```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import xenia_python_client_library
from xenia_python_client_library.rest import ApiException
from pprint import pprint
configuration = xenia_python_client_library.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.dutchanalytics.net/v1.1
configuration.host = "https://api.dutchanalytics.net/v1.1"
# Create an instance of the API class
api_instance = xenia_python_client_library.CoreApi(xenia_python_client_library.ApiClient(configuration))

try:
    # Service status
    api_response = api_instance.service_status()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CoreApi->service_status: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Status**](Status.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **service_users_create**
> ServiceUserDetail service_users_create(project_name, data)

Create a new service user


### Description 
Create a new service user. A unique email is generated for the service user. Additionally, a token for this service user is generated. This token can be used to authorize requests sent to our API. 

The token is **ONLY** returned on creation and will not be accessible afterwards.

### Optional Parameters
- `name`: Name of the service user 


#### Request Examples 
```
{
  "name": "service-user-1"
}
```

### Response Structure 
Details of the created service user
 - `id`: Unique identifier for the service user (UUID) 

 - `email`: Email of the service user  

 - `token`: The API token for the created service user  

 - `name`: Name of the service user 

 - `creation_date`: Date when the service user was created

#### Response Examples 
```
{
  "id": "13a9ba27-6888-4528-826e-8e1002eab13d",
  "email": "13a9ba27-6888-4528-826e-8e1002eab13d.project1@serviceuser.xenia.dutchanalytics.net",
  "token": "e962d9190348af7fa8d233d75cff7385b4335f81",
  "name": "service-user-1",
  "creation_date": "2020-03-24T09:16:27.504+00:00"
}
```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import xenia_python_client_library
from xenia_python_client_library.rest import ApiException
from pprint import pprint
configuration = xenia_python_client_library.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.dutchanalytics.net/v1.1
configuration.host = "https://api.dutchanalytics.net/v1.1"
# Create an instance of the API class
api_instance = xenia_python_client_library.CoreApi(xenia_python_client_library.ApiClient(configuration))
project_name = 'project_name_example' # str | 
data = xenia_python_client_library.ServiceUserCreate() # ServiceUserCreate | 

try:
    # Create a new service user
    api_response = api_instance.service_users_create(project_name, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CoreApi->service_users_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **data** | [**ServiceUserCreate**](ServiceUserCreate.md)|  | 

### Return type

[**ServiceUserDetail**](ServiceUserDetail.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **service_users_delete**
> service_users_delete(project_name, service_user_id)

Delete service user


### Description 
Delete a service user from a project


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import xenia_python_client_library
from xenia_python_client_library.rest import ApiException
from pprint import pprint
configuration = xenia_python_client_library.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.dutchanalytics.net/v1.1
configuration.host = "https://api.dutchanalytics.net/v1.1"
# Create an instance of the API class
api_instance = xenia_python_client_library.CoreApi(xenia_python_client_library.ApiClient(configuration))
project_name = 'project_name_example' # str | 
service_user_id = 'service_user_id_example' # str | 

try:
    # Delete service user
    api_instance.service_users_delete(project_name, service_user_id)
except ApiException as e:
    print("Exception when calling CoreApi->service_users_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **service_user_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **service_users_get**
> ServiceUserList service_users_get(project_name, service_user_id)

Retrieve details of a service user


### Description 
Retrieve details of a service user

### Response Structure 
Details of the service user
 - `id`: Unique identifier for the service user (UUID) 

 - `email`: Email of the service user  

 - `name`: Name of the service user 

 - `creation_date`: Date when the service user was created

#### Response Examples 
```
{
  "id": "13a9ba27-6888-4528-826e-8e1002eab13d",
  "email": "13a9ba27-6888-4528-826e-8e1002eab13d.project1@serviceuser.xenia.dutchanalytics.net",
  "name": "new-service-user-name",
  "creation_date": "2020-03-26T12:18:43.123+00:00"
}
```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import xenia_python_client_library
from xenia_python_client_library.rest import ApiException
from pprint import pprint
configuration = xenia_python_client_library.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.dutchanalytics.net/v1.1
configuration.host = "https://api.dutchanalytics.net/v1.1"
# Create an instance of the API class
api_instance = xenia_python_client_library.CoreApi(xenia_python_client_library.ApiClient(configuration))
project_name = 'project_name_example' # str | 
service_user_id = 'service_user_id_example' # str | 

try:
    # Retrieve details of a service user
    api_response = api_instance.service_users_get(project_name, service_user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CoreApi->service_users_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **service_user_id** | **str**|  | 

### Return type

[**ServiceUserList**](ServiceUserList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **service_users_list**
> list[ServiceUserList] service_users_list(project_name)

List service users


### Description 
List service users defined in a project

### Response Structure 
List of details of the service users:
 - `id`: Unique identifier for the service user (UUID) 

 - `email`: Email of the service user 

 - `name`: Name of the service user 

 - `creation_date`: Date when the service user was created

#### Response Examples 
```
[
  {
    "id": "537bca64-5ab6-43eb-a7ef-1638bc30b6ed",
    "email": "537bca64-5ab6-43eb-a7ef-1638bc30b6ed.project1@serviceuser.xenia.dutchanalytics.net",
    "name": "service-user-1",
    "creation_date": "2020-03-24T09:16:27.504+00:00"
  },
  {
    "id": "13a9ba27-6888-4528-826e-8e1002eab13d",
    "email": "13a9ba27-6888-4528-826e-8e1002eab13d.project1@serviceuser.xenia.dutchanalytics.net",
    "name": "service-user-2",
    "creation_date": "2020-03-26T12:18:43.123+00:00"
  }
]
```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import xenia_python_client_library
from xenia_python_client_library.rest import ApiException
from pprint import pprint
configuration = xenia_python_client_library.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.dutchanalytics.net/v1.1
configuration.host = "https://api.dutchanalytics.net/v1.1"
# Create an instance of the API class
api_instance = xenia_python_client_library.CoreApi(xenia_python_client_library.ApiClient(configuration))
project_name = 'project_name_example' # str | 

try:
    # List service users
    api_response = api_instance.service_users_list(project_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CoreApi->service_users_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 

### Return type

[**list[ServiceUserList]**](ServiceUserList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **service_users_token**
> ServiceUserTokenList service_users_token(project_name, service_user_id, data)

Reset the token of a service user


### Description 
Reset the token of a service user. The old token will be deleted and a new one will be created for the service user. No data should be sent in the body of the request.

### Response Structure 
Details of the new token for the service user
 - `token`: The new API token for the service user

#### Response Examples
```
{
  "token": "e962d9190348af7fa8d233d75cff7385b4335f81"
}
```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import xenia_python_client_library
from xenia_python_client_library.rest import ApiException
from pprint import pprint
configuration = xenia_python_client_library.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.dutchanalytics.net/v1.1
configuration.host = "https://api.dutchanalytics.net/v1.1"
# Create an instance of the API class
api_instance = xenia_python_client_library.CoreApi(xenia_python_client_library.ApiClient(configuration))
project_name = 'project_name_example' # str | 
service_user_id = 'service_user_id_example' # str | 
data = None # object | 

try:
    # Reset the token of a service user
    api_response = api_instance.service_users_token(project_name, service_user_id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CoreApi->service_users_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **service_user_id** | **str**|  | 
 **data** | **object**|  | 

### Return type

[**ServiceUserTokenList**](ServiceUserTokenList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **service_users_update**
> ServiceUserList service_users_update(project_name, service_user_id, data)

Update service user details

 
### Description
Update the name of a service user

### Optional Parameters
- `name`: Name of the service user 


#### Request Examples 

```
{
  "name": "new-service-user-name",
}
```

### Response Structure 
Details of the updated service user
 - `id`: Unique identifier for the service user (UUID) 

 - `email`: Email of the service user  

 - `name`: Name of the service user 

 - `creation_date`: Date when the service user was created

#### Response Examples 
```
{
  "id": "13a9ba27-6888-4528-826e-8e1002eab13d",
  "email": "13a9ba27-6888-4528-826e-8e1002eab13d.project1@serviceuser.xenia.dutchanalytics.net",
  "name": "new-service-user-name",
  "creation_date": "2020-03-26T12:18:43.123+00:00"
}
```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import xenia_python_client_library
from xenia_python_client_library.rest import ApiException
from pprint import pprint
configuration = xenia_python_client_library.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.dutchanalytics.net/v1.1
configuration.host = "https://api.dutchanalytics.net/v1.1"
# Create an instance of the API class
api_instance = xenia_python_client_library.CoreApi(xenia_python_client_library.ApiClient(configuration))
project_name = 'project_name_example' # str | 
service_user_id = 'service_user_id_example' # str | 
data = xenia_python_client_library.ServiceUserCreate() # ServiceUserCreate | 

try:
    # Update service user details
    api_response = api_instance.service_users_update(project_name, service_user_id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CoreApi->service_users_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**|  | 
 **service_user_id** | **str**|  | 
 **data** | [**ServiceUserCreate**](ServiceUserCreate.md)|  | 

### Return type

[**ServiceUserList**](ServiceUserList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subscriptions_list**
> list[SubscriptionList] subscriptions_list()

List subscriptions


### Description 
List all available subscriptions which are available for organizations

### Response Structure
A list of details of the subscriptions
 - `id`: Unique identifier for the subscription (UUID) 

 - `name`: Name of the subscription 

 - `max_projects`: The number of maximum projects allowed to be created with this type of subscription 

 - `max_users`: The number of maximum users allowed to be created with this type of subscription 

 - `agreement`: Link to the Xenia Free SaaS Services Agreement document 

 - `terms_conditions`: Link to the the Xenia SaaS Terms & Conditions document 



### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import xenia_python_client_library
from xenia_python_client_library.rest import ApiException
from pprint import pprint
configuration = xenia_python_client_library.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.dutchanalytics.net/v1.1
configuration.host = "https://api.dutchanalytics.net/v1.1"
# Create an instance of the API class
api_instance = xenia_python_client_library.CoreApi(xenia_python_client_library.ApiClient(configuration))

try:
    # List subscriptions
    api_response = api_instance.subscriptions_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CoreApi->subscriptions_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[SubscriptionList]**](SubscriptionList.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_create**
> UserPendingDetail user_create(data)

Create a new user


### Description 
Create a new user with the given details - email, password, name and surname. After creation, an email is send to the email address to activate the acount.
A user is required to accept the terms and conditions.

The password needs to meet the following requirements:
- At least 8 characters long
- At least one capital and one lowercase letter
- At least one number
- At least one of the following symbols: !#$%&')(*+,./:;"<=>?[@]^_`{|}~-" 

### Required Parameters
- `email`: Email of the user. This is a unique field. 

- `password`: Password of the user 

- `terms_conditions`: Boolean field. Pass True to accept terms and conditions. 


### Optional Parameters
- `name`: Name of the user 

- `surname`: Surname of the user

#### Request Examples 
```
{
  "email": "test@example.com",
  "password": "secret-password",
  "name": "User name",
  "surname": "User surname",
  "terms_conditions": true
}
```

```
{
  "email": "test@example.com",
  "password": "secret-password",
  "terms_conditions": true
}
```

### Response Structure 
Details of the created user
 - `email`: Email of the user 

 - `name`: Name of the user 

 - `surname`: Surname of the user 

#### Response Examples 
```
{
  "email": "test@example.com",
  "name": "User name",
  "surname": "User surname"
}
```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import xenia_python_client_library
from xenia_python_client_library.rest import ApiException
from pprint import pprint
configuration = xenia_python_client_library.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.dutchanalytics.net/v1.1
configuration.host = "https://api.dutchanalytics.net/v1.1"
# Create an instance of the API class
api_instance = xenia_python_client_library.CoreApi(xenia_python_client_library.ApiClient(configuration))
data = xenia_python_client_library.UserPendingCreate() # UserPendingCreate | 

try:
    # Create a new user
    api_response = api_instance.user_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CoreApi->user_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**UserPendingCreate**](UserPendingCreate.md)|  | 

### Return type

[**UserPendingDetail**](UserPendingDetail.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_delete**
> user_delete()

Delete user


### Description 
Delete the user that makes the request


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import xenia_python_client_library
from xenia_python_client_library.rest import ApiException
from pprint import pprint
configuration = xenia_python_client_library.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.dutchanalytics.net/v1.1
configuration.host = "https://api.dutchanalytics.net/v1.1"
# Create an instance of the API class
api_instance = xenia_python_client_library.CoreApi(xenia_python_client_library.ApiClient(configuration))

try:
    # Delete user
    api_instance.user_delete()
except ApiException as e:
    print("Exception when calling CoreApi->user_delete: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_get**
> UserDetail user_get()

Get user details


### Description 
Get the details of the user that makes the request

### Response Structure 
Details of the user:
 - `id`: Unique identifier for the user (UUID) 

 - `email`: Email of the user 

 - `name`: Name of the user 

 - `surname`: Surname of the user 

 - `registration_date`: Date when the user was registered

#### Response Examples 
```
{
  "id": "4740a13a-70ae-4b7a-a461-8231eb2c0594",
  "email": "test@example.com",
  "name": "User name",
  "surname": "User surname",
  "registration_date": "2020-01-10 10:06:25.632+00:00"
}
```


### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import xenia_python_client_library
from xenia_python_client_library.rest import ApiException
from pprint import pprint
configuration = xenia_python_client_library.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to https://api.dutchanalytics.net/v1.1
configuration.host = "https://api.dutchanalytics.net/v1.1"
# Create an instance of the API class
api_instance = xenia_python_client_library.CoreApi(xenia_python_client_library.ApiClient(configuration))

try:
    # Get user details
    api_response = api_instance.user_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CoreApi->user_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**UserDetail**](UserDetail.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

