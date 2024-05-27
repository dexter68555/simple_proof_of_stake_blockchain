import hashlib
import time

class Block:
    def __init__(self, index, previous_hash, timestamp, transactions, validator, hash, signature):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.transactions = transactions
        self.validator = validator
        self.hash = hash
        self.signature = signature

    @staticmethod
    def calculate_hash(index, previous_hash, timestamp, transactions, validator):
        value = str(index) + str(previous_hash) + str(timestamp) + str(transactions) + str(validator)
        return hashlib.sha256(value.encode('utf-8')).hexdigest()

    @staticmethod
    def create_genesis_block():
        return Block(0, "0", int(time.time()), "Genesis Block", "0", "0", "0")
