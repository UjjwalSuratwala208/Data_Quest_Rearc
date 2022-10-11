# imoport necesarry libraries

import requests
import json
import pandas as pd

url = ("https://datausa.io/api/data?drilldowns=Nation&measures=Population")
r = requests.get(url)
r.json()


# to store the data into a JSON file - writing population.json

with open("population.json", "w") as outfile:
     json.dump(r.json(), outfile)