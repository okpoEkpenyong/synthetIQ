import requests
import json


# query = """
# {
#   nfts (skip:0, first: 10, subgraphError:deny){
#     id
#     name
#     symbol
#     owner
#     address
#     assetState
#     tx
#     block
#     transferable
#  }
# }"""

# body = { query: { match_all: {} } }

query = """
{ query: { match_all: {} } }
"""

base_url = "https://v4.subgraph.mainnet.oceanprotocol.com"
route = "/subgraphs/name/oceanprotocol/ocean-subgraph"
url = "https://v4.aquarius.oceanprotocol.com/api/aquarius/assets/query"
# url = base_url + route

headers = {"Content-Type": "application/json"}
payload = json.dumps({"query": query})
response = requests.request("POST", url, headers=headers, data=payload)
result = json.loads(response.text)

print(json.dumps(result, indent=4, sort_keys=True))
