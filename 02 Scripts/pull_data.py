import requests
import pandas as pd
import json

# Define the GraphQL endpoint for Uniswap v3 on The Graph
url = 'https://api.thegraph.com/subgraphs/name/uniswap/uniswap-v3'

# Define the GraphQL query for fetching swap data
query = """
{
  swaps(first: 1000, orderBy: timestamp, orderDirection: desc) {
    id
    transaction {
      id
      timestamp
    }
    pair {
      token0 {
        symbol
      }
      token1 {
        symbol
      }
    }
    sender
    recipient
    amount0
    amount1
    amountUSD
  }
}
"""

# Make the API request to fetch the data
response = requests.post(url, json={'query': query})

# Check if the request was successful
if response.status_code == 200:
    data = response.json()
    if 'data' in data and 'swaps' in data['data']:
        swaps = data['data']['swaps']
        
        # Check if we have data before proceeding
        if swaps:
            # Convert the JSON data into a DataFrame
            df = pd.DataFrame(swaps)
            # Save the data to a CSV file
            os.chdir('/Users/vivan/Documents/02 USC Items/01 USC/01 Semester 1/05 Paper/01 Data')
            df.to_csv('uniswap_v3_swaps.csv', index=False)
            print("Data saved successfully to 'uniswap_v3_swaps.csv'")
        else:
            print("No swap data found. The response is empty.")
    else:
        print("The GraphQL query did not return expected data format. Response content:")
        print(json.dumps(data, indent=2))
else:
    print(f"Request failed with status code {response.status_code}")
    print(response.text)