import os
import requests
import scrape_data
from bs4 import BeautifulSoup




def get_week_menu():
    res = requests.get('https://www.sammen.no/no/bergen/mat/hoyteknologisenteret')
    if res.status_code != 200:
        print(res.staus_code)
        quit()

    soup_data = BeautifulSoup(res.text, 'html.parser')


    week_menu = soup_data.find(id='weekmenu')
    week_menu = map(lambda x: str(x)[3:-4].strip().replace('\n', ' '), week_menu.find_all('p'))
    return str(list(week_menu))

token = os.environ.get('TOKEN')

week_menu = get_week_menu()

url = 'https://slack.com/api/chat.postMessage'
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer " + token,
    }
myobj = {
    'channel': 'dev', 
    'text': week_menu,
    }

x = requests.post(url, headers=headers, json = myobj)
print("Status Code", x.status_code)

