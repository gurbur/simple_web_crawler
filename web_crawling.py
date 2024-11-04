import requests
from bs4 import BeautifulSoup
import pandas as pd

df = pd.read_csv("movies.csv")

specific_column = df['title']

print(specific_column)

for i in range(1, 10):
    movie_name = specific_column[i]

    url = "https://www.imdb.com/find/?q={}&ref_=nv_sr_sm".format(movie_name)
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        html = response.text
    else:
        print("Error! failed to bring page");

    print("Brought successful:")

    soup = BeautifulSoup(html, "html.parser")
    # 가져온 html에서 첫 번째 제목부분 찾아서 가져오기
    info = soup.find("ul", class_="ipc-metadata-list-summary-item__stl").get_text()

    print(info)
    
