from datetime import datetime
from pathlib import Path
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

### Read config file
config = configparser.ConfigParser()
config.read('dev.ini')
log_dir = config['DEFAULT']['log_dir']

output = []

### Iterate through all ids to call the API for each id
for id in seller_ids:
  url = f"{config['DEFAULT']['Host']}/search?seller_id={id}"

  response_API = requests.get(url)

  results = response_API.json()["results"]

  ### Iterate through all item for each seller id
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

file_path = Path(f"logs/{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt")

###Create log file, write the output of the API and save it in path given in log_dir
with open(file_path, 'w') as file:
    file.write(json.dumps(output, indent=2, sort_keys=True))
