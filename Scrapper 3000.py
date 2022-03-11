import bs4
import requests
import json
import urllib
import csv

def get_data(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.121 Safari/537.36"
    }
    all_data = []
    i = 1
    for item in range(1, 84):
        req = requests.get(url + f"{item}", headers)
        json_response = req.json()
        for i in range(0, 10):
            try:
                email = (json_response["Page"][i]["Email"])
            except:
                email = ("No email")
            all_data.append(email)
            print(i)
            i+=1

    with open(file='data.csv', mode='w', encoding="utf-8", newline='') as file:
        writer = csv.writer(file, delimiter='\t')

        for data in all_data:
            writer.writerow(data)

get_data("https://whoiswho.dp.ru/api/Company/ListForSpecialization?specializationId=8106&pageSize=12&pageNumber=")