import os
import csv
import pandas as pd

from datetime import date, datetime, timedelta

from airflow import DAG

version = 1
default_args = {
    "start_date": datetime(2023, 2, 17, 0, 0, 0),
    "retries": 2,
    "max_active_runs": 1,
    "retry_delay": timedelta(minutes=1),
}

def filter_data():
    df = pd.read_csv("applications_dataset_1.csv",sep=',',)

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
    

