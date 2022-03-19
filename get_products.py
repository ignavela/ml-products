import requests
import json

#TODO: upgrade the input to receive more than one user


seller_id = input("Please enter the seller id: ")

url = f'https://api.mercadolibre.com/sites/MLA/search?seller_id={seller_id}'

# We call the API passing the user id provided

response_API = requests.get(url)

# Pass the result to .json

data = response_API.json()

# Filter by just "results" attribute

items = data["results"]

# Here we iterate through all items from seller id

output = []
for i in items:
  output.append(
    {
      'id': i['catalog_product_id'],
      'title': i['title'],
      'category_id': i['category_id'],
      'name': i['domain_id']
    }
  )

# TODO: Send to file
print(json.dumps(output, indent=4))