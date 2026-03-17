import requests
from bs4 import BeautifulSoup

def scrape_news():
    url = "https://news.ycombinator.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    headlines = []
    for item in soup.select(".titleline a"):
        headlines.append(item.text)

    return headlines

if __name__ == "__main__":
    news = scrape_news()
    for n in news:
        print(n)