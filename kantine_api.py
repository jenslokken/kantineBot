import os
import requests
import scrape_data
from bs4 import BeautifulSoup
import datetime



def get_week_menu():
    res = requests.get('https://www.sammen.no/no/bergen/mat/hoyteknologisenteret')
    if res.status_code != 200:
        print(res.staus_code)
        quit()

    soup_data = BeautifulSoup(res.text, 'html.parser')


    week_menu = soup_data.find(id='weekmenu')
    week_menu = map(lambda x: str(x)[3:-4].strip().replace('\n', ' ').replace('.', ''), week_menu.find_all('p'))
    return list(week_menu)

week = ["mandag", "tirsdag", "onsdag", "torsdag", "fredag"]

token = os.environ.get('TOKEN')

week_menu = get_week_menu()
today = datetime.date.today().weekday()

url = 'https://slack.com/api/chat.postMessage'
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer " + token,
    }
myobj = {
    'channel': 'dev', 
    'text': "I dag er det mest sannsynlig *" + week_menu[today].lower() + "* i kantinen på høytek.:tobwat:",
    }

x = requests.post(url, headers=headers, json = myobj)
print("Status Code", x.status_code)
