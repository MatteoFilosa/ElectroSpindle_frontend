import requests
import pandas as pd

x = requests.get('http://arca.diag.uniroma1.it:8082/rodaggi/spindles/1/raw_data?limit=100')
df = pd.DataFrame(x.json()['data'])
print(df.head())
