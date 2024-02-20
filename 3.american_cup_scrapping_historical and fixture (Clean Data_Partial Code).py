#Partial Code

import pandas as pd

df = pd.read_csv("american_cup_fixture.csv")
df2 = pd.read_csv("american_cup_historical_data.csv")

#Cleaningn df fixture

df["home"]=df["home"].str.strip()
df["away"]=df["away"].str.strip()
df["score"]=df["score"].str.strip()
df.replace({"Concacaf 5": "Canadá", "Concacaf 6": "Costa Rica"},inplace=True)

#Cleaning df2 historical
#df2[df2["home"].isnull()]
df2.dropna(inplace=True)
df2.shape
