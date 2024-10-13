from web3 import Web3
import os
import pandas as pd
from dotenv import load_dotenv,find_dotenv

# passwords loading

path_to_file = "000 Passwords/passcode.env"  # Full path
load_dotenv(path_to_file)
password = os.getenv("PASSWORD")

# Replace with your Infura or Alchemy URL
infura_url = f'https://mainnet.infura.io/v3/{password}'
web3 = Web3(Web3.HTTPProvider(infura_url))

# Check if the connection is successful
if web3.is_connected():
    print("Connected to Ethereum Node successfully!")
else:
    print("Failed to connect to Ethereum Node.")
    

# # Uniswap v3 Factory contract address
# uniswap_v3_factory_address = web3.to_checksum_address('0x1F98431c8aD98523631AE4a59f267346ea31F984')

# # Replace this with the actual ABI JSON copied from Etherscan
# uniswap_v3_factory_abi = [
#     {
#         "inputs": [],
#         "name": "poolCount",
#         "outputs": [
#             {
#                 "internalType": "uint256",
#                 "name": "",
#                 "type": "uint256"
#             }
#         ],
#         "stateMutability": "view",
#         "type": "function"
#     },
#     {
#         "inputs": [
#             {
#                 "internalType": "address",
#                 "name": "token0",
#                 "type": "address"
#             },
#             {
#                 "internalType": "address",
#                 "name": "token1",
#                 "type": "address"
#             },
#             {
#                 "internalType": "uint24",
#                 "name": "fee",
#                 "type": "uint24"
#             }
#         ],
#         "name": "getPool",
#         "outputs": [
#             {
#                 "internalType": "address",
#                 "name": "pool",
#                 "type": "address"
#             }
#         ],
#         "stateMutability": "view",
#         "type": "function"
#     }
#     # Add more ABI entries as needed or paste the entire ABI here
# ]

# # Create a contract object for the Uniswap v3 Factory
# uniswap_v3_factory = web3.eth.contract(address=uniswap_v3_factory_address, abi=uniswap_v3_factory_abi)

# # Fetch the number of pools created by the Uniswap v3 factory
# try:
#     num_pools = uniswap_v3_factory.functions.poolCount().call()
#     print(f"Number of pools created: {num_pools}")
# except Exception as e:
#     print(f"Error fetching pool count: {e}")