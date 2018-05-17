from Population import *
from copy import deepcopy
from util import *
import matplotlib.pyplot as plt
from random import *

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
        self.tsunamiyears = []

    def getTsunamiYears(self):
        seed(3)
        for i in range(self.time.days/365):
            if random() < 0.1:
                self.tsunamiyears.append(i + self.startdate.year)

    def tsunamiIsComing(self):
        if self.date.month >= 10 and self.date.year in self.tsunamiyears:
            return True
        elif self.date.month < 10 and self.date.year-1 in self.tsunamiyears:
            return True
        return False

    def temperature(self, scenario, year=0):
        if year == 0:
            year = self.date.year
        if year <= 2000:
            return 29.348

        elif year <= 2055:
            if scenario == 1:
                return 0.018181818 * year - 7.015636364
            elif scenario == 2:
                return 0.025454545 * year - 21.561090909
            elif scenario == 3:
                return 0.023636364 * year - 17.924727273
            elif scenario == 4:
                return 0.036363636 * year - 43.379272727
            elif scenario == 5:
                return 29.348
            else:
                raise Exception(msg="Wrong scenario!")
        elif year <= 2090:
            if scenario == 1:
                return 30.348
            elif scenario == 2:
                return 0.011428571 * year + 7.262285714
            elif scenario == 3:
                return 0.025714286 * year - 22.194857143
            elif scenario == 4:
                return 0.048571429 * year - 68.466285714
            elif scenario == 5:
                return 29.348
            else:
                raise Exception(msg="Wrong scenario!")
        else:
            if scenario == 1:
                return 30.348
            elif scenario == 2:
                return 31.148
            elif scenario == 3:
                return 31.548
            elif scenario == 4:
                return 33.048
            elif scenario == 5:
                return 29.348
            else:
                raise Exception(msg="Wrong scenario!")

    def updatePop(self, oldPop, temperature):
        self.population.updateTime()

        new_eggs = self.population.updateEggs(oldPop)
        self.egg_history.append(new_eggs)

        self.population.updateFHatched(oldPop, temperature, self.tsunamiIsComing())
        self.population.updateMHatched(oldPop, temperature, self.tsunamiIsComing())

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

    def simulate(self, t, scenario):
        """:type t timedelta"""

        self.time = t
        self.getTsunamiYears()
        for i in range(t.days):
            self.populationHistory.append(deepcopy(self.population))
            self.updatePop(self.populationHistory[-1], self.temperature(scenario))
            self.date += timedelta(1)

            if t.days > (50 * 365) and ((i + 1) % (365 * 10)) == 0:
                print("Simulated %i years!" % ((i + 1) / 365))

        # printList(self.populationHistory)
        print self.population

    def plot(self, scenario, new_eggs=False):
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

            filename = "pop" + str(int(self.populationHistory[0].getTotalPopulation())) + "/pop_scenario"+ str(scenario) + "_" + str(
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

        #plt.setp(plt.plot(days, popLists["m_adult"][(50*365)+12:(51*365)+17], label="Adult males (not breeding)"), linewidth=lw)
        plt.setp(plt.plot(days, popLists["m_breeding"][(50*365)+12:(51*365)+17], label="Breeding males"), linewidth=lw)
        #plt.setp(plt.plot(days, popLists["f_fertile"][(50*365)+12:(51*365)+17], label="Fertile females"), linewidth=lw)
        plt.setp(plt.plot(days, popLists["f_breeding"][(50*365)+12:(51*365)+17], label="Breeding females"), linewidth=lw)
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
        x_labels = ["apr", "mei", "jun", "jul", "aug", "sep", "okt", "nov", "dec", "jan", "feb", "mar", "apr"]

        plt.xticks(x_ticks, x_labels)

        plt.savefig(filename, dpi=900)
        plt.close()

    def plotTemperature(self):

        years = range(1900, 2150)
        temps1 = [self.temperature(1, y) for y in years]
        temps2 = [self.temperature(2, y) for y in years]
        temps3 = [self.temperature(3, y) for y in years]
        temps4 = [self.temperature(4, y) for y in years]

        print(temps1)

        plt.plot(years, temps1, label="Scenario 1")
        plt.plot(years, temps2, label="Scenario 2")
        plt.plot(years, temps3, label="Scenario 3")
        plt.plot(years, temps4, label="Scenario 4")

        plt.xlabel('Year')
        plt.ylabel('Temperature')

        plt.legend(bbox_to_anchor=(0.5, 1.2), loc=9, ncol=2)
        plt.subplots_adjust(top=.83)

        plt.show()