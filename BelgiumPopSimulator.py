import matplotlib.pyplot as plt

from util import *


def birthrate():
    births_per_person_per_year = 0.01086 + 0.00425 + 0.003  # births + migration + unknown marge
    return births_per_person_per_year


def deathrate():
    deaths_per_person_per_year = 0.00986
    return deaths_per_person_per_year


class BelgiumPopSimulator:

    def __init__(self, init_child_count, init_adult_count, init_aged_count):
        self._ChildCount = init_child_count
        self._AdultCount = init_adult_count
        self._AgedCount = init_aged_count
        self._DeathCount = 0

        self.children = []
        self.adults = []
        self.aged = []
        self.death = []
        self.totalPop = []
        self.time = None

    def getPopulationCount(self):
        return self._ChildCount + self._AdultCount + self._AgedCount

    def getChildCount(self):
        return self._ChildCount

    def getAdultCount(self):
        return self._AdultCount

    def getAgedCount(self):
        return self._AgedCount

    def getDeathCount(self):
        return self._DeathCount

    def child2adult(self):
        return self._ChildCount / float(21*365)

    def adult2aged(self):
        return self._AdultCount / float(20*365)

    def aged2death(self):
        return deathrate()*self.getPopulationCount()/365.0

    def births(self):
        return birthrate()*self.getPopulationCount()/365.0

    def showPlot(self, time, labels=None):
        if labels is None:
            labels = ["children", "adults", "aged", "total"]

        for label in labels:
            if label == "children":
                plt.plot(range(time.get_in_days()), self.children, label="Children")
            elif label == "adults":
                plt.plot(range(time.get_in_days()), self.adults, label="Adults")
            elif label == "aged":
                plt.plot(range(time.get_in_days()), self.aged, label="Aged")
            elif label == "death":
                plt.plot(range(time.get_in_days()), self.death, label="Death")
            elif label == "total":
                plt.plot(range(time.get_in_days()), self.totalPop, label="Total Population")

        plt.xlabel('time in days')
        plt.ylabel('Number of people')

        plt.legend(bbox_to_anchor=(0.5, 1.2), loc=9, ncol=2)
        plt.subplots_adjust(top=.83)
        years, days = time.get_years_and_days()
        plt.savefig("pop"+str(years)+"y"+str(days)+"d"+".png")
        plt.show()

    def simulate(self, time):
        """

        :type time: Time
        """
        self.time = time
        for t in range(time.get_in_days()):
            self._ChildCount += (self.births() - self.child2adult())
            self._AdultCount += (self.child2adult() - self.adult2aged())
            self._AgedCount += (self.adult2aged() - self.aged2death())
            self._DeathCount += self.aged2death()

            self.children.append(self._ChildCount)
            self.adults.append(self._AdultCount)
            self.aged.append(self._AgedCount)
            self.death.append(self._DeathCount)
            self.totalPop.append(self.getPopulationCount())

            if (t % 365) == 0 or t == time.get_in_days()-1:
                years, days = Time(days=t).get_years_and_days()
                print "Simulation after %i years and %i days:\n%s" % (years, days, self)

    def plot(self):
        if self.time is not None:
            self.showPlot(self.time)
        else:
            raise AttributeError('Time not yet instantiated, run the simulation first!')

    def plotHistorical(self):
        if self.time is None:
            raise AttributeError('Time not yet instantiated, run the simulation first!')

        days = range(self.time.get_in_days())
        years, histDays = readHistoricalPopulation("BelgianPopulationHistory.txt")
        histYears = []
        for y in years:
            histYears.append((y-1950)*365)

        plt.plot(days, self.totalPop, label="Total Population")
        plt.plot(histYears, histDays)

        plt.xlabel('time in days')
        plt.ylabel('Number of people')

        plt.legend(bbox_to_anchor=(0.5, 1.2), loc=9, ncol=2)
        plt.subplots_adjust(top=.83)

        yearsPrint, daysPrint = self.time.get_years_and_days()
        plt.savefig("pop"+str(yearsPrint)+"y"+str(daysPrint)+"d"+".png")

        x_ticks = [day for day in days if (day % (365*5)) == 0]  # Only pull out full years
        x_labels = [str((i*5)+1950) for i in range(len(x_ticks))]

        plt.xticks(x_ticks, x_labels)
        plt.show()

    def __str__(self):
        return_string = "Children: " + str(self._ChildCount) + "\n"
        return_string += "Adults: " + str(self._AdultCount) + "\n"
        return_string += "Aged: " + str(self._AgedCount) + "\n"
        return_string += "Death: " + str(self._DeathCount) + "\n"
        return_string += "Total Population (alive): " + str(self.getPopulationCount()) + "\n"
        return return_string
