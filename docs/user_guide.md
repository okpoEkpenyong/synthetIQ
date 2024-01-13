# SynthetIQ: AI Recommendation System for Ocean Data Marketplace

## 1. Introduction

SynthetIQ is an AI-driven recommendation system designed to enhance the Ocean Data Marketplace experience, thereby improving it's business value. It leverages a Flask backend and a custom React frontend (forked Ocean Marketplace) to provide users with personalized dataset recommendations. This build which is meant as a proof of concept, evaluates data quality using metrics like completeness, temporal coverage, geographical coverage, and more, targeting only climate-specific dataset. The filtering algorithm is however powerful enough to handle different groupings of filter or tags ranging from health to compute or any useful search. This documentation outlines the installation, configuration, and usage of SynthetIQ.

## 2. Installation

### 2.1 Prerequisites

- Python 3.10+
- Flask
- React
- ...

### 2.2 Installation Steps

1. Clone the SynthetIQ repository: `git clone <repository-url>`
2. Create a virtual envirinment and install Python dependencies: `pip install -r requirements.txt`
3. Install Node.js dependencies: `cd frontend && npm install`

## 3. Configuration

The configuration file is located at `config.py`. Update the file with your specific settings, such as API keys and database connections.

## 4. Usage

### 4.1 Starting the Application

- Navigate to the folder flask_backend and run: `python app.py`. Please note that the setup is only for development purposes hence the configurations like CORS and localhost
- Start the React frontend: `cd frontend && npm start`

### 4.2 Accessing the API

The API is accessible at `http://localhost:5000/api/recommendations`. Refer to the API documentation for available endpoints.

### 4.3 Interacting with the Frontend

Open the SynthetIQ frontend in your browser at `http://localhost:8000`. The user interface provides a customized Ocean Marketplace experience for exploring recommended climate-related datasets.

## 5. Endpoints

This aspect is work in progress.

## 6. Data Models

### 6.1 Dataset Model

In this iteration, we do not have a database, but rely on Aquarius, an offline caching system implemented by the Ocean Protocol. This worked excellently for this build as discovered a query that could pull the entire datasets from different networks.

```json
{
  "id": "string",
  "metadata": {
    // Dataset metadata fields
  },
  "quality_metrics": {
    // Quality metrics for the dataset
  }
}
```

## 7. User Interface

The UI is a simple system of grids that displays the filtered recommended system sent from the Flask backend. In future iterations we intend to improve on the rating system by adding community feedback features and adopting advance AI filtering systems to enhance the recommendation and personalization.

# 8. Integration & Benefit of the Innovation

This benefits of attaching a well researched and AI driven rating system to the Marketplace is huge. Many papers have been written on how to improve data quality via metadata metrics. I believe the C2D feature of the OPF will further enhance this rating system as users will be able to use our system to verify the datasets quality in addition to the metadata. SynthetIQ seamlessly integrates Ocean Technology features into its architecture, demonstrating a high level of compatibility and synergy. The project effectively uses Ocean Protocol's core components, including decentralized datatokens, and asset metadata standards, to ensure a cohesive and efficient system

# 9. Limitations

Currently the system relies on metadata data solely and is based only on climate datasets.

## 8. License

This project is licensed under the MIT License.
