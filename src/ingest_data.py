#####################################################################
#                       Data Ingestion Step                         #
#####################################################################

import kagglehub
#from kagglehub import KaggleDatasetAdapter
import os
from os.path import join as join
import pandas as pd
import logging
import geopandas as gpd
from shapely import wkt

# Configure logging
logging.basicConfig(format="%(asctime)s: %(message)s", level=logging.INFO, force=True)
logger = logging.getLogger(__name__)

# Output directory for datasets
output_dir = r"C:\Users\smomt\OneDrive\Documents\work\Interview\Aurora\Take Home\data"

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Kaggle dataset description:
# https://www.kaggle.com/datasets/sobhanmoosavi/us-road-construction-and-closures
repo = "sobhanmoosavi/us-road-construction-and-closures"
file_name = "US_Constructions_Dec21"

# Route file details
rt_file_dir = r"C:\Users\smomt\OneDrive\Documents\work\Interview\Aurora\Take Home"
rt_file_name = "sf_paths (2).csv"
out_rt_file_name = "sf_paths.parquet"


def get_data_csv(repo: str, file_name: str) -> pd.DataFrame:
    """
    Download dataset from Kaggle and convert it to parquet format
    
    Reference: https://github.com/Kaggle/kagglehub
    """

    logger.info("Download the dataset from Kaggle")
    dataset_path = kagglehub.dataset_download(repo, force_download=True)
    file_path = f"{dataset_path}/{file_name}.csv"

    logger.info("Load the csv file")
    df = pd.read_csv(file_path, low_memory=False)

    return df



def save_parquet(df: pd.DataFrame, file_name: str):
    """
    Save DataFrame as parquet file
    """
    
    logger.info(f"Saving DataFrame to {file_name}.parquet")
    df.to_parquet(f"{file_name}.parquet", engine="pyarrow")


    
def convert_route_file_to_geoparquet(rt_file_dir: str, rt_file_name: str) -> None:
    """
    Convert the route file to geodataframe and save as geoparquet file
    """
    
    logger.info("Converting route file to parquet format")
    df_routes = pd.read_csv(join(rt_file_dir, rt_file_name), low_memory=False)

    logger.info("Generating geometry from WKT linestrings")
    df_routes["geometry"] = df_routes["path_wkt"].apply(wkt.loads)

    logger.info("Converting DataFrame to GeoDataFrame")
    df_routes.drop(columns=["path_wkt"], inplace=True)
    gdf_routes = gpd.GeoDataFrame(df_routes, geometry="geometry")

    logger.info("Setting CRS to WGS84 (EPSG:4326)")
    gdf_routes.set_crs(epsg=4326, inplace=True)
    
    logger.info(f"Saving GeoDataFrame to {out_rt_file_name}")
    gdf_routes.to_parquet(join(rt_file_dir, out_rt_file_name), engine="pyarrow", index=False)

    
def run_ingest():
    """Run ingestion tasks"""
    logger.info("Start data ingestion")

    logger.info("Start processing route file...")
    convert_route_file_to_geoparquet(rt_file_dir, rt_file_name)
    
    logger.info("Start processing Kaggle dataset...")
    save_parquet(get_data_csv(repo, file_name), file_name)

if __name__ == "__main__":
    run_ingest()

