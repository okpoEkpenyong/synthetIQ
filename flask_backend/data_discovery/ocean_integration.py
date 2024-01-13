# src/data_discovery/ocean_integration.py
from ocean_lib.example_config import get_config_dict
from ocean_lib.ocean.ocean import Ocean
import requests


class OceanIntegration:
    def __init__(self, rpc, metadata_cache_url):
        self.ocean = self.get_ocean_instance(rpc)
        self.metadata_cache_url = metadata_cache_url

    def get_top_datasets(self, text):
        # Implement logic to retrieve top datasets from Ocean Protocol
        # the search method searches for DDOs in aquarius that contain the target text string
        all_ddos = self.ocean.assets.search(text)

        # Return all metadata for each dataset
        all_metadata = [ddo.metadata for ddo in all_ddos] if all_ddos else []

        return all_metadata, all_ddos

    def get_ocean_instance(self, rpc):
        config = get_config_dict(rpc)
        ocean = Ocean(config)
        return ocean

    def fetch_aquarius_data(self, body):
        url = f"{self.metadata_cache_url}/api/aquarius/assets/query"
        # url = "https://v4.aquarius.oceanprotocol.com/api/aquarius/assets/query"
        chain_ids = [
            1287,
            137,
            1,
            10,
            5,
            56,
            246,
            1285,
            80001,
            58008,
            8996,
        ]

        # body = {
        #     "from": 0,
        #     "size": 209,
        #     "query": {
        #         "bool": {
        #             "filter": [
        #                 {"term": {"_index": "aquarius"}},
        #                 {"terms": {"chainId": chain_ids}},
        #                 {"term": {"purgatory.state": False}},
        #                 {"bool": {"must_not": [{"term": {"nft.state": 5}}]}},
        #             ]
        #         }
        #     },
        #     "sort": {"nft.created": "desc"},
        # }

        response = requests.post(url, json={"body": body})
        #   response = requests.post(url, json=body)

        if response.status_code == 200:
            data = response.json()
            # print("status:", response.status_code)
            # if "hits" in data and "hits" in data["hits"]:
            #     for hit in data["hits"]["hits"]:
            return data
        else:
            print(f"Error fetching Aquarius data. Status code: {response.status_code}")
            return None
