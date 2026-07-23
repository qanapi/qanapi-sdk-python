# Auth

Types:

```python
from qanapi.types import (
    AuthLoginResponse,
    AuthLogoutResponse,
    AuthRefreshTokenResponse,
    AuthRetrieveUserDetailsResponse,
    AuthRevokeTokenResponse,
)
```

Methods:

- <code title="post /auth/login">client.auth.<a href="./src/qanapi/resources/auth.py">login</a>(\*\*<a href="src/qanapi/types/auth_login_params.py">params</a>) -> <a href="./src/qanapi/types/auth_login_response.py">AuthLoginResponse</a></code>
- <code title="post /auth/logout">client.auth.<a href="./src/qanapi/resources/auth.py">logout</a>() -> <a href="./src/qanapi/types/auth_logout_response.py">AuthLogoutResponse</a></code>
- <code title="post /auth/refresh">client.auth.<a href="./src/qanapi/resources/auth.py">refresh_token</a>() -> <a href="./src/qanapi/types/auth_refresh_token_response.py">AuthRefreshTokenResponse</a></code>
- <code title="get /auth/userdetails">client.auth.<a href="./src/qanapi/resources/auth.py">retrieve_user_details</a>() -> <a href="./src/qanapi/types/auth_retrieve_user_details_response.py">AuthRetrieveUserDetailsResponse</a></code>
- <code title="post /auth/revoke">client.auth.<a href="./src/qanapi/resources/auth.py">revoke_token</a>() -> <a href="./src/qanapi/types/auth_revoke_token_response.py">AuthRevokeTokenResponse</a></code>

# Encrypt

Types:

```python
from qanapi.types import EncryptEncryptDataResponse
```

Methods:

- <code title="post /encrypt">client.encrypt.<a href="./src/qanapi/resources/encrypt.py">encrypt_data</a>(\*\*<a href="src/qanapi/types/encrypt_encrypt_data_params.py">params</a>) -> <a href="./src/qanapi/types/encrypt_encrypt_data_response.py">EncryptEncryptDataResponse</a></code>

# Decrypt

Types:

```python
from qanapi.types import DecryptDecryptPayloadResponse
```

Methods:

- <code title="post /decrypt">client.decrypt.<a href="./src/qanapi/resources/decrypt.py">decrypt_payload</a>(\*\*<a href="src/qanapi/types/decrypt_decrypt_payload_params.py">params</a>) -> <a href="./src/qanapi/types/decrypt_decrypt_payload_response.py">DecryptDecryptPayloadResponse</a></code>

# APIKeys

Types:

```python
from qanapi.types import APIKeyRevokeResponse, APIKeyRotateResponse
```

Methods:

- <code title="patch /api-keys/{apiKey}/revoke">client.api_keys.<a href="./src/qanapi/resources/api_keys.py">revoke</a>(api_key) -> <a href="./src/qanapi/types/api_key_revoke_response.py">APIKeyRevokeResponse</a></code>
- <code title="patch /api-keys/{apiKey}/rotate">client.api_keys.<a href="./src/qanapi/resources/api_keys.py">rotate</a>(api_key) -> <a href="./src/qanapi/types/api_key_rotate_response.py">APIKeyRotateResponse</a></code>
