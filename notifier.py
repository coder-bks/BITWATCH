import requests
from config import TOKEN,CHAT_ID


def notify(message):
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={message}'
    response = requests.get(url)
    if response.status_code==200:
        return True
    else:
        raise ValueError("website not reachable or crashed")


