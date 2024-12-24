from abc import ABC, abstractmethod
import requests

class TokenStorage(ABC):
  def __init__(self, base_url: str, initial_refresh_token: str) -> None:
    super().__init__()
    self.base_url = base_url
    self.store_refresh_token(initial_refresh_token)

  @abstractmethod
  def get_refresh_token(self) -> str:
    raise NotImplementedError

  @abstractmethod
  def store_refresh_token(self, refresh_token: str):
    raise NotImplementedError

  def get_access_token(self) -> str:
    resp = requests.post(
      f"{self.base_url}/gotrue/token?grant_type=refresh_token",
      json = {
        "refresh_token": self.get_refresh_token,
      })
    refresh_token = resp.json()["refresh_token"]
    self.store_refresh_token(refresh_token)
    return resp.json()["access_token"]


# For actual production use, you should store the refresh token in a secure way.
# For example, you can store it in a database or a file.
class InMemoryRefreshTokenStorage(TokenStorage):
  def __init__(self, base_url: str, initial_refresh_token: str) -> None:
    super().__init__(base_url, initial_refresh_token)

  def get_refresh_token(self) -> str:
    return self.refresh_token

  def store_refresh_token(self, refresh_token: str):
    self.refresh_token = refresh_token

if __name__ == "__main__":
  base_url = "https://beta.appflowy.cloud"
  storage = InMemoryRefreshTokenStorage(base_url, "your initial refresh token")
  access_token = storage.get_access_token()
