import json
import os

class PasswordStore:
    def __init__(self, encryptor):
        self.file = "data.json"
        self.encryptor = encryptor
        if not os.path.exists(self.file):
            with open(self.file, "w") as f:
                json.dump({}, f)

    def save(self, service, username, password):
        with open(self.file, "r") as f:
            data = json.load(f)

        data[service] = {
            "username": self.encryptor.encrypt(username),
            "password": self.encryptor.encrypt(password)
        }

        with open(self.file, "w") as f:
            json.dump(data, f)

    def load(self):
        with open(self.file, "r") as f:
            data = json.load(f)

        decrypted = {}
        for service, creds in data.items():
            decrypted[service] = {
                "username": self.encryptor.decrypt(creds["username"]),
                "password": self.encryptor.decrypt(creds["password"])
            }
        return decrypted