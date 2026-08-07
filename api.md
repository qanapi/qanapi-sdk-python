# V3

Types:

```python
from qanapi.types import APIKey, Configuration, Permission, Role, User, Value
```

## Roles

Types:

```python
from qanapi.types.v3 import RoleListResponse
```

Methods:

- <code title="get /v3/roles">client.v3.roles.<a href="./src/qanapi/resources/v3/roles.py">list</a>() -> <a href="./src/qanapi/types/v3/role_list_response.py">RoleListResponse</a></code>

## Configurations

Types:

```python
from qanapi.types.v3 import ConfigurationListResponse
```

Methods:

- <code title="post /v3/configurations">client.v3.configurations.<a href="./src/qanapi/resources/v3/configurations.py">create</a>(\*\*<a href="src/qanapi/types/v3/configuration_create_params.py">params</a>) -> <a href="./src/qanapi/types/configuration.py">Configuration</a></code>
- <code title="put /v3/configurations/{configuration}">client.v3.configurations.<a href="./src/qanapi/resources/v3/configurations.py">update</a>(configuration, \*\*<a href="src/qanapi/types/v3/configuration_update_params.py">params</a>) -> <a href="./src/qanapi/types/configuration.py">Configuration</a></code>
- <code title="get /v3/configurations">client.v3.configurations.<a href="./src/qanapi/resources/v3/configurations.py">list</a>() -> <a href="./src/qanapi/types/v3/configuration_list_response.py">ConfigurationListResponse</a></code>
- <code title="delete /v3/configurations/{configuration}">client.v3.configurations.<a href="./src/qanapi/resources/v3/configurations.py">delete</a>(configuration) -> None</code>
- <code title="get /v3/configurations/{configuration}">client.v3.configurations.<a href="./src/qanapi/resources/v3/configurations.py">show</a>(configuration) -> <a href="./src/qanapi/types/configuration.py">Configuration</a></code>

## Users

Types:

```python
from qanapi.types.v3 import UserListResponse
```

Methods:

- <code title="post /v3/users">client.v3.users.<a href="./src/qanapi/resources/v3/users.py">create</a>(\*\*<a href="src/qanapi/types/v3/user_create_params.py">params</a>) -> <a href="./src/qanapi/types/user.py">User</a></code>
- <code title="get /v3/users">client.v3.users.<a href="./src/qanapi/resources/v3/users.py">list</a>() -> <a href="./src/qanapi/types/v3/user_list_response.py">UserListResponse</a></code>
- <code title="delete /v3/users/{user}">client.v3.users.<a href="./src/qanapi/resources/v3/users.py">delete</a>(user) -> None</code>
- <code title="get /v3/users/me">client.v3.users.<a href="./src/qanapi/resources/v3/users.py">me</a>() -> <a href="./src/qanapi/types/user.py">User</a></code>
- <code title="patch /v3/users/{user}">client.v3.users.<a href="./src/qanapi/resources/v3/users.py">patch</a>(user, \*\*<a href="src/qanapi/types/v3/user_patch_params.py">params</a>) -> <a href="./src/qanapi/types/user.py">User</a></code>
- <code title="patch /v3/users/{user}/restore">client.v3.users.<a href="./src/qanapi/resources/v3/users.py">restore</a>(user) -> <a href="./src/qanapi/types/user.py">User</a></code>
- <code title="get /v3/users/{user}">client.v3.users.<a href="./src/qanapi/resources/v3/users.py">show</a>(user) -> <a href="./src/qanapi/types/user.py">User</a></code>

## APIKeys

Types:

```python
from qanapi.types.v3 import APIKeyListResponse, APIKeyRotateResponse
```

Methods:

- <code title="get /v3/api-keys">client.v3.api_keys.<a href="./src/qanapi/resources/v3/api_keys.py">list</a>() -> <a href="./src/qanapi/types/v3/api_key_list_response.py">APIKeyListResponse</a></code>
- <code title="post /v3/api-keys/{apiKey}/revoke">client.v3.api_keys.<a href="./src/qanapi/resources/v3/api_keys.py">revoke</a>(api_key) -> None</code>
- <code title="post /v3/api-keys/{apiKey}/rotate">client.v3.api_keys.<a href="./src/qanapi/resources/v3/api_keys.py">rotate</a>(api_key) -> <a href="./src/qanapi/types/v3/api_key_rotate_response.py">APIKeyRotateResponse</a></code>
- <code title="get /v3/api-keys/{apiKey}">client.v3.api_keys.<a href="./src/qanapi/resources/v3/api_keys.py">show</a>(api_key) -> <a href="./src/qanapi/types/api_key.py">APIKey</a></code>

## Logs

Types:

```python
from qanapi.types.v3 import (
    LogActivityResponse,
    LogAPIResponse,
    LogQanapiFlowResponse,
    LogUnifiedResponse,
)
```

Methods:

