class GrantWriter:
    def __init__(self, config: Config):
        self.config = config

    def write_grant(self, grant_id: int, grant_data: dict):
        """
        Write grant application
        """
        url = self.config.submit_url + '/write/' + str(grant_id)
        response = requests.post(url, json=grant_data)
        if response.status_code == 200:
            print("Grant application written successfully")
        else:
            raise Exception("Error in writing grant application")
