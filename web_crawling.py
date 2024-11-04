import requests
from bs4 import BeautifulSoup
import pandas as pd

df = pd.read_csv("movies.csv")

data = {'movieId': [], 'director': []}

specific_column = df['title']

for i in range(1, 10):
    print(i, "ongoing...")
    movie_name = specific_column[i]

    url = "https://www.imdb.com/find/?q={}&ref_=nv_sr_sm".format(movie_name)
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        html = response.text
    else:
        print("Error! failed to bring page");

    soup = BeautifulSoup(html, "html.parser")
    # 가져온 html에서 첫 번째 감독, 배우 부분 찾아서 가져오기
    info = soup.find("ul", class_="ipc-metadata-list-summary-item__stl").get_text()

    info = info.split(",")[0]

    data['movieId'].append(i)
    data['director'].append(info)

output_df = pd.DataFrame(data)

output_df.to_csv('output.csv', index=False)
