import p  # print
import re
from user_management.user_profile import UserProfile
from datetime import datetime
from collections import namedtuple
from data_discovery.ocean_integration import OceanIntegration
import numpy as np
from shapely.geometry import Polygon
import pandas as pd


"""_scenario_
Let's consider a scenario where we're dealing with a climate data dataset,
and we want to evaluate its quality based on the following characteristics:

1. Completeness of Key Variables:
Check for the presence of key variables that are crucial for climate data,
such as temperature, humidity, and precipitation.

2. Temporal Coverage:
Assess the dataset's temporal coverage to ensure it spans a relevant time period for climate analysis.

3. Geographical Coverage:
Evaluate the geographical coverage to ensure the dataset covers regions of interest for climate studies.

4. Data Format Consistency:
Check if the data is consistent in terms of format (e.g., uniform units, consistent data types).

5.Metadata Availability:
Assess the presence of metadata, including information about the data source, collection methods, and any transformations applied.

# Additional from OPF docs:
1. What is the reputation of the dataset's publisher?
2. Does the dataset include well-defined metadata and provenance information?
3. Is sample data available for evaluation?
4. What is the dataset's rating within the marketplace? (Check the star rating we've implemented.)
5. Is the publisher responsive to inquiries? You can initiate a direct message to the publisher via the marketplace to engage in discussions before making a data purchase.

Note: Provenance is a record of ownership of a work of art or an antique, used as a guide to authenticity or quality
"""