- <code title="get /v3/logs/activity">client.v3.logs.<a href="./src/qanapi/resources/v3/logs.py">activity</a>(\*\*<a href="src/qanapi/types/v3/log_activity_params.py">params</a>) -> <a href="./src/qanapi/types/v3/log_activity_response.py">LogActivityResponse</a></code>
- <code title="get /v3/logs/api">client.v3.logs.<a href="./src/qanapi/resources/v3/logs.py">api</a>(\*\*<a href="src/qanapi/types/v3/log_api_params.py">params</a>) -> <a href="./src/qanapi/types/v3/log_api_response.py">LogAPIResponse</a></code>
- <code title="get /v3/logs/qanapi-flow">client.v3.logs.<a href="./src/qanapi/resources/v3/logs.py">qanapi_flow</a>(\*\*<a href="src/qanapi/types/v3/log_qanapi_flow_params.py">params</a>) -> <a href="./src/qanapi/types/v3/log_qanapi_flow_response.py">LogQanapiFlowResponse</a></code>
- <code title="get /v3/logs/unified">client.v3.logs.<a href="./src/qanapi/resources/v3/logs.py">unified</a>(\*\*<a href="src/qanapi/types/v3/log_unified_params.py">params</a>) -> <a href="./src/qanapi/types/v3/log_unified_response.py">LogUnifiedResponse</a></code>

## Encryption

Types:

```python
from qanapi.types.v3 import EncryptionDecryptResponse, EncryptionEncryptResponse
```

Methods:

- <code title="post /v3/encryption/{proxy}/decrypt">client.v3.encryption.<a href="./src/qanapi/resources/v3/encryption.py">decrypt</a>(proxy, \*\*<a href="src/qanapi/types/v3/encryption_decrypt_params.py">params</a>) -> <a href="./src/qanapi/types/v3/encryption_decrypt_response.py">EncryptionDecryptResponse</a></code>
- <code title="post /v3/encryption/{proxy}/encrypt">client.v3.encryption.<a href="./src/qanapi/resources/v3/encryption.py">encrypt</a>(proxy, \*\*<a href="src/qanapi/types/v3/encryption_encrypt_params.py">params</a>) -> <a href="./src/qanapi/types/v3/encryption_encrypt_response.py">EncryptionEncryptResponse</a></code>

# V2

## Auth

Types:

```python
from qanapi.types.v2 import (
    AuthLoginResponse,
    AuthLogoutResponse,
    AuthRefreshTokenResponse,
    AuthRetrieveUserDetailsResponse,
    AuthRevokeTokenResponse,
)
```

Methods:

- <code title="post /v2/auth/login">client.v2.auth.<a href="./src/qanapi/resources/v2/auth.py">login</a>(\*\*<a href="src/qanapi/types/v2/auth_login_params.py">params</a>) -> <a href="./src/qanapi/types/v2/auth_login_response.py">AuthLoginResponse</a></code>
- <code title="post /v2/auth/logout">client.v2.auth.<a href="./src/qanapi/resources/v2/auth.py">logout</a>() -> <a href="./src/qanapi/types/v2/auth_logout_response.py">AuthLogoutResponse</a></code>
- <code title="post /v2/auth/refresh">client.v2.auth.<a href="./src/qanapi/resources/v2/auth.py">refresh_token</a>() -> <a href="./src/qanapi/types/v2/auth_refresh_token_response.py">AuthRefreshTokenResponse</a></code>
- <code title="get /v2/auth/userdetails">client.v2.auth.<a href="./src/qanapi/resources/v2/auth.py">retrieve_user_details</a>() -> <a href="./src/qanapi/types/v2/auth_retrieve_user_details_response.py">AuthRetrieveUserDetailsResponse</a></code>
- <code title="post /v2/auth/revoke">client.v2.auth.<a href="./src/qanapi/resources/v2/auth.py">revoke_token</a>() -> <a href="./src/qanapi/types/v2/auth_revoke_token_response.py">AuthRevokeTokenResponse</a></code>

## Encrypt

Types:

```python
from qanapi.types.v2 import EncryptEncryptDataResponse
```

Methods:

- <code title="post /v2/encrypt">client.v2.encrypt.<a href="./src/qanapi/resources/v2/encrypt.py">encrypt_data</a>(\*\*<a href="src/qanapi/types/v2/encrypt_encrypt_data_params.py">params</a>) -> <a href="./src/qanapi/types/v2/encrypt_encrypt_data_response.py">EncryptEncryptDataResponse</a></code>

## Decrypt

Types:

```python
from qanapi.types.v2 import DecryptDecryptPayloadResponse
```

Methods:

- <code title="post /v2/decrypt">client.v2.decrypt.<a href="./src/qanapi/resources/v2/decrypt.py">decrypt_payload</a>(\*\*<a href="src/qanapi/types/v2/decrypt_decrypt_payload_params.py">params</a>) -> <a href="./src/qanapi/types/v2/decrypt_decrypt_payload_response.py">DecryptDecryptPayloadResponse</a></code>

## APIKeys

Types:

```python
from qanapi.types.v2 import APIKeyRevokeResponse, APIKeyRotateResponse
```

Methods:

- <code title="patch /v2/api-keys/{apiKey}/revoke">client.v2.api_keys.<a href="./src/qanapi/resources/v2/api_keys.py">revoke</a>(api_key) -> <a href="./src/qanapi/types/v2/api_key_revoke_response.py">APIKeyRevokeResponse</a></code>
- <code title="patch /v2/api-keys/{apiKey}/rotate">client.v2.api_keys.<a href="./src/qanapi/resources/v2/api_keys.py">rotate</a>(api_key) -> <a href="./src/qanapi/types/v2/api_key_rotate_response.py">APIKeyRotateResponse</a></code>
