import pandas as pd
from typing import Text
import os


def read_data(file_path: Text) -> pd.DataFrame:
    csv_file = pd.read_csv(file_path)
    csv_file["Order Date"] = pd.to_datetime(csv_file["Order Date"], infer_datetime_format=True)
    return csv_file


dataset_url = os.path.abspath("train.csv")
df = read_data(dataset_url)
