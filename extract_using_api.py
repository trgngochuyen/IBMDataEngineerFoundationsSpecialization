import requests
import pandas as pd 
import config

api_key = config.api_key

url = f'http://api.exchangeratesapi.io/v1/latest?access_key={api_key}'
response = requests.get(url)

rates = dict(response.json())['rates']
df = pd.DataFrame(list(rates.items()), columns=["Currency", "Rate"])

# Save the Dataframe
csv_file = df.to_csv(index=False)