class DataRecommender:
    def __init__(self, ocean_integration, user_profile):
        self.user_profile = user_profile
        self.ocean_integration = ocean_integration

    def evaluate_data_quality(self, dataset):
        # Placeholder values for metrics weights
        completeness_weight = 0.4
        temporal_coverage_weight = 0.2
        geographical_coverage_weight = 0.2
        data_format_consistency_weight = 0.1
        metadata_availability_weight = 0.1

        # Placeholder scores for each metric
        completeness_score = self.evaluate_completeness(dataset)
        temporal_coverage_score = self.evaluate_temporal_coverage(dataset)
        geographical_coverage_score = self.evaluate_geographical_coverage(dataset)
        data_format_consistency_score = self.evaluate_data_format_consistency(dataset)
        metadata_availability_score = self.evaluate_metadata_availability(dataset)

        # Calculate the overall quality score based on weighted metrics
        overall_quality_score = (
            completeness_weight * completeness_score
            + temporal_coverage_weight * temporal_coverage_score
            + geographical_coverage_weight * geographical_coverage_score
            + data_format_consistency_weight * data_format_consistency_score
            + metadata_availability_weight * metadata_availability_score
        )

        # print("overall_quality_score:", overall_quality_score)

        return overall_quality_score

    def calculate_overlap_score(
        self, range1_start, range1_end, range2_start, range2_end
    ):
        # Placeholder logic to calculate the overlap score between two date ranges
        """Algorithm By Raymond Hettinger (stackoverflow)
           1. Determine the latest of the two start dates and the earliest of the two end dates.
           2.Compute the timedelta by subtracting them.
           3. If the delta is positive, that is the number of days of overlap.
        Args:
            range1_start (_type_): datetime
            range1_end (_type_): datetime
            range2_start (_type_): datetime
            range2_end (_type_): datetime

        Returns:
            _type_: int
        """
        named_range = namedtuple("named_range", ["start", "end"])

        r1 = named_range(start=range1_start, end=range1_end)
        r2 = named_range(start=range2_start, end=range2_end)

        latest_start = max(r1.start, r2.start)
        earliest_end = min(r1.end, r2.end)
        delta = (earliest_end - latest_start).days + 1

        overlap = max(0, delta)

        return overlap

    def evaluate_completeness(self, dataset):
        # Placeholder logic to check completeness of key variables
        key_variables = ["temperature", "humidity", "precipitation"]

        # Check if "categories" is available in the dataset metadata
        if (
            "categories" in dataset
            and dataset["metadata"]["categories"] is not None
            and dataset["metadata"]["description"] is not None
            and dataset["metadata"]["additionalInformation"] is not None
        ):
            present_variables = [
                variable
                for variable in key_variables
                if variable in dataset["metadata"]["categories"]
                or variable in dataset["metadata"]["description"]
                or variable in dataset["metadata"]["additionalInformation"]
            ]
            completeness_score = len(present_variables) / len(key_variables)
        else:
            # Handle the case when "categories" is not available
            completeness_score = 0.0  # You can choose an appropriate default value

        # print("completeness_score:", completeness_score)
        return completeness_score

    def evaluate_temporal_coverage(self, dataset):
        # Check if "temporal_coverage" is available in the dataset
        if (
            "temporal_coverage" in dataset
            and dataset["additionalInformation"]["temporal_coverage"] is not None
        ):
            # Placeholder logic to assess temporal coverage
            start_date_str = dataset["additionalInformation"]["temporal_coverage"][
                "start"
            ]
            end_date_str = dataset["additionalInformation"]["temporal_coverage"]["end"]

            # Convert date strings to datetime objects
            start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
            end_date = datetime.strptime(end_date_str, "%Y-%m-%d")

            # For demonstration, consider a target time period
            target_start_date_str = "2022-04-11"
            target_end_date_str = "2023-03-22"

            # Convert target date strings to datetime objects
            target_start_date = datetime.strptime(target_start_date_str, "%Y-%m-%d")
            target_end_date = datetime.strptime(target_end_date_str, "%Y-%m-%d")

            # Calculate a temporal coverage score based on the intersection of the dataset and target time period
            temporal_coverage_score = self.calculate_overlap_score(
                start_date, end_date, target_start_date, target_end_date
            )
        else:
            # Handle the case when "temporal_coverage" is not available
            temporal_coverage_score = 0.0  # You can choose an appropriate default value
            # print("temporal_coverage_score:", temporal_coverage_score)
        return temporal_coverage_score

    def evaluate_geographical_coverage(self, dataset):
        if (
            "geographical_coverage" in dataset
            and dataset["additionalInformation"]["geographical_coverage"] is not None
        ):
            # Placeholder logic to assess geographical coverage
            dataset_coverage = dataset["additionalInformation"]["geographical_coverage"]

            target_coverage = {"latitude": (0, 60), "longitude": (-90, 90)}

            # Calculate a geographical coverage score based on the intersection of the dataset and target ranges

            # Create polygons representing the geographical coverage
            dataset_polygon = Polygon(
                [
                    (dataset_coverage["longitude"][0], dataset_coverage["latitude"][0]),
                    (dataset_coverage["longitude"][1], dataset_coverage["latitude"][0]),
                    (dataset_coverage["longitude"][1], dataset_coverage["latitude"][1]),
                    (dataset_coverage["longitude"][0], dataset_coverage["latitude"][1]),
                ]
            )

            target_polygon = Polygon(
                [
                    (target_coverage["longitude"][0], target_coverage["latitude"][0]),
                    (target_coverage["longitude"][1], target_coverage["latitude"][0]),
                    (target_coverage["longitude"][1], target_coverage["latitude"][1]),
                    (target_coverage["longitude"][0], target_coverage["latitude"][1]),
                ]
            )

            # Calculate the intersection area of the two polygons
            intersection_area = dataset_polygon.intersection(target_polygon).area

            # Normalize by the area of the dataset's coverage
            dataset_area = dataset_polygon.area
            geographical_coverage_score = intersection_area / dataset_area
        else:
            geographical_coverage_score = 0.0
            # print("geographical_coverage_score:", geographical_coverage_score)
        return geographical_coverage_score

    def evaluate_data_format_consistency(self, dataset):
        if (
            "data_format" in dataset
            and dataset["additionalInformation"]["data_format"] is not None
        ):
            # Placeholder logic to check data format consistency
            unit = dataset["data_format"]["unit"]
            data_type = dataset["data_format"]["data_type"]

            # For demonstration, consider a target unit and data type
            target_unit = "Celsius"
            target_data_type = "float"

            # Check if the dataset's unit and data type match the target
            data_format_consistency_score = (
                1.0 if (unit == target_unit and data_type == target_data_type) else 0.0
            )
        else:
            data_format_consistency_score = 0.0
            # print("data_format_consistency_score:", data_format_consistency_score)
        return data_format_consistency_score

    def evaluate_metadata_availability(self, dataset):
        # Placeholder logic to assess metadata availability
        essential_metadata = [
            "source",
            "collection_methods",
            "transformation",
            "created",
            "description",
            "name",
            "categories",
            "license",
            "author",
            "data-format",
            "temporal-coverage",
            "event",  # additional info for provenance
        ]

        if "metadata" in dataset and dataset["metadata"] is not None:
            metadata = dataset["metadata"]

            # Check if "additionalInformation" is present and not None
            additional_info = metadata.get("additionalInformation")
            event_info = dataset.get("event")

            if additional_info is not None and event_info is not None:
                # Check if essential metadata fields are present in the dataset
                present_metadata = [
                    field
                    for field in essential_metadata
                    if (field in metadata or field in additional_info)
                    or field in event_info
                ]

                # Calculate a metadata availability score based on the presence of essential metadata
                metadata_availability_score = len(present_metadata) / len(
                    essential_metadata
                )
            else:
                metadata_availability_score = 0.0
        else:
            metadata_availability_score = 0.0

        # print("metadata_availability_score:", metadata_availability_score)
        return metadata_availability_score

    def recommend_datasets(self, user_profile: UserProfile, tags):
        # Placeholder for recommendation algorithm

        NAME_PER_NETWORK = {
            1: "mainnet",
            5: "goerli",
            10: "optimism",
            56: "bsc",
            137: "polygon",
            246: "energyweb",
            1285: "moonriver",
            1287: "moonbase",
            80001: "mumbai",
            58008: "sepolia",
            8996: "development",
        }

        chain_ids = [137, 1, 10]
        body = {
            "from": 0,
            "size": 400,
            "query": {
                "bool": {
                    "filter": [
                        {"term": {"_index": "aquarius"}},
                        {"terms": {"chainId": chain_ids}},
                        {"term": {"purgatory.state": False}},
                        {"bool": {"must_not": [{"term": {"nft.state": 5}}]}},
                    ]
                }
            },
            "sort": {"nft.created": "desc"},
        }
        aquarius_data = self.ocean_integration.fetch_aquarius_data(body)

        if aquarius_data:
            # Use aquarius_data to filter and recommend datasets based on user interests
            relevant_datasets = [
                dataset["_source"]
                for dataset in aquarius_data["hits"]["hits"]
                if (
                    any(
                        re.search(re.escape(tags), str(dataset["_source"]))
                        for tags in user_profile.interests
                    )
                )
            ]

            # #print(relevant_datasets["_source"]["metadata"])
            # Create a DataFrame from the relevant datasets
            # df = pd.DataFrame(relevant_datasets)

            # Save the DataFrame to a CSV file
            # df.to_csv("compute_relevant_datasets.csv", index=False)

            # #print("Saved relevant datasets to 'relevant_datasets.csv'")

            # #print(df)
            # #print(df.columns)

            # print("tags:", tags)
            # print("interests:", user_profile.interests)

            # Dummy top datasets (DDO)
            dummy_top_datasets = [
                {
                    "id": "dummy_dataset_123",
                    "name": "Climate Data Set",
                    "tags": ["climate", "temperature", "humidity", "precipitation"],
                    "variables": ["temperature", "humidity", "precipitation"],
                    "temporal_coverage": {"start": "2022-01-01", "end": "2022-12-31"},
                    "geographical_coverage": {
                        "latitude": (0, 90),
                        "longitude": (-180, 180),
                    },
                    "data_format": {"unit": "Celsius", "data_type": "float"},
                    "metadata": {
                        "source": "Dummy Climate Organization",
                        "collection_methods": "Sensor network",
                        "transformation": "Cleaned and normalized",
                    },
                },
                {
                    "id": "2",
                    "tags": ["oceanography"],
                    "metadata": {
                        "characteristic1": "value3",
                        "characteristic2": "value4",
                    },
                },
                {
                    "id": "3",
                    "tags": ["challenge"],
                    "metadata": {
                        "characteristic1": "value3",
                        "characteristic2": "value4",
                    },
                },
                {
                    "id": "4",
                    "tags": ["predictions"],
                    "metadata": {
                        "characteristic1": "value3",
                        "characteristic2": "value4",
                    },
                },
                # Add more dummy datasets as needed
            ]

            # #print("user_profile interest:", user_profile.interests)
            # #print("dummy_top_datasets:", dummy_top_datasets)
            # #print("relevant datasets:", relevant_datasets)
            # Evaluate data quality for each dataset
            ranked_datasets = [
                (dataset, self.evaluate_data_quality(dataset))
                for dataset in relevant_datasets
            ]
            # print("//////////////////////////////////////////")

            ranked_datasets.sort(key=lambda x: x[1], reverse=True)

            # Return recommended datasets
            recommended_datasets = [dataset[0] for dataset in ranked_datasets]

            # Recommend only the top 10 datasets
            top_datasets = ranked_datasets[:10]

            # print("top_ten:", top_datasets)

            data_metrics = [
                {
                    # "id": dataset[0]["id"],
                    # "metadata": dataset[0]["metadata"],
                    "ddo": dataset[0],
                    "data_format_consistency": self.evaluate_data_format_consistency(
                        dataset[0]
                    ),
                    "completeness": self.evaluate_completeness(dataset[0]),
                    "geo_coverage": self.evaluate_geographical_coverage(dataset[0]),
                    "metadata_availability": self.evaluate_metadata_availability(
                        dataset[0]
                    ),
                    "temporaral_coverage": self.evaluate_temporal_coverage(dataset[0]),
                    "overall_quality": self.evaluate_data_quality(dataset[0]),
                }
                for dataset in top_datasets
            ]

            return data_metrics
