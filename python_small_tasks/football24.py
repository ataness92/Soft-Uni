import requests
from bs4 import BeautifulSoup
import pandas as pd

standings_url = "https://www.futbol24.com/teamCompare/England/Leicester-City/vs/England/Leeds-United/"
data = requests.get(standings_url)
soup = BeautifulSoup(data.text, "html.parser")

print(soup)
