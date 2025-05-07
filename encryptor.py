import base64
import hashlib
from cryptography.fernet import Fernet

class Encryptor:
    def __init__(self, master_password):
        key = hashlib.sha256(master_password.encode()).digest()
        self.fernet = Fernet(base64.urlsafe_b64encode(key))

    def encrypt(self, data):
        return self.fernet.encrypt(data.encode()).decode()

    def decrypt(self, token):
        return self.fernet.decrypt(token.encode()).decode()