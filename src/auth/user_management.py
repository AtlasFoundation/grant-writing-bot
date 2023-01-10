class UserManagement:
    def __init__(self, config: Config):
        self.config = config

    def login(self):
        url = self.config.login_url
        data = {"username": self.config.username,
                "password": self.config.password}
        response = requests.post(url, data=data)
        if response.status_code == 200:
            print("Login Successful")
        else:
            raise Exception("Error in logging in")

    def logout(self):
        url = self.config.login_url + '/logout'
        response = requests.get(url)
        if response.status_code == 200:
            print("Logout Successful")
        else:
            raise Exception("Error in logging out")
