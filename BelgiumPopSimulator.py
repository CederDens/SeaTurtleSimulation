import matplotlib.pyplot as plt

from util import Time

births_per_person_per_year = 0.01086 + 0.00425 + 0.003  # births + migration + unknown marge
deaths_per_person_per_year = 0.00986


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
        return deaths_per_person_per_year*self.getPopulationCount()/365.0

    def births(self):
        return births_per_person_per_year*self.getPopulationCount()/365.0

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

        plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
                   ncol=2, mode="expand", borderaxespad=0.)

        plt.show()

    def simulate(self, time):
        """

        :type time: Time
        """
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

        self.showPlot(time)

    def __str__(self):
        return_string = "Children: " + str(self._ChildCount) + "\n"
        return_string += "Adults: " + str(self._AdultCount) + "\n"
        return_string += "Aged: " + str(self._AgedCount) + "\n"
        return_string += "Death: " + str(self._DeathCount) + "\n"
        return_string += "Total Population (alive): " + str(self.getPopulationCount()) + "\n"
        return return_string
