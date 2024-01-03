import os, dotenv, requests
from datetime import datetime, timedelta
from crawling import WebCrawling
from web_address import ko_sources

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


# TODO 2. Other Newspapers
names = ['nyt', 'wp', 'ft']

# The New York Times (nyt)
crawled =WebCrawling('https://www.nytimes.com/section/todayspaper?redirect_uri=https%3A%2F%2Fwww.nytimes.com%2Finternational%2F')
crawled_nyt = crawled.news('.css-1u3p7j1')
body['news'][names[0]] = crawled_nyt

# The Washington Post (wp)
crawled =WebCrawling('https://www.washingtonpost.com/todays_paper/updates/')
crawled_wp = crawled.news('#Front-Page .wpds-c-eGurKC')
body['news'][names[1]] = crawled_wp

# The Finanical Times (ft)
crawled =WebCrawling('https://www.ft.com/')
crawled_ft = crawled.news('#top-stories + .layout-desktop__grid-container .text.text--color-black.text-display--scale-3.text--weight-500')
body['news'][names[2]] = crawled_ft

# sheety
body['news']['date'] = yesterday_formatted
body['news']['week'] = week_yesterday
sheety_response = requests.post(sheety_endpoint_en, json=body, headers=bearer_header)
sheety_response.raise_for_status()

print(body)
for name in names:
    del body['news'][name]



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




