#Partial code

from bs4 import BeautifulSoup
import requests
import pandas as pd

#Scrapping all teams an his historical data in american cup since 1916 to 2021 to export in a two df historical and fixture.

years = ['1916','1917','1919','1920','1921','1922','1923','1924','1925','1926','1927','1929','1935','1937','1939','1941','1942','1945','1946','1947','1949','1953','1955','1956','1957','1963','1967','1975','1979','1983','1987','1989','1991','1993','1995','1997','1999','2001','2004','2007','2011','2015','2016','2019','2021','2021']

def get_matches(year):
    web = f'https://es.wikipedia.org/wiki/Copa_Am%C3%A9rica_{year}'
    response = requests.get(web)
    content = response.text
    soup = BeautifulSoup(content, 'lxml')
    matches = soup.find_all('table', class_='collapsible autocollapse vevent plainlist',width=True)

    home = []
    score = []
    away = []
