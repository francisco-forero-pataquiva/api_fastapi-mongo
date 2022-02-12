import schedule
import time
from database.db_populator import api_scrapper

def job():
    api_scrapper()

schedule.every().day.at("22:54").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)