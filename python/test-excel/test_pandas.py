import pandas as pd

df = pd.read_excel('test.xlsx')
print(df.to_json())
