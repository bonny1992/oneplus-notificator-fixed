import math
import requests
import datetime

from bs4 import BeautifulSoup
from time import sleep
from os import system

def secs_to_time(seconds):
    if seconds < 60:
        return "{seconds} secondi".format(
        seconds = seconds
        )
    else:
        if int(seconds / 60 / 60 / 24) > 0:
            days = seconds / 60 / 60 / 24
            return "{days} giorni, {hours} ore, {minutes} minuti, {seconds} secondi".format(
            days = int(days),
            hours = int((math.ceil((days - int(days)) * 24))),
            minutes = int((math.ceil((days - int(days)) * 24 * 60))),
            seconds = int(math.ceil((days - int(days)) * 24 * 60 * 60))
            )
        elif int(seconds / 60 / 60) > 0:
            hours = seconds / 60 / 60
            return "{hours} ore, {minutes} minuti, {seconds} secondi".format(
            hours = int(hours),
            minutes = int((math.ceil((hours - int(hours)) * 60))),
            seconds = int((math.ceil((hours - int(hours)) * 60 * 60)))
            )
        elif int(seconds / 60) > 0:
            minutes = seconds / 60
            return "{minutes} minuti, {seconds} secondi".format(
            minutes = int(minutes),
            seconds = int(((minutes - int(minutes)) * 60 ))
            )

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
seconds = 299

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
            print("[{}] Prenotabile! Notifica in invio...".format(datetime.datetime.now()))
            request = requests.post(NOTIFY_URL, data=payload)
            prenotable = True
        else:
            print("[{}] Prenotabile, ma non verrà notificato.".format(datetime.datetime.now()))
    else:
        if prenotable == True:
            payload["event"] = "Non più prenotabile!"
            payload["description"] = "Il Oneplus 3T 128gb <b>non è più prenotabile</b>!"
            print("[{}] Non prenotabile! Notifica in invio...".format(datetime.datetime.now()))
            request = requests.post(NOTIFY_URL, data=payload)
            prenotable = False
        else:
            print("[{}] Non prenotabile, ma non verrà notificato.".format(datetime.datetime.now()))
    executions += 1
    print("[{}] Attendo per {time}".format(datetime.datetime.now(),
    time = secs_to_time(seconds + 1)))
    i = 0
    while True:
        sleep(1)
        i += 1
        if i > 299:
            break
