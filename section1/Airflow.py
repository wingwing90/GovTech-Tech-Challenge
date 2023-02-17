import os
import glob
import csv
import pandas as pd

import re

from datetime import date, datetime, timedelta

from airflow import DAG

version = 1
default_args = {
    "start_date": datetime(2023, 2, 17, 0, 0, 0),
    "retries": 2,
    "max_active_runs": 1,
    "retry_delay": timedelta(minutes=1),
}

def latest_file():
    folder_path = r"GovTech-Tech-Challenge\section1\input_file"
    file_type = r'\*.csv'
    files = glob.glob(folder_path + file_type)
    latest_file = max(files, key=os.path.getctime)
    print(latest_file)

    return latest_file

def filter_data():
    df = pd.read_csv(latest_file(),sep=',')

    success_df = df[(df['mobile_no'] == re.match(pattern="^\d{8}$", string=in_str)) & (df['email'] == re.match(pattern="\b[A-Za-z0-9_-]+@[A-Za-z0-9.-]+\.(com|net)\b", string=in_str))]

    fail_df = 

with DAG(
    dag_id=f"psp-isbank-fetcher-v{version}",
    description="Fetch reports from Isbank and load to Datahub",
    schedule_interval=" 0 * * * * ",
    default_args={**DAG_DEFAULT_ARGS, **default_args},
    max_active_runs=1,
    tags=[DAG_DEFAULT_ARGS["owner"], "dwh"],
    catchup=False,
    on_failure_callback=alerts.setup_on_failure_callback(),
) as dag:

    FilterData = PythonOperator(
        task_id = "FilterData",
        python_callable = filter_data
    )
    

