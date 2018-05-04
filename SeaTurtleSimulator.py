from Population import *
from copy import deepcopy
from util import *
import matplotlib.pyplot as plt


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
        self.egg_history = []
        self.time = None

    def updatePop(self, oldPop, temperature):
        self.population.updateTime()

        new_eggs = self.population.updateEggs(oldPop)
        self.egg_history.append(new_eggs)

        self.population.updateFHatched(oldPop, temperature)
        self.population.updateMHatched(oldPop, temperature)

        self.population.updateFInWater(oldPop)
        self.population.updateMInWater(oldPop)

        self.population.updateFJuveniel(oldPop)
        self.population.updateMJuveniel(oldPop)

        self.population.updateFSubAdult(oldPop)
        self.population.updateMSubAdult(oldPop)

        self.population.updateMAdult(oldPop)

        self.population.updateFNotFertile(oldPop)
        self.population.updateFFertile(oldPop)
        self.population.updateFAged(oldPop)
        self.population.updateFFertilized(oldPop)

        self.population.updateFBreeding(oldPop)
        self.population.updateMBreeding(oldPop)

    def simulate(self, t, temperature):
        """:type time timedelta"""

        self.time = t
        for i in range(t.days):
            self.populationHistory.append(deepcopy(self.population))
            self.updatePop(self.populationHistory[-1], temperature)
            self.date += timedelta(1)

            if t.days > (50 * 365) and ((i + 1) % (365 * 10)) == 0:
                print("Simulated %i years!" % ((i + 1) / 365))

        #printList(self.populationHistory)
        print self.population

    def plot(self):
        if len(self.populationHistory) == 0:
            raise AttributeError('Run the simulation first!')

        days = range(self.time.days)

        popLists = getPopLists(self.populationHistory)

        l1 = plt.plot(days, popLists["total"], label="Total Population")
        l2 = plt.plot(days, popLists["females"], label="Female Population")
        l3 = plt.plot(days, popLists["males"], label="Male Population")
        # l4 = plt.plot(days, popLists["eggs"], label="Number of eggs")
        # l5 = plt.plot(days, popLists["fertilized_females"], label="Fertilized females")
        # l6 = plt.plot(days, popLists["breeding_females"], label="Breeding females")
        # l7 = plt.plot(days, self.egg_history, label="new eggs")

        lw = 0.7

        plt.setp(l1, linewidth=lw)
        plt.setp(l2, linewidth=lw)
        plt.setp(l3, linewidth=lw)
        # plt.setp(l4, linewidth=lw)
        # plt.setp(l5, linewidth=lw)
        # plt.setp(l6, linewidth=lw)
        # plt.setp(l7, linewidth=lw)


        plt.xlabel('year')
        plt.ylabel('Number of turtles')

        plt.legend(bbox_to_anchor=(0.5, 1.2), loc=9, ncol=2)
        plt.subplots_adjust(top=.83)

        x_distance = self.time.days / 10

        days.append(days[-1] + 1)

        x_ticks = [day for day in days if (day % x_distance) == 0]
        x_labels = [str(i*x_distance/365 + self.startdate.year) for i in range(len(x_ticks)+1)]

        plt.xticks(x_ticks, x_labels)
        plt.savefig("pop" + str(self.time.days/365) + "y" + str(self.time.days % 365) + "d" + ".png", dpi=900)
        # plt.show()

