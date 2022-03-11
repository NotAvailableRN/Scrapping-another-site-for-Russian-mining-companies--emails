import requests
import json
import urllib
import csv

def get_data(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.121 Safari/537.36" #header was taken directly from site
    }
    all_data = []
    y = 1
    for item in range(1, 84):#info is downloaded via JSON file - total number of pages that we are looking for on site is 84
        req = requests.get(url + f"{item}", headers) 
        json_response = req.json() 
        for i in range(0, 10): #each JSON reply has 10 values with info
            try:
                email = (json_response["Page"][i]["Email"]) #iterating through them
            except:
                email = ("No email")
            all_data.append(email)
            print(y) #just to see how many entries we have
            y+=1

    with open(file='data.csv', mode='w', encoding="utf-8", newline='') as file:
        writer = csv.writer(file, delimiter='\t')

        for data in all_data:
            writer.writerow(data)

get_data("https://whoiswho.dp.ru/api/Company/ListForSpecialization?specializationId=8106&pageSize=12&pageNumber=") #the site that we use
