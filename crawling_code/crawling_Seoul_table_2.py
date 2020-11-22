import pandas as pd
import numpy as np

url = "https://www.seoul.go.kr/coronaV/coronaStatus.do"
print(url)

table = pd.read_html(url)
print(len(table))

df = table[0]
print(df)

df.transpose()

print(df.loc[0])

file_name = f"seoul-covid19_.csv"
print(file_name)

df.to_csv(file_name ,index =False)

pd.read_csv(file_name)
