
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


def readHistoricalPopulation(fileName):
    years = []
    popSize = []
    histFile = open(fileName, 'r')
    for line in histFile:
        years.append(int(line.split()[0]))
        popSize.append(int(float(line.split()[1].replace(',', '.'))*1000000))
    return years, popSize
