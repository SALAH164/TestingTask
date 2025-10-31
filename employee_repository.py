import requests

class EmpRepo:
    url = "https://example.com/employees"

    def fetch(self):
        r = requests.get(self.url)
        if r.status_code != 200:
            raise Exception("Request failed")
        data = r.json()
        return sorted(data, key=lambda i: i["id"])
