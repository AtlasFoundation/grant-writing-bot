import requests


class GrantFinder:
    def __init__(self, config: Config):
        self.config = config

    def search_grants(self, search_criteria: dict):
        url = self.config.grant_search_url
        response = requests.get(url, params=search_criteria)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception("Error in searching grants")
