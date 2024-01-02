import os, dotenv, requests
from datetime import datetime, timedelta
from crawling import WebCrawling
from web_address import ko_sources

dotenv.load_dotenv()
sheety_endpoint_ko = os.getenv('SHEETY_ENDPOINT_KO')
bearer_header = {
    "Authorization": f"Bearer {os.getenv('BEARER_HEADER')}"
}

body = {'news': {}}
today = datetime.now()
today_formatted = today.strftime("%Y/%m/%d")
yesterday = today - timedelta(days=1)
yesterday_formatted = yesterday.strftime("%Y/%m/%d")
week_today = today.weekday()
week_yesterday = yesterday.weekday()


# TODO 1. Korean Newspapers
for key, url in ko_sources.items():
    crawled = WebCrawling(url)
    crawled_news = crawled.news('._persist_wrap > div:nth-child(1) > div:nth-child(1) .newspaper_brick_item._start_page li')
    body['news'][key] = crawled_news

body['news']['date'] = today_formatted
body['news']['week'] = week_today
sheety_response = requests.post(sheety_endpoint_ko, json=body, headers=bearer_header)
sheety_response.raise_for_status()
print(body)

for key, url in ko_sources.items():
    del body['news'][key]

print(body)


# TODO 2. English Newspapers


# TODO 3. Japanese Newspapers


# TODO 4. European Newspapers


# TODO 5. Chinese Newspapers


