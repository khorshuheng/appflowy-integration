from os import environ
import requests

access_token = environ['APPFLOWY_ACCESS_TOKEN']
headers = {"Authorization": f"Bearer {access_token}"}
try:
  base_url = environ['APPFLOWY_BASE_URL']
except:
  base_url = "https://beta.appflowy.cloud"
api_base_url =  base_url + "/api"
workspace_api_base_url = api_base_url + "/workspace"

resp = requests.get(
  workspace_api_base_url,
  headers=headers,
)
print(resp.text)
