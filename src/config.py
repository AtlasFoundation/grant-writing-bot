class Config:
    def __init__(self):
        self.login_url = ""
        self.submit_url = ""
        self.username = ""
        self.password = ""
        self.database_url = ""
        self.database_name = ""
        self.collection_name = ""

    def read_config(self, config_path: str):
        """
        Read configuration from file
        """
        with open(config_path, "r") as file:
            config = json.load(file)
            self.login_url = config["login_url"]
            self.submit_url = config["submit_url"]
            self.username = config["username"]
            self.password = config["password"]
            self.database_url = config["database_url"]
            self.database_name = config["database_name"]
            self.collection_name = config["collection_name"]
