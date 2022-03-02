from brownie import SimpleStorage, accounts, config


def read_contract():
    # Most recent deployment
    simple_storage = SimpleStorage[-1]
    print(simple_storage.retrieve())
    pass


def main():
    read_contract()
