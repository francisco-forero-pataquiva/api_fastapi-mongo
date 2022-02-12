import requests
from db import collection,do_count
import asyncio

def api_scrapper():
    url_count ='https://api.spaceflightnewsapi.net/v3/articles/count'
    count_api = int(requests.get(url_count).text)
    count_db = asyncio.get_event_loop().run_until_complete(do_count())
    if count_api != count_db:
        if count_db > count_api:
            print("There are duplicates")
                #print duplicated ids
        else:
            delta = count_api-count_db
            index_global=count_api-delta
            print(f"There are {delta} articles to include")
            while index_global < count_api:
                print(index_global)
                index = 0
                url = f'https://api.spaceflightnewsapi.net/v3/articles?_limit=50&_start={index_global}'
                response = requests.get(url)
                data = response.json()
                for _ in data:
                    collection.insert_one(data[index])
                    index+=1
                    index_global+=1
    else:
        print("Database updated!")
