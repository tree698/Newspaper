import requests
from bs4 import BeautifulSoup


def get_contents(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.text


class WebCrawling:

    def __init__(self, url):
        self.url = url

    def news(self, css_selector):
        contents = get_contents(self.url)
        soup = BeautifulSoup(contents, 'html.parser')
        titles = soup.select(css_selector)
        title_list = [title.getText().strip() for title in titles]
        return '&&&'.join(title_list)

