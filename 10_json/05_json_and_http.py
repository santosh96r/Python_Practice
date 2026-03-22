import json
from urllib.request import urlopen

with urlopen("https://finance.yahoo.com/markets/currencies/") as response:
    source = response.read()

data = json.loads(source)

datajson = json.dumps(data, indent = 4 )

print(datajson)