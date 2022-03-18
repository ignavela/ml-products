import requests
import json

seller_id = input("Please enter the seller id: ")
base_url = 'https://api.mercadolibre.com/sites/MLA/search?seller_id={}'
url = base_url.format(seller_id)
response_API = requests.get(url)

data = response_API.json()

print(json.dumps(data["results"], indent = 4, sort_keys = True))