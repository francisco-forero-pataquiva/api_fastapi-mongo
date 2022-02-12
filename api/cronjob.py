import schedule
import time
from db_populator import api_scrapper


def job():
    api_scrapper()

schedule.every().day.at("09:00").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)