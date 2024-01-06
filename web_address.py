from datetime import datetime, timedelta

today = datetime.now()
today_formatted = today.strftime("%Y%m%d")
yesterday = today - timedelta(days=1)
yesterday_formatted = yesterday.strftime("%Y%m%d")


ko_jp_sources = {
    '조선': 'https://media.naver.com/press/023/newspaper',
    '중앙': 'https://media.naver.com/press/025/newspaper',
    '동아': 'https://media.naver.com/press/020/newspaper',
    '한국': 'https://media.naver.com/press/469/newspaper',
    '경향': 'https://media.naver.com/press/032/newspaper',
    '서울': 'https://media.naver.com/press/081/newspaper',
    '국민': 'https://media.naver.com/press/005/newspaper',
    '한경': 'https://media.naver.com/press/015/newspaper',
    '매경': 'https://media.naver.com/press/009/newspaper',
    'asahimorning': f'https://www.asahi.com/shimen/{today_formatted}/?iref=pc_gnavi',
    'asahinight': f'https://www.asahi.com/shimen/{yesterday_formatted}ev/?iref=pc_gnavi'
}

ko_jp_selector = {
    'selector': '._persist_wrap > div:nth-child(1) > div:nth-child(1) .newspaper_brick_item._start_page li',
    'asahimorning': '#shimen-digest > ul > li > a',
    'asahinight': '.List.ListSideImage.ListHeadline li:not(:first-child):not(:last-child)'
}

en_sources = {
    'nyt': 'https://www.nytimes.com/section/todayspaper?redirect_uri=https%3A%2F%2Fwww.nytimes.com%2Finternational%2F',
    'wp': 'https://www.washingtonpost.com/todays_paper/updates/',
    'ft': 'https://www.ft.com/',
    'wsj': f'https://www.wsj.com/print-edition/{yesterday_formatted}/frontpage'
}

en_selector = {
    'nyt': '.css-1u3p7j1',
    'wp': '#Front-Page .wpds-c-eGurKC',
    'ft': '#top-stories + .layout-desktop__grid-container .text.text--color-black.text-display--scale-3.text--weight-500',
    'wsj': '.WSJTheme--list-item--v87pvXUl a'
}

fake_user_agents = [
    'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.83 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
]




