import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

csv_file = r"C:\Users\wingw\Documents\repo\GovTech-Tech-Challenge\section5\car.csv"

print(csv_file)

raw_df = pd.read_csv(csv_file,sep=',')

print(raw_df)

raw_df['buying'] = raw_df['buying'].map({'vhigh': 4,'high': 3,'med': 2,'low': 1})
raw_df['maint'] = raw_df['maint'].map({'vhigh': 4,'high': 3,'med': 2,'low': 1})
raw_df['doors'] = raw_df['doors'].map({'2': 2,'3': 3,'4': 4,'5more': 5})
raw_df['persons'] = raw_df['persons'].map({'2': 2,'4': 4,'more': 5})
raw_df['lug_boot'] = raw_df['lug_boot'].map({'small': 1,'med': 2,'big': 3})
raw_df['safety'] = raw_df['safety'].map({'low': 1,'med': 2,'high': 3})
raw_df['class'] = raw_df['class'].map({'unacc': 0.70023,'acc': 0.22222,'good': 0.03993,'vgood': 0.03762})

print(raw_df)

df_test, df_train = train_test_split(raw_df, test_size = 0.2, random_state = 1)

print(df_train)

regressor = LinearRegression

regressor.fit(df_train)