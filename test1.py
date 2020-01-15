
import bs4 as bs
import urllib.request
import re


sauce = urllib.request.Request('http://www.eurofootball.bg/bookmakers.php?v=bookmakers&repr=16&hid=1', headers={'User-Agent': 'Mozilla/5.0'})
data=urllib.request.urlopen(sauce).read()
# data = infile.decode('ISO-8859-1') # Read the content as string decoded with ISO-8859-1

# print(data)
soup = bs.BeautifulSoup(data, 'lxml')



# pattern = r"(title=\")(?P<country>\w+)[:][ ](?P<league>[\w ]*)\b"

print(soup)
# print(data.get_text())


a = soup.find('tr', {'class': 'off-a'})

for i in soup.find_all('tr', {'class': 'off-a'}):


# pattern = r"(title=\")(?P<country>\w+)[:][ ](?P<league>[\w ]*)\b"
#     i = a
    # print(i)
    print(i.get_text())
    print(i.find_all('a')[1]['href'])

#
# print(i.find('a', {'id': 'leaguetitle'}).get_text().split(": "))
# for i in i.find_all('table', {'id': 'blocks'}):
#
#     hour_minute = i.find('td', {"class": "kick"}).get_text()
#     status = i.find('td', {"class": "status"}).get_text()
#     home = i.find('td', {"class": "home"}).find('a').get_text()
#     away = i.find('td', {"class": "away"}).find('a').get_text()
#     score = i.find('td', {"class": "score"}).text
#     halftime = i.find('td', {"class": "halftime"}).text
#
#     print(hour_minute, end=" ")
#     print(status, end=" ")
#     print(home, end=" ")
#     print(away, end=" ")
#     print(score, end=" ")
#     print(halftime)
#
# # for i in a:
#     # print(i.get_text())
#     # m = i.get_text()
#     # m = m.split("\n")
#     # print(type(m))
#     # print(m)
#
#     # print("-------------------------------------------")
#     # print(i.contents[1])
#     # print("-------------------------------------------")