from Population import *
from copy import deepcopy
from util import *
import matplotlib.pyplot as plt


class SeaTurtleSimulator:
    def __init__(self, startdate, startpopulation, lam):
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
        self.lam = lam

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
        self.population.updateFFertilized(oldPop, self.lam)

        self.population.updateFBreeding(oldPop, self.lam)
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

        # printList(self.populationHistory)
        print self.population

    def plot(self, new_eggs=False):
        if len(self.populationHistory) == 0:
            raise AttributeError('Run the simulation first!')

        days = range(self.time.days)
        popLists = getPopLists(self.populationHistory)
        lw = 0.7

        if not new_eggs:
            l1 = plt.plot(days, popLists["total"], label="Total Population")
            l2 = plt.plot(days, popLists["females"], label="Female Population")
            l3 = plt.plot(days, popLists["males"], label="Male Population")

            plt.setp(l1, linewidth=lw)
            plt.setp(l2, linewidth=lw)
            plt.setp(l3, linewidth=lw)

            filename = "pop" + str(int(self.populationHistory[0].getTotalPopulation())) + "/pop" + str(
                self.time.days / 365) + "y" + str(
                self.time.days % 365) + "d" + str(self.lam) + ".png"

        else:
            print max(self.egg_history[-365:])
            l7 = plt.plot(days, self.egg_history, label="new eggs")
            plt.setp(l7, linewidth=lw)
            filename = "pop" + str(int(self.populationHistory[0].getTotalPopulation())) + "/newEggs" + str(
                self.time.days / 365) + "y" + str(
                self.time.days % 365) + "d" + str(self.lam) + ".png"

        plt.xlabel('year')
        plt.ylabel('Number of turtles')

        plt.legend(bbox_to_anchor=(0.5, 1.2), loc=9, ncol=2)
        plt.subplots_adjust(top=.83)

        x_distance = self.time.days / 10

        days.append(days[-1] + 1)

        x_ticks = [day for day in days if (day % x_distance) == 0]
        x_labels = [str(i * x_distance / 365 + self.startdate.year) for i in range(len(x_ticks) + 1)]

        plt.xticks(x_ticks, x_labels)

        plt.savefig(filename, dpi=900)
        # plt.show()
        plt.close()

    def plotCompartments(self):
        if len(self.populationHistory) < 60:
            raise AttributeError('Run the simulation for at least 60 years first!')

        days = range(370)
        popLists = getPopLists(self.populationHistory)
        lw = 1

        # plt.setp(plt.plot(days, popLists["m_adult"][(50*365)+12:(51*365)+17], label="Adult males (not breeding)"), linewidth=lw)
        # plt.setp(plt.plot(days, popLists["m_breeding"][(50*365)+12:(51*365)+17], label="Breeding males"), linewidth=lw)
        # plt.setp(plt.plot(days, popLists["f_fertile"][(50*365)+12:(51*365)+17], label="Fertile females"), linewidth=lw)
        # plt.setp(plt.plot(days, popLists["f_breeding"][(50*365)+12:(51*365)+17], label="Breeding females"), linewidth=lw)
        plt.setp(plt.plot(days, popLists["f_fertilized"][(50*365)+12:(51*365)+17], label="Fertilized females"), linewidth=lw)

        filename = "pop" + str(int(self.populationHistory[0].getTotalPopulation())) + "/categorical" + str(self.lam) + ".png"

        plt.xlabel('year')
        plt.ylabel('Number of turtles')

        plt.legend(bbox_to_anchor=(0.5, 1.2), loc=9, ncol=2)
        plt.subplots_adjust(top=.83)

        day_lengths = [0, 30, 31, 30, 31, 31, 30, 31, 30, 31, 31, 28, 31]
        x_ticks = [0]
        for x in day_lengths[1:]:
            x_ticks.append(x_ticks[-1] + x)
        print x_ticks
        x_labels = ["apr", "mei", "jun", "jul", "aug", "sep", "okt", "nov", "dec", "jan", "feb", "mar", "apr"]

        plt.xticks(x_ticks, x_labels)

        plt.savefig(filename, dpi=900)
        plt.close()