import time
import json
from Blockchain import Blockchain
from ProofOfStake import ProofOfStake
from Block import Block
from Wallet import Wallet
from Stakeholder import Stakeholder

class PoSBlockchain:
    def __init__(self, blockchain_file='blockchain.json'):
        self.blockchain_file = blockchain_file
        self.blockchain = Blockchain()
        self.pos = ProofOfStake()
        self.load_blockchain()

    def add_stakeholder(self, stakeholder):
        self.pos.add_stake(stakeholder)
        self.save_blockchain()

    def create_block(self, validator_address):
        latest_block = self.blockchain.get_latest_block()
        new_index = latest_block.index + 1
        new_timestamp = int(time.time())
        transactions = self.blockchain.get_pending_transactions()
        new_hash = Block.calculate_hash(new_index, latest_block.hash, new_timestamp, transactions, validator_address)
        new_signature = Wallet().sign_data(new_hash)
        new_block = Block(new_index, latest_block.hash, new_timestamp, transactions, validator_address, new_hash, new_signature)
        self.blockchain.add_block(new_block)
        self.blockchain.clear_pending_transactions()
        print(f"Block {new_index} added by {validator_address}")
        self.save_blockchain()

    def simulate_block_creation(self):
        validator = self.pos.select_validator()
        self.create_block(validator)

    def create_transaction(self, sender, recipient, amount):
        self.blockchain.create_transaction(sender, recipient, amount)
        self.save_blockchain()

    def is_chain_valid(self):
        return self.blockchain.is_chain_valid()

    def print_block(self, index):
        if index < 0 or index >= len(self.blockchain.chain):
            print("Block index out of range")
            return
        block = self.blockchain.chain[index]
        print(json.dumps(block.__dict__, indent=4))

    def save_blockchain(self):
        data = {
            'chain': [block.__dict__ for block in self.blockchain.chain],
            'pending_transactions': self.blockchain.get_pending_transactions(),
            'stakers': self.pos.stakers
        }
        with open(self.blockchain_file, 'w') as file:
            json.dump(data, file)

    def load_blockchain(self):
        try:
            with open(self.blockchain_file, 'r') as file:
                data = json.load(file)
                self.blockchain.chain = [Block(**block) for block in data['chain']]
                self.blockchain.pending_transactions = data['pending_transactions']
                self.pos.stakers = data['stakers']
        except FileNotFoundError:
            pass
