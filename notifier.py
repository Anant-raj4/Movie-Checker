import requests
import os

url = "https://unogs-unogs-v1.p.rapidapi.com/search/deleted"


def get_info():
    querystring = {"limit": "5", "country_list": "IN", "title": "3 Idiots"}

    headers = {
        "X-RapidAPI-Key": "2c7c38c414mshe73f464b755052bp1ad20ajsn93ce58ea9c5a",
        "X-RapidAPI-Host": "unogs-unogs-v1.p.rapidapi.com"
    }

    response = requests.request(
        "GET", url, headers=headers, params=querystring)
    print(response.text)
    title = response["name"].text
    summary = response["type"].text
    return title, summary


def sender(title, summary):
    response = requests.post('https://api.mynotifier.app', {
        "apiKey": '74ad268d-6cf5-484f-8d04-e01afac9eec9',
        "message": title,
        "description": summary,
        "type": "info",
    })


get_info()
sender(title, summary)
