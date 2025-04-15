import requests

class DummyJsonClient:
    BASE_URL = "https://dummyjson.com"

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.token = None
        self.headers = {}

    def connect(self):
        """Authenticate and store the token if successful."""
        try:
            response = requests.post(
                f"{self.BASE_URL}/auth/login",
                json={"username": self.username, "password": self.password}
            )
            # print("Login response:", response.status_code, response.text)
            if response.status_code == 200:
                data = response.json()
                self.token = data.get("accessToken")
                # print("Access token:", self.token)
                self.headers = {
                "Authorization": f"Bearer {self.token}",
                "Content-Type": "application/json"
            }
                return True
            else:
                print(f"Login failed: {response.status_code} {response.text}")
                return False

        except requests.RequestException as e:
            print(f"Connection error: {e}")
            return False

    def get(self, path, params=None):
        """Helper method to make authenticated GET requests."""
        url = f"{self.BASE_URL}{path}"
        try:
            response = requests.get(url, headers=self.headers, params=params)
            if response.status_code == 200:
                return response.json()
            else:
                print(f"GET {path} failed: {response.status_code} {response.text}")
                return None
        except requests.RequestException as e:
            print(f"Request error on {path}: {e}")
            return None