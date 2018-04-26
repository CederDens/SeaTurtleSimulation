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

    def updatePop(self, oldPop):
        self.population.updateTime()

        self.population.updateEggs(oldPop)

        self.population.updateFHatched(oldPop)
        self.population.updateMHatched(oldPop)

        self.population.updateFInWater(oldPop)
        self.population.updateMInWater(oldPop)

        self.population.updateFInRif(oldPop)
        self.population.updateMInRif(oldPop)

        self.population.updateFJuveniel(oldPop)
        self.population.updateMJuveniel(oldPop)

    def simulate(self, days):
        for _ in range(days):
            self.populationHistory.append(deepcopy(self.population))
            self.updatePop(self.populationHistory[-1])
            self.date += timedelta(1)
        printList(self.populationHistory)
