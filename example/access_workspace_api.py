import os
import requests
access_token = os.environ['APPFLOWY_ACCESS_TOKEN']
headers = {"Authorization": f"Bearer {access_token}"}
resp = requests.get(
  os.environ['APPFLOWY_API_BASE_URL'] + "/api/workspace",
  headers=headers,
)
print(resp.text)
