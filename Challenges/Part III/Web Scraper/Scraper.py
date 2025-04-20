import urllib.request
from bs4 import BeautifulSoup

class Scraper:
    def __init__(self, site):
        self.site = site

    def scrape(self):
        response = urllib.request.urlopen(self.site)
        html = response.read()
        parser = 'html.parser'
        soup = BeautifulSoup(html, parser)
        with open("output.txt", "w") as f:
            for tag in soup.find_all('a'):
                url = tag.get('href')
                if url is None:
                    continue
                # Removed: and "html" from this if. Not sure why it doesn't work out. 
                if url in url:
                    print("\n" + url)
                    f.write(url + "\n")

news = "https://news.google.com/"
Scraper(news).scrape()
