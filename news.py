import requests
from bs4 import BeautifulSoup


def get_news_from_rbc(limit=3):
    url = "https://www.rbc.ru/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    headlines = []

    for item in soup.find_all('a', class_='main__feed__link js-yandex-counter js-visited')[:limit]:
        headlines.append({'title': item.get_text(), 'link': item['href']})

    if response.status_code != 200:
        print(f"Ошибка при получении {url}: {response.status_code}")

    return headlines
