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

- <code title="post /auth/login">client.v2.auth.<a href="./src/qanapi/resources/v2/auth.py">login</a>(\*\*<a href="src/qanapi/types/v2/auth_login_params.py">params</a>) -> <a href="./src/qanapi/types/v2/auth_login_response.py">AuthLoginResponse</a></code>
- <code title="post /auth/logout">client.v2.auth.<a href="./src/qanapi/resources/v2/auth.py">logout</a>() -> <a href="./src/qanapi/types/v2/auth_logout_response.py">AuthLogoutResponse</a></code>
- <code title="post /auth/refresh">client.v2.auth.<a href="./src/qanapi/resources/v2/auth.py">refresh_token</a>() -> <a href="./src/qanapi/types/v2/auth_refresh_token_response.py">AuthRefreshTokenResponse</a></code>
- <code title="get /auth/userdetails">client.v2.auth.<a href="./src/qanapi/resources/v2/auth.py">retrieve_user_details</a>() -> <a href="./src/qanapi/types/v2/auth_retrieve_user_details_response.py">AuthRetrieveUserDetailsResponse</a></code>
- <code title="post /auth/revoke">client.v2.auth.<a href="./src/qanapi/resources/v2/auth.py">revoke_token</a>() -> <a href="./src/qanapi/types/v2/auth_revoke_token_response.py">AuthRevokeTokenResponse</a></code>

## Encrypt

Types:

```python
from qanapi.types.v2 import EncryptEncryptDataResponse
```

Methods:

- <code title="post /encrypt">client.v2.encrypt.<a href="./src/qanapi/resources/v2/encrypt.py">encrypt_data</a>(\*\*<a href="src/qanapi/types/v2/encrypt_encrypt_data_params.py">params</a>) -> <a href="./src/qanapi/types/v2/encrypt_encrypt_data_response.py">EncryptEncryptDataResponse</a></code>

## Decrypt

Types:

```python
from qanapi.types.v2 import DecryptDecryptPayloadResponse
```

Methods:

- <code title="post /decrypt">client.v2.decrypt.<a href="./src/qanapi/resources/v2/decrypt.py">decrypt_payload</a>(\*\*<a href="src/qanapi/types/v2/decrypt_decrypt_payload_params.py">params</a>) -> <a href="./src/qanapi/types/v2/decrypt_decrypt_payload_response.py">DecryptDecryptPayloadResponse</a></code>

## APIKeys

Types:

```python
from qanapi.types.v2 import APIKeyRevokeResponse, APIKeyRotateResponse
```

Methods:

- <code title="patch /api-keys/{apiKey}/revoke">client.v2.api_keys.<a href="./src/qanapi/resources/v2/api_keys.py">revoke</a>(api_key) -> <a href="./src/qanapi/types/v2/api_key_revoke_response.py">APIKeyRevokeResponse</a></code>
- <code title="patch /api-keys/{apiKey}/rotate">client.v2.api_keys.<a href="./src/qanapi/resources/v2/api_keys.py">rotate</a>(api_key) -> <a href="./src/qanapi/types/v2/api_key_rotate_response.py">APIKeyRotateResponse</a></code>
