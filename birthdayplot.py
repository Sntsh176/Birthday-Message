import json
import datetime
import calendar
from collections import Counter
from bokeh.plotting import figure, show, output_file

def createjson(_birthdays):
    with open("birthdaydict.json", "w") as f:
        json.dump(_birthdays, f)
        f.close()
def readjson():
    with open("birthdaydict.json", "r") as f:
        info = json.load(f)
        f.close()
    return info
def printcurrentbirthdays():
    print("\nWelcome to the birthday dictionary. We know the birthdays of: ")
    for x in readjson():
        print(x)
def getbirthday(_info):
    while True:
        printcurrentbirthdays()
        who = input("Who's birthday do you want to look up? x to exit: ")
        if who == "x": break
        if who in _info:
            print(who + "'s birthday is " + _info[who])
        else:
            if input("Add " + who + " to json file? y or n: ") == "y":
                bday = input("Enter birthday for " + who + ": ")
                _info[who] = bday
                createjson(_info)
def birthdaymonths():
    bdays = []
    info = readjson()
    for x in info.values():
        bdays.append(datetime.datetime.strptime(x, "%m/%d/%Y").strftime("%B"))
    return Counter(bdays)
def main():
    getbirthday(readjson())
    print("---- Monthly Counts ----")
    bCounter = birthdaymonths()
    print(str(bCounter.elements).split("(")[1].split(")")[0])
    x_categories = []
    output_file("plot.html")
    for m_name in calendar.month_name:
        x_categories.append(m_name)
    x = list(bCounter.keys())
    y = list(bCounter.values())
    p = figure(x_range=x_categories)
    p.vbar(x=x, top=y, width=1)
    show(p)
if __name__ == "__main__":
    main()