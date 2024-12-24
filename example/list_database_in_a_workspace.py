import requests

if __name__ == "__main__":
  access_token = <your access token>
  headers = {"Authorization": f"Bearer {access_token}"}
  base_url = "https://beta.appflowy.cloud"
  resp = requests.get(
    f"{base_url}/api/workspace",
    headers=headers).json()
  workspace_id = [
    workspace["workspace_id"]
    for workspace in resp["data"]
    if workspace["workspace_name"] == "My Workspace"
    ][0]
  resp = requests.get(
    f"{base_url}/api/workspace/{workspace_id}/database",
    headers=headers).json()
  database_id = [
    database["id"]
    for database in resp["data"]
    if any([view["name"] == "To-dos" for view in database["views"]])
  ][0]
