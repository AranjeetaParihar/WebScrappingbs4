from bs4 import BeautifulSoup
import requests

URL = "https://en.wikipedia.org/wiki/Japanese_horror"
response = requests.get(URL)
print(response.status_code)
if response.status_code != 200:
    print('Failed to load the page.')
else:
    data = response.text
    soup = BeautifulSoup(data, 'html.parser')
    division = soup.find_all("div", class_="div-col")
    item_list = [movie.getText() for movie in division]
    movies_list = item_list[0].split('\n')
    with open('movies.txt', 'a', encoding="utf8") as file:
        for movie in movies_list:
            if movie != '':
                file.write(f'{movie}\n')
