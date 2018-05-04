from datetime import *
from util import *
from math import *


def male2BreedingRate(day):
    e = exp(-0.5*pow(((day - 75) / float(22)), 2))
    return e / (22. * sqrt(2. * pi))


def female2BreedingRate(day):
    e = exp(-0.5 * pow(((day - 61) / float(18)), 2))
    return e / (18. * sqrt(2. * pi))


def hatchRate(temperature):
    denominator = 1 + exp(1.2 * (temperature - 32.6))
    return 0.89 / denominator


def femaleHatchRate(temperature):
    denominator = 1 + exp(-12.585*(temperature-29.198))   # Changed the formula so it fitted the data from the research
    return 1 / float(denominator)


def maleHatchRate(temperature):
    denominator = 1 + exp(-12.585*(temperature-29.198))   # Changed the formula so it fitted the data from the research
    return 1 - (1 / float(denominator))

class Population:
    def __init__(self, init_m_juveniel, init_m_subadult, init_m_adult, init_f_juveniel, init_f_subadult,
                 init_f_not_fertile, init_f_fertile, init_f_aged, init_date):
        self.date = init_date

        self.eggs = 0

        self.m_hatched = 0
        self.m_in_water = 0
        self.m_juveniel = init_m_juveniel
        self.m_subadult = init_m_subadult
        self.m_adult = init_m_adult
        self.m_breeding = 0

        self.f_hatched = 0
        self.f_in_water = 0
        self.f_juveniel = init_f_juveniel
        self.f_subadult = init_f_subadult
        self.f_not_fertile = init_f_not_fertile
        self.f_fertile = init_f_fertile
        self.f_breeding = 0
        self.f_fertilized = 0
        self.f_aged = init_f_aged

    def getMalePopulation(self):
        return self.m_in_water + self.m_hatched + self.m_juveniel + self.m_subadult + self.m_adult + self.m_breeding

    def getFemalePopulation(self):
        return self.f_hatched + self.f_in_water + self.f_juveniel + self.f_subadult + self.f_not_fertile +\
               self.f_fertile + self.f_breeding + self.f_fertilized + self.f_aged

    def getTotalPopulation(self):
        return self.getMalePopulation() + self.getFemalePopulation()

    def updateTime(self):
        self.date += timedelta(1)

    def updateEggs(self, oldPop):
        """:type oldPop Population"""

        new_eggs = oldPop.f_fertilized * 600 / float(90)    # Divided by 90 because females stay 30 days before they lay eggs
        to_hatch = oldPop.eggs / float(55)
        self.eggs += (new_eggs - to_hatch)
        return new_eggs

    def updateFHatched(self, oldPop, temperature):
        """:type oldPop Population"""

        from_egg = oldPop.eggs * hatchRate(temperature) * femaleHatchRate(temperature) / float(55)
        to_death = oldPop.f_hatched * 0.02
        to_water = oldPop.f_hatched * 0.98
        self.f_hatched += (from_egg - to_death - to_water)

    def updateMHatched(self, oldPop, temperature):
        """:type oldPop Population"""

        from_egg = oldPop.eggs * hatchRate(temperature) * maleHatchRate(temperature) / float(55)
        to_death = oldPop.m_hatched * 0.02
        to_water = oldPop.m_hatched * 0.98
        self.m_hatched += (from_egg - to_death - to_water)

    def updateFInWater(self, oldPop):
        """:type oldPop Population"""

        from_hatched = oldPop.f_hatched * 0.98
        to_death = oldPop.f_in_water * 0.6 / float(5)
        to_juv = oldPop.f_in_water * 0.4 / float(5)
        self.f_in_water += (from_hatched - to_death - to_juv)

    def updateMInWater(self, oldPop):
        """:type oldPop Population"""

        from_hatched = oldPop.m_hatched * 0.98
        to_death = oldPop.m_in_water * 0.6 / float(5)
        to_juv = oldPop.m_in_water * 0.4 / float(5)
        self.m_in_water += (from_hatched - to_death - to_juv)

    def updateFJuveniel(self, oldPop):
        """:type oldPop Population"""

        from_water = oldPop.f_in_water * 0.4 / float(5)
        to_death = (oldPop.f_juveniel * 0.1196) / float(14.5 * 365)
        to_subadult = (oldPop.f_juveniel * 0.8804) / float(14.5 * 365)
        self.f_juveniel += (from_water - to_death - to_subadult)

    def updateMJuveniel(self, oldPop):
        """:type oldPop Population"""

        from_water = oldPop.m_in_water * 0.4 / float(5)
        to_death = (oldPop.m_juveniel * 0.1196) / float(14.5 * 365)
        to_subadult = (oldPop.m_juveniel * 0.8804) / float(14.5 * 365)
        self.m_juveniel += (from_water - to_death - to_subadult)

    def updateFSubAdult(self, oldPop):
        """:type oldPop Population"""

        from_juv = oldPop.f_juveniel * 0.8804 / float(14.5 * 365)
        to_death = (oldPop.f_subadult * 0.1526) / float(7 * 365)
        to_not_fertile = (oldPop.f_subadult * 0.8474) / float(7 * 365)
        self.f_subadult += (from_juv - to_death - to_not_fertile)

    def updateMSubAdult(self, oldPop):
        """:type oldPop Population"""

        from_juv = oldPop.m_juveniel * 0.8804 / float(14.5 * 365)
        to_death = (oldPop.m_subadult * 0.1526) / float(7 * 365)
        to_adult = (oldPop.m_subadult * 0.8474) / float(7 * 365)
        self.m_subadult += (from_juv - to_death - to_adult)

    def updateMAdult(self, oldPop):
        """:type oldPop Population"""

        from_sub_adult = (oldPop.m_subadult * 0.8474) / float(7 * 365)
        to_death = oldPop.m_adult / float(58.5 * 365)

        if isMBreedingDate(self.date):
            to_breeding = oldPop.m_adult * male2BreedingRate(getMBreedingDay(self.date)) / float(2)
            from_breeding = oldPop.m_breeding / float(30)
        else:
            to_breeding = 0
            from_breeding = oldPop.m_breeding

        self.m_adult += (from_sub_adult + from_breeding - to_death - to_breeding)

    def updateFNotFertile(self, oldPop):
        """:type oldPop Population"""

        from_sub_adult = (oldPop.f_subadult * 0.8474) / float(7 * 365)
        to_fertile = oldPop.f_not_fertile / float(8.5 * 365)

        self.f_not_fertile += (from_sub_adult - to_fertile)

    def updateFFertile(self, oldPop):
        """:type oldPop Population"""

        from_not_fertile = oldPop.f_not_fertile / float(8.5 * 365)
        from_fertilized = oldPop.f_fertilized / float(90)
        to_aged = oldPop.f_fertile / float(20 * 365)

        if isFBreedingDate(self.date):
            to_breeding = oldPop.f_fertile * female2BreedingRate(getFBreedingDay(self.date)) / float(5)
            from_breeding = oldPop.f_breeding / float(60)
        else:
            to_breeding = 0
            from_breeding = oldPop.f_breeding

        self.f_fertile += (from_not_fertile + from_breeding + from_fertilized - to_aged - to_breeding)

    def updateFAged(self, oldPop):
        """:type oldPop Population"""

        from_fertile = oldPop.f_fertile / float(20 * 365)
        to_death = oldPop.f_aged / float(30 * 365)
        self.f_aged += (from_fertile - to_death)

    def updateFBreeding(self, oldPop, lam):
        """:type oldPop Population"""

        if isFBreedingDate(self.date):
            from_fertile = oldPop.f_fertile * female2BreedingRate(getFBreedingDay(self.date)) / float(5)
            to_fertile = oldPop.f_breeding / float(60)
        else:
            from_fertile = 0
            to_fertile = oldPop.f_breeding

        to_fertilized = oldPop.f_breeding * oldPop.m_breeding * lam    # used square root for a stable population
        self.f_breeding += (from_fertile - to_fertile - to_fertilized)

    def updateMBreeding(self, oldPop):
        """:type oldPop Population"""

        if isMBreedingDate(self.date):
            from_adult = oldPop.m_adult * male2BreedingRate(getMBreedingDay(self.date)) / float(2)
            to_adult = oldPop.m_breeding / float(30)
        else:
            from_adult = 0
            to_adult = oldPop.m_breeding


        self.m_breeding += (from_adult - to_adult)

    def updateFFertilized(self, oldPop, lam):
        """:type oldPop Population"""

        from_breeding = oldPop.f_breeding * oldPop.m_breeding * lam    # used square root for a stable population
        to_fertile = oldPop.f_fertilized / float(90)

        self.f_fertilized += (from_breeding - to_fertile)

    def __repr__(self):
        ret = Color.BOLD + "Population on: %s\n" % self.date + Color.END
        ret += "  ---> Male population: %f\n" % self.getMalePopulation()
        ret += "  ---> Female population: %f\n" % self.getFemalePopulation()
        ret += "  ---> Total population: %f\n" % self.getTotalPopulation()
        ret += "  ---> Number of eggs: %f\n" % self.eggs
        ret += "\n"
        return ret
