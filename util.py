from datetime import date
from Population import *
import matplotlib.pyplot as plt


class Time:
    def __init__(self, years=0, days=0):
        """

        :type years: int
        :type days: int
        """
        self._years = years
        self._days = days

    def get_in_days(self):
        return self._years * 365 + self._days

    def get_years_and_days(self):
        days = self.get_in_days()
        years = days // 365
        remaining_days = days - 365 * years
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
        popSize.append(int(float(line.split()[1].replace(',', '.')) * 1000000))
    return years, popSize


def printList(lst):
    for l in lst:
        print l


def isMDepartingDate(d):
    """:type d date"""

    if 1 <= d.month <= 9:
        return False
    return True


def isFDepartingDate(d):
    """:type d date"""

    if 1 <= d.month <= 9:
        return False
    return True


def isMLeavingDate(d):
    """:type d date"""

    if 1 <= d.month <= 3:
        return True
    return False


def isFLeavingDate(d):
    """:type d date"""

    if 4 <= d.month <= 9:
        return True
    return False


def getMBreedingDay(d):
    """:type d date"""

    if d.month >= 10:  # october, november or december
        return (d - date(d.year, 10, 1)).days
    elif d.month <= 2:  # january or february
        return (d - date(d.year - 1, 10, 1)).days
    else:
        raise RuntimeError("Getting breeding days of date out of male breeding season!")


def getFBreedingDay(d):
    """:type d date"""

    if d.month >= 10:  # october, november or december
        return (d - date(d.year, 10, 1)).days
    else:
        raise RuntimeError("Getting breeding days of date out of female breeding season!")


def toDays(years=0, days=0):
    return years * 365 + days


def getPopLists(histPop):
    """

    :type histPop: list[Population]
    """
    retDic = {}
    for k in ["females", "males", "total", "eggs", "m_hatched", "m_in_water", "m_juveniel", "m_subadult", "m_adult",
              "m_breeding", "f_hatched", "f_in_water", "f_juveniel", "f_subadult", "f_not_fertile", "f_fertile",
              "f_breeding", "f_fertilized", "f_aged"]:
        retDic[k] = []
    for p in histPop:
        retDic["females"].append(p.getFemalePopulation())
        retDic["males"].append(p.getMalePopulation())
        retDic["total"].append(p.getTotalPopulation())
        retDic["eggs"].append(p.eggs)
        retDic["m_hatched"].append(p.m_hatched)
        retDic["m_in_water"].append(p.m_in_water)
        retDic["m_juveniel"].append(p.m_juveniel)
        retDic["m_subadult"].append(p.m_subadult)
        retDic["m_adult"].append(p.m_adult)
        retDic["m_breeding"].append(p.m_breeding)
        retDic["f_hatched"].append(p.f_hatched)
        retDic["f_in_water"].append(p.f_in_water)
        retDic["f_juveniel"].append(p.f_juveniel)
        retDic["f_subadult"].append(p.f_subadult)
        retDic["f_not_fertile"].append(p.f_not_fertile)
        retDic["f_fertile"].append(p.f_fertile)
        retDic["f_breeding"].append(p.f_breeding)
        retDic["f_fertilized"].append(p.f_fertilized)
        retDic["f_aged"].append(p.f_aged)
    return retDic


def readTemps():
    f = open("temperatures.txt", "r")
    temps = {}
    year = 1960
    for line in f:
        temps[year] = float(line)
        year += 1
    return temps


def getTestRange(start, step):
    ret = []
    for i in range(11):
        ret.append(start + i * step)
    return ret


def readStablePops():
    f = open("stablePops.txt", "r")
    pops = []
    lams = []
    eggs = []
    for line in f:
        if not line.startswith("//") and not line.startswith("populationsize"):
            spl = line.split(', ')
            pops.append(int(spl[0]))
            lams.append(float(spl[1]))
            eggs.append(int(spl[2][:-1]))

    l1 = plt.plot(pops, eggs)

    plt.xlabel('Population')
    plt.ylabel('Lambda')
    plt.savefig("stablePops.png")
