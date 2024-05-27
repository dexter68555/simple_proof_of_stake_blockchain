from Block import Block

class Blockchain:
    def __init__(self):
        self.chain = [Block.create_genesis_block()]
        self.pending_transactions = []

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, new_block):
        if self.is_valid_new_block(new_block, self.get_latest_block()):
            self.chain.append(new_block)

    def is_valid_new_block(self, new_block, previous_block):
        if previous_block.index + 1 != new_block.index:
            return False
        if previous_block.hash != new_block.previous_hash:
            return False
        if new_block.hash != Block.calculate_hash(new_block.index, new_block.previous_hash, new_block.timestamp, new_block.transactions, new_block.validator):
            return False
        return True

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            if not self.is_valid_new_block(self.chain[i], self.chain[i-1]):
                return False
        return True

    def create_transaction(self, sender, recipient, amount):
        self.pending_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount
        })

    def get_pending_transactions(self):
        return self.pending_transactions

    def clear_pending_transactions(self):
        self.pending_transactions = []
