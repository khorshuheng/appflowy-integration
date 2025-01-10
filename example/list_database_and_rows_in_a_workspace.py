import requests

if __name__ == "__main__":
  access_token = "replace with your access token"
  headers = {"Authorization": f"Bearer {access_token}"}
  base_url = "https://beta.appflowy.cloud"
  # List all workspaces which the access token has access to
  resp = requests.get(
    f"{base_url}/api/workspace",
    headers=headers).json()
  workspace_id = [
    workspace["workspace_id"]
    for workspace in resp["data"]
    if workspace["workspace_name"] == "My Workspace"
    ][0]
  # List all databases in the workspace
  resp = requests.get(
    f"{base_url}/api/workspace/{workspace_id}/database",
    headers=headers).json()
  database_id = [
    database["id"]
    for database in resp["data"]
    if any([view["name"] == "To-dos" for view in database["views"]])
  ][0]
  # List all row ids in the database
  resp = requests.get(
    f"{base_url}/api/workspace/{workspace_id}/database/{database_id}/row",
    headers=headers).json()
  row_ids = [row["id"] for row in resp["data"]]
  # List all row details in the database given the row ids
  resp = requests.get(
    f"{base_url}/api/workspace/{workspace_id}/database/{database_id}/row/detail?ids={','.join(row_ids)}",
    params={"ids": ",".join(row_ids)},
    headers=headers).json()
  # List all row updated since timestamp in the database
  resp = requests.get(
    f"{base_url}/api/workspace/{workspace_id}/database/{database_id}/row/updated",
    params={"after": "2025-01-10T15:00:00Z"},
    headers=headers).json()
