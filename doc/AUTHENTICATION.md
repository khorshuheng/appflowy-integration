## User Account
For the purpose of automation, it is recommended to create a separate user account, then add the user as a member in the workspace.
This is so that, in the event that the user account is compromised, the workspace owner can still revoke the user's access.

## Authentication
AppFlowy Cloud employs token-based authentication. You can retrieve a refresh token via the following steps:

1. Log in via the admin frontend. (https://beta.appflowy.cloud)
2. Check the cookies associated with the site. The refresh token is stored under the key `sb-refresh-token`, whereas the access token is stored under they key `sb-access-token`.
3. Since a refresh token can only be used once, and we plan to use it in a script, we should clear the cookie to prevent the token from being consumed.

## Access Token
For ad-hoc API requests, such as those made via Postman or Curl, it is recommended to use the access token instead of the refresh token. The following example retrieves the workspace information.

```python
import requests
access_token = "your_access_token"
headers = {"Authorization": f"Bearer {access_token}"}
resp = requests.get(
  "https://beta.appflowy.cloud/api/workspace",
  headers=headers,
)
```

## Refresh Token
For programmatic access, you can use the refresh token to obtain a new access token after the original expired.
```python
import requests
resp = requests.get(
  "https://beta.appflowy.cloud/api/workspace",
  headers=headers,
)
resp = requests.post(
  "https://beta.appflowy.clouid/gotrue/token?grant_type=refresh_token",
  json = {
    "refresh_token": <refresh_token>,
  }
access_token = resp.json()["access_token"]
```
