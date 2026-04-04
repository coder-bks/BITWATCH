import requests
from config import COINGECKO_KEY

def scrapping():
    try:
        response = requests.get(
            "https://api.coingecko.com/api/v3/simple/price",
            params={
                "ids": "bitcoin",
                "vs_currencies": "inr,usd"
            },
            headers={"x-cg-demo-api-key": COINGECKO_KEY},
            timeout=10
        )
        if response.status_code == 200:
            data = response.json()
            inr_price = data["bitcoin"]["inr"]
            usd_price = data["bitcoin"]["usd"]
            return f"Bitcoin — INR: ₹{inr_price:,} | USD: ${usd_price:,}"
        else:
            raise ValueError(f"API returned {response.status_code}")
    except Exception as e:
        raise ValueError(f"website not reachable or crashed: {e}")

# def scrapping():
#     url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=inr,usd"
#     response = requests.get(url)
#     if response.status_code==200:
#         try:
#             data = response.json()
#             inr_price = data["bitcoin"]["inr"]
#             usd_price = data["bitcoin"]["usd"]
#             return f"Bitcoin — INR: ₹{inr_price} | USD: ${usd_price}"
#         except KeyError as e:
#             print(f"A key error occurred: {e}. Check your dictionary structure.")
#     else:
#         raise ValueError("website not reachable or crashed")


