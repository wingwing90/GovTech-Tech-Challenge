import pandas as pd
import numpy as np

csv_file = r"C:\Users\wingw\Documents\repo\GovTech-Tech-Challenge\section5\car.csv"

print(csv_file)

raw_df = pd.read_csv(csv_file,sep=',')

print(raw_df)