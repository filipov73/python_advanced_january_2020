import bs4 as bs
import urllib.request
import re

sauce = urllib.request.urlopen('https://www.scorespro.com/soccer/date/14-12-2019/').read()

soup = bs.BeautifulSoup(sauce, 'lxml')

a = soup.find('div', {'id': 'mainfeed'}).find_all('div', {'class': 'compgrp'})

pattern = r"(title=\")(?P<country>\w+)[:][ ](?P<league>[\w ]*)\b"
i = a[-1]
print(i)
print(i.get_text())

print(i.find('a', {'id': 'leaguetitle'}).get_text().split(": "))
for i in i.find_all('table', {'id': 'blocks'}):

    hour_minute = i.find('td', {"class": "kick"}).get_text()
    status = i.find('td', {"class": "status"}).get_text()
    home = i.find('td', {"class": "home"}).find('a').get_text()
    away = i.find('td', {"class": "away"}).find('a').get_text()
    score = i.find('td', {"class": "score"}).text
    halftime = i.find('td', {"class": "halftime"}).text

    print(hour_minute, end=" ")
    print(status, end=" ")
    print(home, end=" ")
    print(away, end=" ")
    print(score, end=" ")
    print(halftime)

# for i in a:
    # print(i.get_text())
    # m = i.get_text()
    # m = m.split("\n")
    # print(type(m))
    # print(m)

    # print("-------------------------------------------")
    # print(i.contents[1])
    # print("-------------------------------------------")

