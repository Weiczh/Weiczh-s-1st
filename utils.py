from bs4 import BeautifulSoup as bs
#import urllib
#import urllib.request
from urllib.request import urlopen
#import csv


def get_rows():  # get the data from the web
    rows = []
    rows.append(["Rank", "System", "Cores", "Rmax", "Rpeak", "Power"])
    for i in range(1, 6):
        urpage = f'https://top500.org/lists/top500/list/2021/11/?page={i}'
        page = urlopen(urpage)
        soup = bs(page, "html.parser")
        table = soup.find("table")
        results = table.find_all('tr')
        for result in results:
            data = result.find_all("td")
            if len(data) == 0:
                continue
            rank = data[0].getText()
            system = data[1].getText()
            Cores = data[2].getText()
            Rmax = data[3].getText()
            Rpeak = data[4].getText()
            Power = data[5].getText()
            # 处理数据与符号
            system = system.replace('\n', '').replace(
                ' ', '').replace(',', ', ')
            Cores = Cores.replace(',', '')
            Rmax = Rmax.replace(',', '')
            Rpeak = Rpeak.replace(',', '')
            Power = Power.replace(',', '')
            rows.append([rank, system, Cores, Rmax, Rpeak, Power])
            mrows = [rank, system, Cores, Rmax, Rpeak, Power]
    return rows


def search(sth, rows):  # A searching function
    list = []
    for i in rows:
        for j in i:
            if sth in j:
                list.append(i)
    if len(list) == 0:
        return 'No match.'
    else:
        list.insert(0, ["Rank", "System", "Cores", "Rmax", "Rpeak", "Power"])
        return list
