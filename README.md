# us_road_construction

The repository is exercise of a hypothetical scenarios and analytics,

## About Dataset
### Description
This is a countrywide dataset of road construction and closure events, which covers 49 states of the US. Construction events in this dataset could be any roadwork, ranging from fixing pavements to substantial projects that could take months to finish. The data is collected from Jan 2016 to Dec 2021, using multiple APIs that provide streaming traffic incident (or event) data. These APIs broadcast traffic data captured by a variety of entities, such as the US and state departments of transportation, law enforcement agencies, traffic cameras, and traffic sensors within the road-networks. Currently, there are about 6.2 million construction and closure records in this dataset.

### Acknowledgements
_Karimi Monsefi, Amin, Sobhan Moosavi, and Rajiv Ramnath. “Will there be a construction? Predicting road constructions based on heterogeneous spatiotemporal data.”, In Proceedings of the 30th ACM SIGSPATIAL 2022._

#### Approach to Construction Impact Analysis
##### Autonomous Vehicle Deployment Strategy & Risk Assessment
- **Goal 1:** A comprehensive analysis of US road construction for AV deployment strategy
- **Goal 2:** A risk assessment comparison among specific routes in Bay Area CA 
- **Goal 3:** A predictive model development to estimate construction duration proactively

#### Goal 1: __A comprehensive analysis of US road construction for AV deployment strategy__

##### Targets:
- Ingest Data
    - Get data from Kaggle
    - Prepare parquet data
- Intial Explanatory Data Analytics
    - Stats
    - Maps showing constructions
- Feature Extractions
- Top construction activity by cities
- Time series trends by cities
- Compare among cities

#### Goal 2: __A risk assessment comparison among specific routes in Bay Area CA__

##### Targets:
- Matching/tagging construction activity using spatial query
- Mapping the construction for interactive data explore by year, severity and other KPIs
- Generating a risk score
- Idea for extra miles to go

#### Goal 3: __A predictive model development to estimate construction duration proactively__

##### Targets:
- Explore corelation between duration and other variables
- Predict simple models
- Any advance models
- Idea for extra miles to go
- 
#### Data Processing Approach
- Ingest Kaggle data using API
- Store data in parquet format
- Get the additional data
    - Census population, employment
    - National Road network for frieghts: to get the road density of cities - generating city size to normalize
- Extract features from additional files

## File Structure
### src:
Folder contain code for ingesting data - very first step

### Notebook:
Contains the notebook to analyze and visualize the data

### Presentation:
Contain slide deck (darft) for showcasing the outcome

### .kaggle
Folder to hold credential for Kaggle API (currently a dummy file)

### env.yaml
Python Environment file

