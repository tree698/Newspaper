import os, dotenv, requests
from datetime import datetime, timedelta
from crawling import WebCrawling
from web_address import ko_sources, ko_selector, en_sources, en_selector

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
    if len(news) == 0:
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


# TODO 1. Korean Newspapers
for key, url in ko_sources.items():
    crawled = WebCrawling(url)
    crawled_news = crawled.news(ko_selector['selector'])
    body['news'][key] = crawled_news
    save(today_formatted, key, crawled_news)

body['news']['date'] = today_formatted
body['news']['week'] = week_today
sheety(sheety_endpoint_ko, body, bearer_header)
print(body)
reset_body(ko_sources)


# TODO 2. English Newspapers
for key, url in en_sources.items():
    crawled = WebCrawling(url)
    crawled_news = crawled.news(en_selector[key])
    body['news'][key] = crawled_news
    save(yesterday_formatted, key, crawled_news)

body['news']['date'] = yesterday_formatted
body['news']['week'] = week_yesterday
sheety(sheety_endpoint_en, body, bearer_header)
print(body)
reset_body(en_sources)







# The Wall Street Journal => 403
# crawled =WebCrawling('https://www.wsj.com/print-edition/20240103/frontpage')
# crawled_news = crawled.news('.WSJTheme--headline--unZqjb45 reset WSJTheme--heading-3--2z_phq5h typography--serif-display--ZXeuhS5E')
# sep = crawled_news.split('&&&')
# for x in sep:
#     print(x)

# Asahi => Font problem
# crawled =WebCrawling('https://www.asahi.com/shimen/20240103/?iref=pc_gnavi')
# crawled_news = crawled.news('#shimen-digest > ul > li')
# sep = crawled_news.split('&&&')
# for x in sep:
#     print(x)




