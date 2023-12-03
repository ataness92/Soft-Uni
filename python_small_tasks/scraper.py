import requests
from bs4 import BeautifulSoup
import pandas as pd

standings_url = "https://fbref.com/en/comps/9/Premier-League-Stats"
data = requests.get(standings_url)
soup = BeautifulSoup(data.text, "html.parser")

standings_table =soup.select('table.stats_table')[0]
links = standings_table.find_all('a')
links = [l.get("href") for l in links]
links = [l for l in links if '/squads/' in l]

team_urls = [f"https://fbref.com{l}" for l in links]
data = requests.get(team_urls[0])
matches = pd.read_html(data.text, match="Scores & Fixtures")[0]


soup = BeautifulSoup(data.text, features= 'lxml')
links = soup.find_all('a')
links = [l.get("href") for l in links]
links = [l for l in links if l and 'all_comps/shooting/' in l]
data = requests.get(f"https://fbref.com{links[0]}")
shooting = pd.read_html(data.text, match="Shooting")[0]
print(shooting)







