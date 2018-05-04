from datetime import date
from Population import *

class Time:
    def __init__(self, years=0, days=0):
        """

        :type years: int
        :type days: int
        """
        self._years = years
        self._days = days

    def get_in_days(self):
        return self._years*365 + self._days

    def get_years_and_days(self):
        days = self.get_in_days()
        years = days//365
        remaining_days = days - 365*years
        return years, remaining_days


class Color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


def readHistoricalPopulation(fileName):
    years = []
    popSize = []
    histFile = open(fileName, 'r')
    for line in histFile:
        years.append(int(line.split()[0]))
        popSize.append(int(float(line.split()[1].replace(',', '.'))*1000000))
    return years, popSize


def printList(lst):
    for l in lst:
        print l


def isMBreedingDate(d):
    """:type d date"""

    if 3 <= d.month <= 9:
        return False
    return True


def isFBreedingDate(d):
    """:type d date"""

    if 2 <= d.month <= 9:
        return False
    return True


def getMBreedingDay(d):
    """:type d date"""

    if d.month >= 10:   # october, november or december
        return (d - date(d.year, 10, 1)).days
    elif d.month <= 2:  # january or february
        return (d - date(d.year - 1, 10, 1)).days
    else:
        raise RuntimeError("Getting breeding days of date out of male breeding season!")


def getFBreedingDay(d):
    """:type d date"""

    if d.month >= 10:   # october, november or december
        return (d - date(d.year, 10, 1)).days
    elif d.month == 1:  # january
        return (d - date(d.year - 1, 10, 1)).days
    else:
        raise RuntimeError("Getting breeding days of date out of female breeding season!")


def toDays(years=0, days=0):
    return years*365 + days


def getPopLists(histPop):
    """:type p Population"""

    females = []
    males = []
    total = []
    eggs = []
    fertile_females = []
    breeding_females = []
    for p in histPop:
        females.append(p.getFemalePopulation())
        males.append(p.getMalePopulation())
        total.append(p.getTotalPopulation())
        eggs.append(p.eggs)
        fertile_females.append(p.f_fertilized*6)
        breeding_females.append(p.f_breeding)

    return {"females": females, "males": males, "total": total, "eggs": eggs, "fertilized_females": fertile_females, "breeding_females": breeding_females}


def readTemps():
    f = open("temperatures.txt", "r")
    temps = {}
    year = 1960
    for line in f:
        temps[year] = float(line)
        year += 1
    return temps