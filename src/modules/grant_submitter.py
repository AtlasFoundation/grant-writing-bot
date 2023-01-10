import requests
import json

class GrantSubmitter:
    def __init__(self, config):
        self.config = config
        self.session = requests.Session()
    
    def login(self):
        # Login to the funding organization's portal
        login_url = self.config["login_url"]
        credentials = {"username": self.config["username"], "password": self.config["password"]}
        self.session.post(login_url, json=credentials)
        
    def submit_proposal(self, proposal, grant_id):
        # Submit the proposal to the funding organization
        submit_url = self.config["submit_url"].format(grant_id=grant_id)
        submission = {"proposal": proposal}
        response = self.session.post(submit_url, json=submission)
        
        if response.status_code != 200:
            raise Exception("Proposal submission failed with status code: " + str(response.status_code))
        
        print("Proposal submitted successfully!")