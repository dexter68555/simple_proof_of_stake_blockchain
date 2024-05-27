import random
from Stakeholder import Stakeholder

class ProofOfStake:
    def __init__(self):
        self.stakers = {}

    def add_stake(self, stakeholder):
        self.stakers[stakeholder.address] = stakeholder.stake

    def get_total_stake(self):
        return sum(self.stakers.values())

    def select_validator(self):
        total_stake = self.get_total_stake()
        r = random.uniform(0, total_stake)
        cumulative_stake = 0
        for address, stake in self.stakers.items():
            cumulative_stake += stake
            if r <= cumulative_stake:
                return address

    def validate_transaction(self, transaction):
        sender = transaction['sender']
        return sender in self.stakers and self.stakers[sender] > 0
