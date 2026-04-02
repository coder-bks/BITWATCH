import requests

def scrapping():
    try:
        # BTC/USD from Binance
        btc_response = requests.get(
            "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT",
            timeout=10
        )
        # USD to INR conversion
        inr_response = requests.get(
            "https://api.exchangerate-api.com/v4/latest/USD",
            timeout=10
        )
        
        if btc_response.status_code == 200 and inr_response.status_code == 200:
            usd_price = float(btc_response.json()["price"])
            usd_to_inr = inr_response.json()["rates"]["INR"]
            inr_price = round(usd_price * usd_to_inr, 2)
            return f"Bitcoin — INR: ₹{inr_price:,.2f} | USD: ${usd_price:,.2f}"
        else:
            raise ValueError("Price API failed")
            
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


