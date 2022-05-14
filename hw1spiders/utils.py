from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
import PySimpleGUI as sg


class computer:  # define a class of computer
    def __init__(self, Rank, System, Cores, Rmax, Rpeak, Power):  # a computer  has these 6 elements
        self.Rank = Rank
        self.System = System
        self.Cores = Cores
        self.Rmax = Rmax
        self.Rpeak = Rpeak
        self.Power = Power


def get_rows():  # get the data from the web
    rows = []
    rows.append(["Rank", "System", "Cores", "Rmax", "Rpeak", "Power"])
    for i in range(1, 6):
        # the newest Top500 computers
        urpage = f'https://top500.org/lists/top500/list/2021/11/?page={i}'
        page = urlopen(urpage)
        soup = bs(page, "html.parser")  # get the soup
        table = soup.find("table")  # find the table
        results = table.find_all('tr')  # find the label 'tr'
        for result in results:
            data = result.find_all("td")  # find the label 'td'
            if len(data) == 0:
                continue
            cpt = computer(data[0].getText(), data[1].getText(), data[2].getText(
            ), data[3].getText(), data[4].getText(), data[5].getText())
            # deal with the text we get to make datas more good-looking
            cpt.System = cpt.System.replace(
                '\n', '').replace(' ', '').replace(',', ', ')
            cpt.Cores = cpt.Cores.replace(',', '')
            cpt.Rmax = cpt.Rmax.replace(',', '')
            cpt.Rpeak = cpt.Rpeak.replace(',', '')
            cpt.Power = cpt.Power.replace(',', '')
            # add the data to the list rows
            rows.append([cpt.Rank, cpt.System, cpt.Cores,
                        cpt.Rmax, cpt.Rpeak, cpt.Power])
            mrows = [cpt.Rank, cpt.System, cpt.Cores,
                     cpt.Rmax, cpt.Rpeak, cpt.Power]
    return rows


def search(sth, rows):  # A searching function
    list = []
    for i in rows:
        for j in i:
            if sth in j:
                list.append(i)  # get all the elements contains the sth
    if len(list) == 0:
        return 'No match.'
    else:
        list.insert(0, ["Rank", "System", "Cores", "Rmax", "Rpeak", "Power"])
        return list


def window_search(rows):
    sg.theme('DarkAmber')   # set the theme

    layout = [[sg.Text('Enter the searching item'), sg.InputText()],  # set the layout of the window
              [sg.Button('Ok'), sg.Button('Cancel')]]

    window = sg.Window('Searching Top500', layout)  # set the window

    while True:
        event, values = window.read()  # get the values and the event
        if event in (None, 'Cancel'):
            break
        else:
            print(values[0])
            print(search(values[0], rows))
        window.close()
