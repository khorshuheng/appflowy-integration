# Examples

These are short explainers for minimal examples of how to use the AppFlowy OpenAPI-compatible REST endpoint.

First you need to fetch a valid access token as described in [../doc/AUTHENTICATION.md](../doc/AUTHENTICATION.md).

Then configure your environment:

```sh
 export APPFLOWY_ACCESS_TOKEN=
export APPFLOWY_API_BASE_URL=https://appflowy.example.org
```

> Including leading whitespace when exporting the token! This omits an entry in the shell history.

In absence of your own installation you use https://beta.appflowy.cloud as `APPFLOWY_API_BASE_URL`. Register there to create an account.

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

TBD
