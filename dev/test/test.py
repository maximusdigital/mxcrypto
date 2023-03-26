from web3 import Web3

binance_testnet_rpc_url = "https://data-seed-prebsc-1-s1.binance.org:8545/"

web3 = Web3(Web3.HTTPProvider(binance_testnet_rpc_url))
print(f"Is connected: {web3.is_connected()}")  # Is connected: True
# С подключением ва


arb_url = "https://arb1.arbitrum.io/rpc"
web3_arb = Web3(Web3.HTTPProvider(arb_url))
web3_arb.is_connected()

print(f"Is connected: {web3_arb.is_connected()}")  # Is connected: True