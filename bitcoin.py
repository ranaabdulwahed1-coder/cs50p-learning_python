import requests
import sys


try:
    if len(sys.argv) == 2:
        amount = float(sys.argv[1])
        r = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd")
        o = r.json()
        price = o["bitcoin"]["usd"]
        total = amount * price
        print(f'${total: ,.4f}')
    else:
        sys.exit('missing command line')
except ValueError:
    sys.exit()
