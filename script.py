from web3 import Web3

# Connect to personal blockhain through ganache
ganache_url = 'HTTP://127.0.0.1:7545'

# Instantiate web3 connection
web3 = Web3(Web3.HTTPProvider(ganache_url))

# Send some crypotcurrency
account_1 = '0xB39331De9C11db4196E9Ef491567eD87d93d963D'  # Sender account
account_2 = '0xEb75cb47C2880A4aa4959BB1BEcB5d89Ee0C860d'  # Reciever account

# Verifying that the transaction is valid
private_key = '62e8cc682fe25ea34ba50a053882c721fa6658e84777e4eca596ca3929bae7f9'

# Get the nonce
nonce = web3.eth.getTransactionCount(account_1)

# Build a transaction
tx = {
    'nonce': nonce,
    'to': account_2,
    'value': web3.toWei(1, 'ether'),
    'gas': 2000000,
    'gasPrice': web3.toWei('50', 'gwei')
}
# Sign the transaction
signed_tx = web3.eth.account.signTransaction(tx, private_key)

# Send the transaction and get the hash (converted to hex)
tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
print(web3.toHex(tx_hash))

# Get a transaction hash
