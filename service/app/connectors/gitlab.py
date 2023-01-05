from functools import cached_property

import httpx

API_URL = "https://gitlab.com/api/graphql"


class Gitlab:
    """Gitlab connector"""

    def __init__(self, token: str):
        self.token = token
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.token}",
        }

    @cached_property
    def logged_user(self) -> str:
        """Get logged user from Gitlab API"""

        query = """
query {
    currentUser {
        username
    }
}
"""
        data = {"query": query}
        response = httpx.post(API_URL, headers=self.headers, json=data)
        username = response.json()["data"]["currentUser"]["username"]
        return username
