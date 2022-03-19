import requests
import json
import argparse
import configparser

### Multiple seller_ids can be sent through CLI arguments
parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('seller_ids', metavar='N', type=int, nargs='+',
                    help='an integer for the accumulator')

args = parser.parse_args()
seller_ids = args.seller_ids
print(seller_ids)

### Read config file
config = configparser.ConfigParser()
config.read('dev.ini')
print(config['DEFAULT']['Host'])

### Iterate through all ids to call the API for each id
for id in seller_ids:
  url = f"{config['DEFAULT']['Host']}/search?seller_id={id}"

  response_API = requests.get(url)

  results = response_API.json()["results"]

  ### Iterate through all item for each seller id 
  output = []
  for r in results:
    output.append(
      {
        'id': r['catalog_product_id'],
        'title': r['title'],
        'category_id': r['category_id'],
        'name': r['domain_id'],
        'seller': id
      }
    )

  # TODO: Send to file
  print(json.dumps(output, indent=4))