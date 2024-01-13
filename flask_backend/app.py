# flask backend server  main.py

from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS extension
from user_management.user_profile import UserProfile
from data_discovery.ocean_integration import OceanIntegration
from data_discovery.data_recommender import DataRecommender
import pprint
import time
import pandas as pd


infura_url = "https://mainnet.infura.io/v3/334badec8bd2402e8e60e8424698981b"

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes


@app.route("/api/recommendations", methods=["GET"])
def recommend_datasets():
    metadata_cache_url = "https://v4.aquarius.oceanprotocol.com"

    ocean_integration = OceanIntegration(infura_url, metadata_cache_url)

    ocean_instance = ocean_integration.get_ocean_instance(
        infura_url,
    )

    tags = ["climate"]  # target search text in the DDO
    # tags = ["compute", "climate"]  # target search text in the DDsO

    user_profile = UserProfile(user_id=1, interests=tags)

    data_recommender = DataRecommender(ocean_integration, user_profile)

    recommended_datasets = data_recommender.recommend_datasets(user_profile, tags)

    df = pd.DataFrame(recommended_datasets)

    df.to_csv("recommended_datasets.csv", index=False)

    # print("Recommended Datasets:", recommended_datasets)

    return jsonify(recommended_datasets)


if __name__ == "__main__":
    app.run(debug=True, port=5100)
