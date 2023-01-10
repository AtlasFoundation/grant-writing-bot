import requests


class FundingOrganization:
    def __init__(self, config: Config):
        self.config = config

    def check_status(self, grant_id: int):
        url = self.config.submit_url + '/status/' + str(grant_id)
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception("Error in getting status")

    def get_guideline(self):
        url = self.config.submit_url + '/guideline'
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception("Error in getting guideline")
