import binascii
import os
import hashlib

class Wallet:
    def __init__(self):
        self.private_key = self.generate_private_key()
        self.public_key = self.generate_public_key(self.private_key)

    @staticmethod
    def generate_private_key():
        return binascii.hexlify(os.urandom(32)).decode('utf-8')

    @staticmethod
    def generate_public_key(private_key):
        return hashlib.sha256(private_key.encode('utf-8')).hexdigest()

    def sign_data(self, data):
        return hashlib.sha256((data + self.private_key).encode('utf-8')).hexdigest()

    def get_address(self):
        return self.public_key
