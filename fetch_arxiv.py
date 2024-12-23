import requests
from bs4 import BeautifulSoup

def fetch_arxiv_articles():
    url = 'https://arxiv.org/list/cs/new'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    articles = []
    for item in soup.find_all('li', class_='arxiv-result'):
        title = item.find('h5', class_='title').text.strip()
        abstract = item.find('p', class_='abstract').text.strip()
        articles.append({'title': title, 'abstract': abstract})

    return articles

if __name__ == "__main__":
    articles = fetch_arxiv_articles()
    for article in articles:
        print(article['title'])
        print(article['abstract'])