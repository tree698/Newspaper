import requests, random
from bs4 import BeautifulSoup
from requests import HTTPError
from web_address import fake_user_agents


class WebCrawling:

    def __init__(self, url):
        self.url = url

    def news(self, css_selector):
        response = requests.get(self.url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        titles = soup.select(css_selector)
        title_list = [title.getText().strip() for title in titles]
        result = '&&&'.join(title_list)
        return result if result else 'NaN'

    """ 
    Ref) Stack Overflow
    https://stackoverflow.com/questions/57983718/could-not-scrape-a-japanese-website-using-beautifulsoup
    """
    def jp_news(self, css_selector):
        headers = {
            'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7',
            'User-Agent': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7,de;q=0.6',
        }

        try:
            contents = requests.get(self.url, headers=headers)
            contents.raise_for_status()
        except HTTPError:
            title_list = []
        else:
            soup = BeautifulSoup(contents.content, 'html.parser')
            titles = soup.select(css_selector)
            title_list = set([title.getText().strip().replace(u"\u3000", " ") for title in titles])
        result = '&&&'.join(title_list)
        return result if result else 'NaN'

    def wsj_news(self, css_selector):
        response = requests.get(self.url, headers={'User-Agent': random.choice(fake_user_agents)})
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        titles = soup.select(css_selector)
        title_list = [title.getText().strip() for title in titles]
        result = '&&&'.join(title_list)
        return result if result else 'NaN'

    def nyt_news(self, css_selector):
        response = requests.get(self.url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        title_main = soup.select(css_selector[0])
        title_main_list = [title.getText().strip() for title in title_main]

        length = length_a1(soup, css_selector[1])
        title_additional = soup.select(f'.css-12y5jls li:nth-child(-n+{length}) h2')
        title_additional_list = [title.getText().strip() for title in title_additional]

        title_list = title_main_list + title_additional_list
        result = '&&&'.join(title_list)
        return result if result else 'NaN'

def length_a1(soup, selector):
    a1 = soup.select(selector)
    a1_list = [title for title in a1 if title.getText().strip() == 'Page A1']
    return len(a1_list)
