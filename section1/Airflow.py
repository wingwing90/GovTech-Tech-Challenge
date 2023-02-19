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
    raw_df = pd.read_csv(latest_file(),sep=',')

    print(raw_df)
    
    name_df = raw_df[['name']]
    
    print(name_df)
    
    first_last_name_df = raw_df.name.str.split(" ", 1,expand=True)
    rename_first_last_name_df = first_last_name_df.rename(columns={0:'first_name', 1:'last_name'})
    
    print(rename_first_last_name_df)
    
    split_name_df = pd.concat([rename_first_last_name_df, raw_df.drop(['name'], axis=1)], axis=1)
    
    print(split_name_df)
    
    split_name_df['date_of_birth'] = pd.to_datetime(split_name_df.date_of_birth)
    # .dt.strftime('%Y%m%d')
    
    format_date_df = split_name_df
    
    print("format_date_df")
    print(format_date_df)

    fil_mobile_email_df = format_date_df[(format_date_df['mobile_no'].str.contains("(\d{8})")) & (format_date_df['email'].str.match("[A-Za-z0-9_-]+@[A-Za-z0-9.-]+\.(com|net)"))]

    print(fil_mobile_email_df)

    success_df = fil_mobile_email_df[(fil_mobile_email_df['date_of_birth']) < "2006-01-01"]

    print(success_df)
    
    success_df.to_csv(r"GovTech-Tech-Challenge\section1\output_file\success.csv", sep=';', encoding='utf-8')
    
    failure_df = raw_df[~raw_df.index.isin(success_df.index)]
    
    print(failure_df)
    
    failure_df.to_csv(r"GovTech-Tech-Challenge\section1\output_file\fail.csv", sep=';', encoding='utf-8')

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
    

