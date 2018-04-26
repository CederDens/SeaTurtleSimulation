from Population import *
from copy import deepcopy
from util import *


class SeaTurtleSimulator:
    def __init__(self, startdate, startpopulation):
        """
        :type startdate date
        :type startpopulation Population

        """

        self.startdate = startdate
        self.date = self.startdate
        self.population = startpopulation
        self.populationHistory = []

    def updatePop(self):
        self.population.updateTime()
        self.population.updateEggs(3)

    def simulate(self, days):
        for _ in range(days):
            self.populationHistory.append(deepcopy(self.population))
            self.updatePop()
            self.date += timedelta(1)
        printList(self.populationHistory)
