import requests
from bs4 import BeautifulSoup


def scrapping():
    url = "https://quotes.toscrape.com"
    response = requests.get(url)
    if response.status_code==200:
    
        soup = BeautifulSoup(response.text, "html.parser")
        quotes = soup.find("span", class_="text")
        results = quotes.text
            
        return results
    else:
        raise ValueError("website not reachable or crashed")


data =scrapping()

# print(data)