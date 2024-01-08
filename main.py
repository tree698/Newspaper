import os, dotenv, requests
from datetime import datetime, timedelta
from crawling import WebCrawling
from web_address import ko_jp_sources, ko_jp_selector, en_sources, en_selector

dotenv.load_dotenv()
sheety_endpoint_ko = os.getenv('SHEETY_ENDPOINT_KO')
sheety_endpoint_en = os.getenv('SHEETY_ENDPOINT_EN')
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


def save(date, name_, news):
    if len(news) == 0 or news == 'NaN':
        print(f'{date} | {name_} is empty.')
    news_list = news.split('&&&')
    for news in news_list:
        with open('news.txt', 'a') as content:
            content.write(f'{date} | {name_} | {news}\n')


def sheety(endpoint, body_, headers):
    response_ = requests.post(endpoint, json=body_, headers=headers)
    response_.raise_for_status()
    return response_


def reset_body(source):
    for key, url in source.items():
        del body['news'][key]


# TODO 1. Korean + Japanese Newspapers
for key, url in ko_jp_sources.items():
    crawled = WebCrawling(url)
    if key == 'asahimorning':
        crawled_news = crawled.jp_news(ko_jp_selector['asahimorning'])
    elif key == 'asahinight':
        crawled_news = crawled.jp_news(ko_jp_selector['asahinight'])
    else:
        crawled_news = crawled.news(ko_jp_selector['selector'])
    body['news'][key] = crawled_news
    save(today_formatted, key, crawled_news)

body['news']['date'] = today_formatted
body['news']['week'] = week_today
# sheety(sheety_endpoint_ko, body, bearer_header)
print(body)
reset_body(ko_jp_sources)


# TODO 2. English Newspapers
for key, url in en_sources.items():
    crawled = WebCrawling(url)
    if key == 'wsj':
        crawled_news = crawled.wsj_news(en_selector[key])
    else:
        crawled_news = crawled.news(en_selector[key])
    body['news'][key] = crawled_news
    save(yesterday_formatted, key, crawled_news)

body['news']['date'] = yesterday_formatted
body['news']['week'] = week_yesterday
# sheety(sheety_endpoint_en, body, bearer_header)
print(body)
reset_body(en_sources)











