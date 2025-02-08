# Examples

These are short explainers for minimal examples of how to use the AppFlowy OpenAPI-compatible REST endpoint.

For the first two examples, you need to fetch a valid access token as described in [../doc/AUTHENTICATION.md](../doc/AUTHENTICATION.md).

Then expose those to your shell environment:

```sh
 export APPFLOWY_ACCESS_TOKEN=
```

> Including leading whitespace when exporting the token! This omits an entry in the shell history.

Optionally, you can also expose a custom endpoint:

```sh
export APPFLOWY_BASE_URL=https://appflowy.example.org
```

In absence of your own installation there is a fallback to use `https://beta.appflowy.cloud` as `APPFLOWY_BASE_URL`. Register there to create an account.

## access workspace api

After exporting the configuration to the environment, invoke this most simple example with:

```sh
python access_workspace_api.py | jq '.'
```

## list database and rows in a workspace

For this one also configure:

```sh
export APPFLOWY_WORKSPACE=My Workspace
```

Run with:

```sh
python list_database_and_rows_in_a_workspace.py | jq '.'
```

## obtain new access token via refresh token

You need to retrieve the refresh token from a browser, as previously described for the access token above.

Then expose it to your environment:

```sh
 export APPFLOWY_REFRESH_TOKEN=
```

> Here it is not so important to prepend the whitespace, since the secret will expire soonly. But it is good practice to train and keep the habit of taking advance care.

`APPFLOWY_BASE_URL` is optionally supported by this example as well.

```sh
python obtain_new_access_token_via_refresh_token.py
```
