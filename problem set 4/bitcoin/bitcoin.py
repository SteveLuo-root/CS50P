import sys
import requests

if len(sys.argv) != 2:
    sys.exit("missing command-line argument")

try:
    n = float(sys.argv[1])
except ValueError:
    sys.exit("invalid command-line argument")

try:
    response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=a76bb3f9edb71b9aa9337dea54c0f6b6bfeb73ef9f7207e2f3ebfd3b4d0192e7")
    output = response.json()
    price = float(output["data"]["priceUsd"])
    print(f"${(price*n):,.4f}")
except requests.RequestException:
    sys.exit("api request failed")
