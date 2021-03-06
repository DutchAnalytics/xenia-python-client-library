# ! DEPRECATED
This repository contains an old version of the Python client library, which is no longer officially supported. Click [here](https://github.com/UbiOps/client-library-python) for the latest version.

***

# xenia-python-client-library
Python Client Library to interact with the Xenia API.

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: v2.1
- Package version: 2.0.1
- Build package: org.openapitools.codegen.languages.PythonClientCodegen
For more information, please visit [https://docs.dutchanalytics.net](https://docs.dutchanalytics.net)

## Requirements.

Python 3.5+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/DutchAnalytics/xenia-python-client-library.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/DutchAnalytics/xenia-python-client-library.git`)

Then import the package:
```python
import xenia_python_client_library
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import xenia_python_client_library
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

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

# Defining host is optional and default to https://api.dutchanalytics.net/v2.1
configuration.host = "https://api.dutchanalytics.net/v2.1"
# Enter a context with an instance of the API client
with xenia_python_client_library.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = xenia_python_client_library.CoreApi(api_client)
    project_name = 'project_name_example' # str | 
model_name = 'model_name_example' # str | 
version = 'version_example' # str | 
data = None # object | 

    try:
        # Retrieve multiple batch model request results
        api_response = api_instance.batch_model_requests_batch_collect(project_name, model_name, version, data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CoreApi->batch_model_requests_batch_collect: %s\n" % e)
    
```

## Documentation for API Endpoints

All URIs are relative to *https://api.dutchanalytics.net/v2.1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*CoreApi* | [**batch_model_requests_batch_collect**](docs/CoreApi.md#batch_model_requests_batch_collect) | **POST** /projects/{project_name}/models/{model_name}/versions/{version}/request-batch-collect | Retrieve multiple batch model request results
*CoreApi* | [**batch_model_requests_batch_delete**](docs/CoreApi.md#batch_model_requests_batch_delete) | **POST** /projects/{project_name}/models/{model_name}/versions/{version}/request-batch-delete | Delete multiple batch model requests
*CoreApi* | [**batch_model_requests_create**](docs/CoreApi.md#batch_model_requests_create) | **POST** /projects/{project_name}/models/{model_name}/versions/{version}/request-batch | Create batch model requests
*CoreApi* | [**batch_model_requests_delete**](docs/CoreApi.md#batch_model_requests_delete) | **DELETE** /projects/{project_name}/models/{model_name}/versions/{version}/request-batch/{request_id} | Delete batch model requests
*CoreApi* | [**batch_model_requests_get**](docs/CoreApi.md#batch_model_requests_get) | **GET** /projects/{project_name}/models/{model_name}/versions/{version}/request-batch/{request_id} | Get batch model request
*CoreApi* | [**batch_model_requests_list**](docs/CoreApi.md#batch_model_requests_list) | **GET** /projects/{project_name}/models/{model_name}/versions/{version}/request-batch | List batch model requests
*CoreApi* | [**batch_pipeline_request_delete**](docs/CoreApi.md#batch_pipeline_request_delete) | **DELETE** /projects/{project_name}/pipelines/{pipeline_name}/request-batch/{pipeline_request_id} | Delete batch pipeline requests
*CoreApi* | [**batch_pipeline_request_get**](docs/CoreApi.md#batch_pipeline_request_get) | **GET** /projects/{project_name}/pipelines/{pipeline_name}/request-batch/{pipeline_request_id} | Get batch pipeline request
*CoreApi* | [**batch_pipeline_requests_batch_collect**](docs/CoreApi.md#batch_pipeline_requests_batch_collect) | **POST** /projects/{project_name}/pipelines/{pipeline_name}/request-batch-collect | Retrieve multiple batch pipeline request results
*CoreApi* | [**batch_pipeline_requests_batch_delete**](docs/CoreApi.md#batch_pipeline_requests_batch_delete) | **POST** /projects/{project_name}/pipelines/{pipeline_name}/request-batch-delete | Delete multiple batch pipeline requests
*CoreApi* | [**batch_pipeline_requests_create**](docs/CoreApi.md#batch_pipeline_requests_create) | **POST** /projects/{project_name}/pipelines/{pipeline_name}/request-batch | Create batch pipeline requests
*CoreApi* | [**batch_pipeline_requests_list**](docs/CoreApi.md#batch_pipeline_requests_list) | **GET** /projects/{project_name}/pipelines/{pipeline_name}/request-batch | List batch pipeline requests
*CoreApi* | [**blobs_create**](docs/CoreApi.md#blobs_create) | **POST** /projects/{project_name}/blobs | Upload a blob
*CoreApi* | [**blobs_delete**](docs/CoreApi.md#blobs_delete) | **DELETE** /projects/{project_name}/blobs/{blob_id} | Delete a blob
*CoreApi* | [**blobs_get**](docs/CoreApi.md#blobs_get) | **GET** /projects/{project_name}/blobs/{blob_id} | Get a blob
*CoreApi* | [**blobs_list**](docs/CoreApi.md#blobs_list) | **GET** /projects/{project_name}/blobs | List blobs
*CoreApi* | [**configurations_list**](docs/CoreApi.md#configurations_list) | **GET** /config/connectors | List available connector configurations
*CoreApi* | [**connectors_create**](docs/CoreApi.md#connectors_create) | **POST** /projects/{project_name}/connectors | Create a connector
*CoreApi* | [**connectors_delete**](docs/CoreApi.md#connectors_delete) | **DELETE** /projects/{project_name}/connectors/{connector_name} | Delete connectors
*CoreApi* | [**connectors_get**](docs/CoreApi.md#connectors_get) | **GET** /projects/{project_name}/connectors/{connector_name} | Get connectors
*CoreApi* | [**connectors_list**](docs/CoreApi.md#connectors_list) | **GET** /projects/{project_name}/connectors | List connectors
*CoreApi* | [**connectors_update**](docs/CoreApi.md#connectors_update) | **PATCH** /projects/{project_name}/connectors/{connector_name} | Update connectors
*CoreApi* | [**credentials_create**](docs/CoreApi.md#credentials_create) | **POST** /projects/{project_name}/credentials | Create credentials
*CoreApi* | [**credentials_delete**](docs/CoreApi.md#credentials_delete) | **DELETE** /projects/{project_name}/credentials/{credentials_name} | Delete credentials
*CoreApi* | [**credentials_get**](docs/CoreApi.md#credentials_get) | **GET** /projects/{project_name}/credentials/{credentials_name} | Get credentials
*CoreApi* | [**credentials_list**](docs/CoreApi.md#credentials_list) | **GET** /projects/{project_name}/credentials | List credentials
*CoreApi* | [**credentials_update**](docs/CoreApi.md#credentials_update) | **PATCH** /projects/{project_name}/credentials/{credentials_name} | Update credentials
*CoreApi* | [**metrics_get**](docs/CoreApi.md#metrics_get) | **GET** /projects/{project_name}/metrics/{metric} | Get metrics
*CoreApi* | [**model_environment_variables_create**](docs/CoreApi.md#model_environment_variables_create) | **POST** /projects/{project_name}/models/{model_name}/environment-variables | Create model environment variable
*CoreApi* | [**model_environment_variables_delete**](docs/CoreApi.md#model_environment_variables_delete) | **DELETE** /projects/{project_name}/models/{model_name}/environment-variables/{id} | Delete model environment variable
*CoreApi* | [**model_environment_variables_get**](docs/CoreApi.md#model_environment_variables_get) | **GET** /projects/{project_name}/models/{model_name}/environment-variables/{id} | Get model environment variable
*CoreApi* | [**model_environment_variables_list**](docs/CoreApi.md#model_environment_variables_list) | **GET** /projects/{project_name}/models/{model_name}/environment-variables | List model environment variables
*CoreApi* | [**model_environment_variables_update**](docs/CoreApi.md#model_environment_variables_update) | **PATCH** /projects/{project_name}/models/{model_name}/environment-variables/{id} | Update model environment variable
*CoreApi* | [**model_requests_create**](docs/CoreApi.md#model_requests_create) | **POST** /projects/{project_name}/models/{model_name}/versions/{version}/request | Create model requests
*CoreApi* | [**model_version_environment_variables_create**](docs/CoreApi.md#model_version_environment_variables_create) | **POST** /projects/{project_name}/models/{model_name}/versions/{version}/environment-variables | Create model version environment variable
*CoreApi* | [**model_version_environment_variables_delete**](docs/CoreApi.md#model_version_environment_variables_delete) | **DELETE** /projects/{project_name}/models/{model_name}/versions/{version}/environment-variables/{id} | Delete model version environment variable
*CoreApi* | [**model_version_environment_variables_get**](docs/CoreApi.md#model_version_environment_variables_get) | **GET** /projects/{project_name}/models/{model_name}/versions/{version}/environment-variables/{id} | Get model version environment variable
*CoreApi* | [**model_version_environment_variables_list**](docs/CoreApi.md#model_version_environment_variables_list) | **GET** /projects/{project_name}/models/{model_name}/versions/{version}/environment-variables | List model version environment variables
*CoreApi* | [**model_version_environment_variables_update**](docs/CoreApi.md#model_version_environment_variables_update) | **PATCH** /projects/{project_name}/models/{model_name}/versions/{version}/environment-variables/{id} | Update model version environment variable
*CoreApi* | [**model_versions_create**](docs/CoreApi.md#model_versions_create) | **POST** /projects/{project_name}/models/{model_name}/versions | Create model versions
*CoreApi* | [**model_versions_delete**](docs/CoreApi.md#model_versions_delete) | **DELETE** /projects/{project_name}/models/{model_name}/versions/{version} | Delete model version
*CoreApi* | [**model_versions_file_download**](docs/CoreApi.md#model_versions_file_download) | **GET** /projects/{project_name}/models/{model_name}/versions/{version}/download | Download model files
*CoreApi* | [**model_versions_file_upload**](docs/CoreApi.md#model_versions_file_upload) | **PUT** /projects/{project_name}/models/{model_name}/versions/{version}/upload | Upload model files
*CoreApi* | [**model_versions_get**](docs/CoreApi.md#model_versions_get) | **GET** /projects/{project_name}/models/{model_name}/versions/{version} | Get model version
*CoreApi* | [**model_versions_list**](docs/CoreApi.md#model_versions_list) | **GET** /projects/{project_name}/models/{model_name}/versions | List model versions
*CoreApi* | [**model_versions_update**](docs/CoreApi.md#model_versions_update) | **PATCH** /projects/{project_name}/models/{model_name}/versions/{version} | Update model version
*CoreApi* | [**models_create**](docs/CoreApi.md#models_create) | **POST** /projects/{project_name}/models | Create a model
*CoreApi* | [**models_delete**](docs/CoreApi.md#models_delete) | **DELETE** /projects/{project_name}/models/{model_name} | Delete a model
*CoreApi* | [**models_get**](docs/CoreApi.md#models_get) | **GET** /projects/{project_name}/models/{model_name} | Get details of model
*CoreApi* | [**models_list**](docs/CoreApi.md#models_list) | **GET** /projects/{project_name}/models | List models in project
*CoreApi* | [**models_update**](docs/CoreApi.md#models_update) | **PATCH** /projects/{project_name}/models/{model_name} | Update a model
*CoreApi* | [**organization_invites_delete**](docs/CoreApi.md#organization_invites_delete) | **DELETE** /organizations/{organization_name}/invites/{invite_id} | Delete an organization invitation of a user
*CoreApi* | [**organization_invites_get**](docs/CoreApi.md#organization_invites_get) | **GET** /organizations/{organization_name}/invites/{invite_id} | Get details of an organization invitation of a user
*CoreApi* | [**organization_invites_list**](docs/CoreApi.md#organization_invites_list) | **GET** /organizations/{organization_name}/invites | List the users invited to an organization
*CoreApi* | [**organization_subscriptions_list**](docs/CoreApi.md#organization_subscriptions_list) | **GET** /organizations/{organization_name}/subscriptions | List subscriptions for an organizations
*CoreApi* | [**organization_usage_details_get**](docs/CoreApi.md#organization_usage_details_get) | **GET** /organizations/{organization_name}/usage/details | Get resource usage details
*CoreApi* | [**organization_usage_get**](docs/CoreApi.md#organization_usage_get) | **GET** /organizations/{organization_name}/usage | Get resource usage
*CoreApi* | [**organization_users_create**](docs/CoreApi.md#organization_users_create) | **POST** /organizations/{organization_name}/users | Add a user to an organization
*CoreApi* | [**organization_users_delete**](docs/CoreApi.md#organization_users_delete) | **DELETE** /organizations/{organization_name}/users/{user_id} | Delete a user from an organization
*CoreApi* | [**organization_users_get**](docs/CoreApi.md#organization_users_get) | **GET** /organizations/{organization_name}/users/{user_id} | Get details of a user in an organization
*CoreApi* | [**organization_users_list**](docs/CoreApi.md#organization_users_list) | **GET** /organizations/{organization_name}/users | List the users in an organization
*CoreApi* | [**organization_users_update**](docs/CoreApi.md#organization_users_update) | **PATCH** /organizations/{organization_name}/users/{user_id} | Update details of a user in an organization
*CoreApi* | [**organizations_create**](docs/CoreApi.md#organizations_create) | **POST** /organizations | Create organizations
*CoreApi* | [**organizations_get**](docs/CoreApi.md#organizations_get) | **GET** /organizations/{organization_name} | Get details of an organization
*CoreApi* | [**organizations_list**](docs/CoreApi.md#organizations_list) | **GET** /organizations | List organizations
*CoreApi* | [**organizations_resource_usage**](docs/CoreApi.md#organizations_resource_usage) | **GET** /organizations/{organization_name}/resources | List resource usage
*CoreApi* | [**organizations_update**](docs/CoreApi.md#organizations_update) | **PATCH** /organizations/{organization_name} | Update details of an organization
*CoreApi* | [**permissions_list**](docs/CoreApi.md#permissions_list) | **GET** /permissions | List the available permissions
*CoreApi* | [**pipeline_object_attachments_create**](docs/CoreApi.md#pipeline_object_attachments_create) | **POST** /projects/{project_name}/pipelines/{pipeline_name}/attachments | Create object attachments
*CoreApi* | [**pipeline_object_attachments_delete**](docs/CoreApi.md#pipeline_object_attachments_delete) | **DELETE** /projects/{project_name}/pipelines/{pipeline_name}/objects/{source_name}/attachments/{destination_name} | Delete attachment of a source and destination object
*CoreApi* | [**pipeline_object_attachments_get**](docs/CoreApi.md#pipeline_object_attachments_get) | **GET** /projects/{project_name}/pipelines/{pipeline_name}/objects/{source_name}/attachments/{destination_name} | Get an attachment of a source and destination object
*CoreApi* | [**pipeline_object_attachments_list**](docs/CoreApi.md#pipeline_object_attachments_list) | **GET** /projects/{project_name}/pipelines/{pipeline_name}/attachments | List object attachments
*CoreApi* | [**pipeline_object_attachments_source_get**](docs/CoreApi.md#pipeline_object_attachments_source_get) | **GET** /projects/{project_name}/pipelines/{pipeline_name}/objects/{source_name}/attachments/ | List the attachments of a source object
*CoreApi* | [**pipeline_object_environment_variables_list**](docs/CoreApi.md#pipeline_object_environment_variables_list) | **GET** /projects/{project_name}/pipelines/{pipeline_name}/objects/{name}/environment-variables | List pipeline object environment variables
*CoreApi* | [**pipeline_objects_create**](docs/CoreApi.md#pipeline_objects_create) | **POST** /projects/{project_name}/pipelines/{pipeline_name}/objects | Add an object to a pipeline
*CoreApi* | [**pipeline_objects_delete**](docs/CoreApi.md#pipeline_objects_delete) | **DELETE** /projects/{project_name}/pipelines/{pipeline_name}/objects/{name} | Delete object from pipeline
*CoreApi* | [**pipeline_objects_get**](docs/CoreApi.md#pipeline_objects_get) | **GET** /projects/{project_name}/pipelines/{pipeline_name}/objects/{name} | Get an object in a pipeline
*CoreApi* | [**pipeline_objects_list**](docs/CoreApi.md#pipeline_objects_list) | **GET** /projects/{project_name}/pipelines/{pipeline_name}/objects | List objects in a pipeline
*CoreApi* | [**pipeline_objects_update**](docs/CoreApi.md#pipeline_objects_update) | **PATCH** /projects/{project_name}/pipelines/{pipeline_name}/objects/{name} | Update an object in a pipeline
*CoreApi* | [**pipelines_create**](docs/CoreApi.md#pipelines_create) | **POST** /projects/{project_name}/pipelines | Create pipelines
*CoreApi* | [**pipelines_delete**](docs/CoreApi.md#pipelines_delete) | **DELETE** /projects/{project_name}/pipelines/{pipeline_name} | Delete pipeline
*CoreApi* | [**pipelines_get**](docs/CoreApi.md#pipelines_get) | **GET** /projects/{project_name}/pipelines/{pipeline_name} | Get pipeline
*CoreApi* | [**pipelines_list**](docs/CoreApi.md#pipelines_list) | **GET** /projects/{project_name}/pipelines | List pipelines
*CoreApi* | [**pipelines_request**](docs/CoreApi.md#pipelines_request) | **POST** /projects/{project_name}/pipelines/{pipeline_name}/request | Make a request to a pipeline
*CoreApi* | [**pipelines_update**](docs/CoreApi.md#pipelines_update) | **PATCH** /projects/{project_name}/pipelines/{pipeline_name} | Update pipeline
*CoreApi* | [**project_environment_variables_create**](docs/CoreApi.md#project_environment_variables_create) | **POST** /projects/{project_name}/environment-variables | Create project environment variable
*CoreApi* | [**project_environment_variables_delete**](docs/CoreApi.md#project_environment_variables_delete) | **DELETE** /projects/{project_name}/environment-variables/{id} | Delete project environment variable
*CoreApi* | [**project_environment_variables_get**](docs/CoreApi.md#project_environment_variables_get) | **GET** /projects/{project_name}/environment-variables/{id} | Get project environment variable
*CoreApi* | [**project_environment_variables_list**](docs/CoreApi.md#project_environment_variables_list) | **GET** /projects/{project_name}/environment-variables | List project environment variables
*CoreApi* | [**project_environment_variables_update**](docs/CoreApi.md#project_environment_variables_update) | **PATCH** /projects/{project_name}/environment-variables/{id} | Update project environment variable
*CoreApi* | [**project_usage_get**](docs/CoreApi.md#project_usage_get) | **GET** /projects/{project_name}/usage | Get resource usage
*CoreApi* | [**projects_create**](docs/CoreApi.md#projects_create) | **POST** /projects | Create projects
*CoreApi* | [**projects_delete**](docs/CoreApi.md#projects_delete) | **DELETE** /projects/{project_name} | Delete a project
*CoreApi* | [**projects_get**](docs/CoreApi.md#projects_get) | **GET** /projects/{project_name} | Get details of a project
*CoreApi* | [**projects_list**](docs/CoreApi.md#projects_list) | **GET** /projects | List projects
*CoreApi* | [**projects_log_list**](docs/CoreApi.md#projects_log_list) | **POST** /projects/{project_name}/logs | List logs for a project
*CoreApi* | [**projects_update**](docs/CoreApi.md#projects_update) | **PATCH** /projects/{project_name} | Update a project
*CoreApi* | [**projects_user_list**](docs/CoreApi.md#projects_user_list) | **GET** /projects/{project_name}/users | List the users in the organization of a project
*CoreApi* | [**role_assignments_create**](docs/CoreApi.md#role_assignments_create) | **POST** /projects/{project_name}/role-assignments | Assign a role to a user in a project
*CoreApi* | [**role_assignments_delete**](docs/CoreApi.md#role_assignments_delete) | **DELETE** /projects/{project_name}/role-assignments/{id} | Delete a role from a user with the given role assignment id
*CoreApi* | [**role_assignments_get**](docs/CoreApi.md#role_assignments_get) | **GET** /projects/{project_name}/role-assignments/{id} | Get details of a role assignment
*CoreApi* | [**role_assignments_per_user_list**](docs/CoreApi.md#role_assignments_per_user_list) | **GET** /projects/{project_name}/users/{user_id}/role-assignments | List the roles assigned to a specific user in a project
*CoreApi* | [**roles_create**](docs/CoreApi.md#roles_create) | **POST** /projects/{project_name}/roles | Create a custom role scoped in a project
*CoreApi* | [**roles_delete**](docs/CoreApi.md#roles_delete) | **DELETE** /projects/{project_name}/roles/{role_name} | Delete a role from a project
*CoreApi* | [**roles_get**](docs/CoreApi.md#roles_get) | **GET** /projects/{project_name}/roles/{role_name} | Get details of a role
*CoreApi* | [**roles_list**](docs/CoreApi.md#roles_list) | **GET** /projects/{project_name}/roles | List the available roles in a project
*CoreApi* | [**roles_update**](docs/CoreApi.md#roles_update) | **PATCH** /projects/{project_name}/roles/{role_name} | Update a role in a project
*CoreApi* | [**service_status**](docs/CoreApi.md#service_status) | **GET** /status | Service status
*CoreApi* | [**service_users_create**](docs/CoreApi.md#service_users_create) | **POST** /projects/{project_name}/service-users | Create a new service user
*CoreApi* | [**service_users_delete**](docs/CoreApi.md#service_users_delete) | **DELETE** /projects/{project_name}/service-users/{service_user_id} | Delete service user
*CoreApi* | [**service_users_get**](docs/CoreApi.md#service_users_get) | **GET** /projects/{project_name}/service-users/{service_user_id} | Retrieve details of a service user
*CoreApi* | [**service_users_list**](docs/CoreApi.md#service_users_list) | **GET** /projects/{project_name}/service-users | List service users
*CoreApi* | [**service_users_token**](docs/CoreApi.md#service_users_token) | **PUT** /projects/{project_name}/service-users/{service_user_id}/token | Reset the token of a service user
*CoreApi* | [**service_users_update**](docs/CoreApi.md#service_users_update) | **PATCH** /projects/{project_name}/service-users/{service_user_id} | Update service user details
*CoreApi* | [**subscriptions_create**](docs/CoreApi.md#subscriptions_create) | **POST** /subscriptions | Create subscriptions
*CoreApi* | [**subscriptions_delete**](docs/CoreApi.md#subscriptions_delete) | **DELETE** /subscriptions/{subscription_name} | Delete a subscription
*CoreApi* | [**subscriptions_get**](docs/CoreApi.md#subscriptions_get) | **GET** /subscriptions/{subscription_name} | Get details of a subscription
*CoreApi* | [**subscriptions_list**](docs/CoreApi.md#subscriptions_list) | **GET** /subscriptions | List subscriptions
*CoreApi* | [**subscriptions_update**](docs/CoreApi.md#subscriptions_update) | **PATCH** /subscriptions/{subscription_name} | Update details of a subscription
*CoreApi* | [**user_create**](docs/CoreApi.md#user_create) | **POST** /user | Create a new user
*CoreApi* | [**user_delete**](docs/CoreApi.md#user_delete) | **DELETE** /user | Delete user
*CoreApi* | [**user_get**](docs/CoreApi.md#user_get) | **GET** /user | Get user details
*CoreApi* | [**user_update**](docs/CoreApi.md#user_update) | **PATCH** /user | Update user details


## Documentation For Models

 - [AttachmentFieldsCreate](docs/AttachmentFieldsCreate.md)
 - [AttachmentFieldsList](docs/AttachmentFieldsList.md)
 - [Attachments](docs/Attachments.md)
 - [AttachmentsCreate](docs/AttachmentsCreate.md)
 - [AttachmentsList](docs/AttachmentsList.md)
 - [BatchModelRequestCreateResponse](docs/BatchModelRequestCreateResponse.md)
 - [BatchModelRequestListResponse](docs/BatchModelRequestListResponse.md)
 - [BatchModelRequestResultList](docs/BatchModelRequestResultList.md)
 - [BatchPipelineRequestCreateResponse](docs/BatchPipelineRequestCreateResponse.md)
 - [BatchPipelineRequestListResponse](docs/BatchPipelineRequestListResponse.md)
 - [BatchPipelineRequestModelRequest](docs/BatchPipelineRequestModelRequest.md)
 - [BatchPipelineRequestResultList](docs/BatchPipelineRequestResultList.md)
 - [BlobList](docs/BlobList.md)
 - [BlobUpload](docs/BlobUpload.md)
 - [ConfigurationList](docs/ConfigurationList.md)
 - [ConnectorCreate](docs/ConnectorCreate.md)
 - [ConnectorFieldCreate](docs/ConnectorFieldCreate.md)
 - [ConnectorFieldList](docs/ConnectorFieldList.md)
 - [ConnectorList](docs/ConnectorList.md)
 - [ConnectorUpdate](docs/ConnectorUpdate.md)
 - [CredentialsCreate](docs/CredentialsCreate.md)
 - [CredentialsList](docs/CredentialsList.md)
 - [CredentialsListWithConfig](docs/CredentialsListWithConfig.md)
 - [CredentialsUpdate](docs/CredentialsUpdate.md)
 - [EnvironmentVariableCreate](docs/EnvironmentVariableCreate.md)
 - [EnvironmentVariableList](docs/EnvironmentVariableList.md)
 - [InheritedEnvironmentVariableList](docs/InheritedEnvironmentVariableList.md)
 - [Logs](docs/Logs.md)
 - [LogsCreate](docs/LogsCreate.md)
 - [Metrics](docs/Metrics.md)
 - [ModelCreate](docs/ModelCreate.md)
 - [ModelInputFieldCreate](docs/ModelInputFieldCreate.md)
 - [ModelInputFieldList](docs/ModelInputFieldList.md)
 - [ModelList](docs/ModelList.md)
 - [ModelOutputFieldCreate](docs/ModelOutputFieldCreate.md)
 - [ModelOutputFieldList](docs/ModelOutputFieldList.md)
 - [ModelRequestCreate](docs/ModelRequestCreate.md)
 - [ModelRequestList](docs/ModelRequestList.md)
 - [ModelUpdate](docs/ModelUpdate.md)
 - [ModelVersionCreate](docs/ModelVersionCreate.md)
 - [ModelVersionFileUpload](docs/ModelVersionFileUpload.md)
 - [ModelVersionList](docs/ModelVersionList.md)
 - [OrganizationCreate](docs/OrganizationCreate.md)
 - [OrganizationDetail](docs/OrganizationDetail.md)
 - [OrganizationList](docs/OrganizationList.md)
 - [OrganizationSubscriptionList](docs/OrganizationSubscriptionList.md)
 - [OrganizationUpdate](docs/OrganizationUpdate.md)
 - [OrganizationUserCreate](docs/OrganizationUserCreate.md)
 - [OrganizationUserDetail](docs/OrganizationUserDetail.md)
 - [OrganizationUserInviteList](docs/OrganizationUserInviteList.md)
 - [OrganizationUserList](docs/OrganizationUserList.md)
 - [OrganizationUserUpdate](docs/OrganizationUserUpdate.md)
 - [PermissionList](docs/PermissionList.md)
 - [PipelineCreate](docs/PipelineCreate.md)
 - [PipelineInputFieldCreate](docs/PipelineInputFieldCreate.md)
 - [PipelineInputFieldList](docs/PipelineInputFieldList.md)
 - [PipelineList](docs/PipelineList.md)
 - [PipelineObjectCreate](docs/PipelineObjectCreate.md)
 - [PipelineObjectList](docs/PipelineObjectList.md)
 - [PipelineObjectUpdate](docs/PipelineObjectUpdate.md)
 - [PipelineRequestCreate](docs/PipelineRequestCreate.md)
 - [PipelineRequestList](docs/PipelineRequestList.md)
 - [PipelineRequestModelRequest](docs/PipelineRequestModelRequest.md)
 - [ProjectCreate](docs/ProjectCreate.md)
 - [ProjectList](docs/ProjectList.md)
 - [ProjectUpdate](docs/ProjectUpdate.md)
 - [ResourceUsage](docs/ResourceUsage.md)
 - [RoleAssignmentCreate](docs/RoleAssignmentCreate.md)
 - [RoleAssignmentList](docs/RoleAssignmentList.md)
 - [RoleCreate](docs/RoleCreate.md)
 - [RoleDetailList](docs/RoleDetailList.md)
 - [RoleList](docs/RoleList.md)
 - [RoleUpdate](docs/RoleUpdate.md)
 - [ServiceUserCreate](docs/ServiceUserCreate.md)
 - [ServiceUserDetail](docs/ServiceUserDetail.md)
 - [ServiceUserList](docs/ServiceUserList.md)
 - [ServiceUserTokenList](docs/ServiceUserTokenList.md)
 - [Status](docs/Status.md)
 - [SubscriptionCreate](docs/SubscriptionCreate.md)
 - [SubscriptionDetail](docs/SubscriptionDetail.md)
 - [SubscriptionList](docs/SubscriptionList.md)
 - [SubscriptionUpdate](docs/SubscriptionUpdate.md)
 - [Success](docs/Success.md)
 - [UsagePerDay](docs/UsagePerDay.md)
 - [UsagePerDayMetric](docs/UsagePerDayMetric.md)
 - [UsagePerMonth](docs/UsagePerMonth.md)
 - [UsagePerMonthMetric](docs/UsagePerMonthMetric.md)
 - [UserDetail](docs/UserDetail.md)
 - [UserPendingCreate](docs/UserPendingCreate.md)
 - [UserPendingDetail](docs/UserPendingDetail.md)
 - [UserUpdate](docs/UserUpdate.md)


## Documentation For Authorization


## api_key

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header


