class Reporting:
    def __init__(self, config: Config):
        self.config = config

    def track_progress(self, grant_id: int):
        url = self.config.submit_url + '/track/' + str(grant_id)
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception("Error in tracking progress")
