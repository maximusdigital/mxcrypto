from web3 import Web3

binance_testnet_rpc = "https://data-seed-prebsc-1-s1.binance.org:8545/"

web3_binance = Web3(Web3.HTTPProvider(binance_testnet_rpc))
print(f"Is connected: {web3_binance.is_connected()}")  # Is connected: True
# С подключением ва

print(f"gas price: {web3_binance.eth.gas_price} BNB")  # кол-во Wei за единицу газа
print(f"current block number: {web3_binance.eth.block_number}")
print(f"number of current chain is {web3_binance.eth.chain_id}")  # 97


arbitrum_rpc = "https://arb1.arbitrum.io/rpc"
web3_arbitrum = Web3(Web3.HTTPProvider(arbitrum_rpc))
print(f"Is connected: {web3_arbitrum.is_connected()}")  # Is connected: True

