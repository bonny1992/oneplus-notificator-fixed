from bs4 import BeautifulSoup
import requests
from time import sleep
import datetime
from os import system

title = "Oneplus Notificator"

system("title "+title)

CHECK_URL = "https://oneplus.net/it/oneplus-3t"
NOTIFY_URL = "https://www.notifymyandroid.com/publicapi/notify"

payload = {
    "apikey": "975edbd8205e0391206d82a8e617683c1dc97c101bd29c5d",
    "application": "Oneplus Notificator",
    "event": "",
    "description": "",
    "priority": 0,
    "url": CHECK_URL,
    "content-type": "text/html"
}

executions = 1
prenotable = False

while True:
    print("[{}] Esecuzione n. {}".format(datetime.datetime.now(), executions))
    html_source = requests.get(CHECK_URL).text
    soup = BeautifulSoup(html_source, 'html.parser')
    radio_128 = soup.find(id = "phone_model2")
    radio_gunmetal = soup.find(id = "405")
    if radio_128 and radio_gunmetal:
        if prenotable == False:
            payload["event"] = "Prenotabile!"
            payload["description"] = "Il Oneplus 3T 128gb è <b>prenotabile</b>!"
            print("[{}] Prenotabile!".format(datetime.datetime.now()))
            request = requests.post(NOTIFY_URL, data=payload)
            prenotable = True
        else:
            print("[{}] Prenotabile, ma non verrà notificato.".format(datetime.datetime.now()))
    else:
        if prenotable == True:
            payload["event"] = "Non più prenotabile!"
            payload["description"] = "Il Oneplus 3T 128gb <b>non è più prenotabile</b>!"
            print("[{}] Non prenotabile!".format(datetime.datetime.now()))
            request = requests.post(NOTIFY_URL, data=payload)
            prenotable = False
        else:
            print("[{}] Non prenotabile, ma non verrà notificato.".format(datetime.datetime.now()))
    executions += 1
    print("[{}] Attendo per un'ora".format(datetime.datetime.now()))
    i = 0
    while True:
        sleep(1)
        i += 1
        if i > 299:
            break
