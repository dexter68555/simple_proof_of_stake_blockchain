import argparse
from Wallet import Wallet
from Stakeholder import Stakeholder
from PoSBlockchain import PoSBlockchain

def main():
    parser = argparse.ArgumentParser(description="Proof-of-Stake Blockchain CLI")
    parser.add_argument('command', choices=['create_wallet', 'add_stakeholder', 'create_transaction', 'mine', 'check_chain', 'get_balance', 'print_block'])
    parser.add_argument('--address', type=str, help="Address of the wallet")
    parser.add_argument('--stake', type=int, help="Stake amount for the stakeholder")
    parser.add_argument('--sender', type=str, help="Sender address for the transaction")
    parser.add_argument('--recipient', type=str, help="Recipient address for the transaction")
    parser.add_argument('--amount', type=int, help="Transaction amount")
    parser.add_argument('--index', type=int, help="Index of the block to print")

    args = parser.parse_args()
    blockchain = PoSBlockchain()

    if args.command == 'create_wallet':
        wallet = Wallet()
        print(f"New wallet created. Address: {wallet.get_address()}")
    elif args.command == 'add_stakeholder':
        if args.address and args.stake:
            blockchain.add_stakeholder(Stakeholder(args.address, args.stake))
            print(f"Stakeholder {args.address} added with stake {args.stake}")
        else:
            print("Address and stake are required to add a stakeholder.")
    elif args.command == 'create_transaction':
        if args.sender and args.recipient and args.amount:
            blockchain.create_transaction(args.sender, args.recipient, args.amount)
            print(f"Transaction from {args.sender} to {args.recipient} of amount {args.amount} created.")
        else:
            print("Sender, recipient, and amount are required to create a transaction.")
    elif args.command == 'mine':
        blockchain.simulate_block_creation()
    elif args.command == 'check_chain':
        if blockchain.is_chain_valid():
            print("The blockchain is valid.")
        else:
            print("The blockchain is not valid.")
    elif args.command == 'print_block':
        if args.index is not None:
            blockchain.print_block(args.index)
        else:
            print("Block index is required to print block details.")

if __name__ == '__main__':
    main()
