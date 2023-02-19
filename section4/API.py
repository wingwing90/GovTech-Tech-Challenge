import requests
import pandas as pd
import matplotlib.pyplot as plt

response = requests.get('https://api.covid19api.com/total/dayone/country/singapore/status/confirmed')

df = pd.DataFrame.from_dict(response.json())

print(df)

plt.plot(df["Date"], df["Cases"])
plt.show()