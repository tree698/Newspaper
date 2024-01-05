import requests, random
from bs4 import BeautifulSoup
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
        return '&&&'.join(title_list)

    """ 
    Ref) Stack Overflow
    https://stackoverflow.com/questions/57983718/could-not-scrape-a-japanese-website-using-beautifulsoup
    """
    def jp_news(self, css_selector):
        response = requests.session()
        headers = {
            'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
        }
        response.headers.update(headers)

        contents = response.get(self.url)
        contents.raise_for_status()
        soup = BeautifulSoup(contents.content, 'html.parser')
        titles = soup.select(css_selector)
        title_list = [title.getText().strip().replace(u"\u3000", " ") for title in titles]
        return '&&&'.join(title_list)

    def wsj_news(self, css_selector):
        response = requests.get(self.url, headers={'User-Agent': random.choice(fake_user_agents)})
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        titles = soup.select(css_selector)
        title_list = [title.getText().strip() for title in titles]
        return '&&&'.join(title_list)