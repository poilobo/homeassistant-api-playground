import requests
from requests import get, post

# from home_assistant import HA_HEADERS, HA_BASE_URL


class HA:
    def __init__(self, base_url: str, bearer_token: str) -> None:
        self.base_url = base_url

        self.headers = {
            "Authorization": f"Bearer {bearer_token}",
            "content-type": "application/json",
        }

    def api_call(self, url: str) -> str:
        output = ""
        try:
            response = get(url, headers=self.headers)

            resp = response.text
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)

        return resp

    def get_api(self) -> str:
        url = f"{self.base_url}/api/"
        print(f"calling {url}")

        return self.api_call(url)
