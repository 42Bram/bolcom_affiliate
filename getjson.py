import json
import requests
from config import bolapi

def get(category):
    jsonfile = requests.get('https://api.bol.com/catalog/v4/lists/?ids=' + category[
        1] + '&apikey=' + bolapi + '&format=json&sort=rankasc&limit=100&offset=100')
    jsondata = jsonfile.json()
    with open("JSON/" + category[0] + ".json", 'w', encoding='utf8') as f:
        json.dump(jsondata, f, ensure_ascii=False, indent=4)
