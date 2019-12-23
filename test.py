import bs4 as bs
import urllib.request
import re

sauce = urllib.request.urlopen('https://www.scorespro.com/soccer/date/20-12-2019/').read()

soup = bs.BeautifulSoup(sauce, 'lxml')

a = soup.find('div', {'id': 'mainfeed'}).find_all('div', {'class': 'compgrp'})

pattern = r"(title=\")(?P<country>\w+)[:][ ](?P<league>[\w ]*)\b"
i = a[-1]
print(i.get_text())
a = i.contents[0]
print(a.find('a', {'id': 'leaguetitle'}).get_text().split(": "))

# for i in a:
    # print(i.get_text())
    # m = i.get_text()
    # m = m.split("\n")
    # print(type(m))
    # print(m)

    # print("-------------------------------------------")
    # print(i.contents[1])
    # print("-------------------------------------------")
