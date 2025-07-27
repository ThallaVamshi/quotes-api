import requests
from bs4 import BeautifulSoup

def get_quotes():
    url = "https://quotes.toscrape.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    quotes_data = []
    for quote in soup.select(".quote"):
        text = quote.find("span", class_="text").get_text()
        author = quote.find("small", class_="author").get_text()
        tags = [tag.get_text() for tag in quote.select(".tags .tag")]
        quotes_data.append({
            "quote": text,
            "author": author,
            "tags": tags
        })

    return quotes_data
