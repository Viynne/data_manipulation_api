import pandas as pd
import numpy as np
from typing import Text
import os
from database.connection import read_data

from fastapi import APIRouter

route_sales = APIRouter()
dataset_url = os.path.abspath("train.csv")
# df = pd.read_csv(dataset_url)


def desired_output_format(data: pd.DataFrame) -> dict:
    return_json = {}
    for i, j in data.items():
        return_json[i] = data[i].tolist()
    return return_json


@route_sales.get("/sales/plot_one/{period}")
async def order_sales(period: Text) -> dict:
    df = read_data(dataset_url)
    sales_by_order = df[["Order Date", "Sales"]]
    sales_by_order.set_index(keys="Order Date", inplace=True)
    sales_by_period = sales_by_order.resample(period[0]).sum()
    sales_by_period.reset_index(inplace=True)
    sales_by_period["Order Date"] = sales_by_period["Order Date"].dt.strftime("%Y-%m-%d")
    sales_by_period["Sales"] = sales_by_period["Sales"].astype(int)
    output_response = desired_output_format(sales_by_period)
    return output_response


# df_sales = order_sales(df, "Year")
#
# r_df = desired_output_format(df_sales)
