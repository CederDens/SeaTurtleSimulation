from datetime import timedelta
from util import *


class Population:
    def __init__(self, init_m_juveniel, init_m_subadult, init_m_adult, init_f_juveniel, init_f_subadult,
                 init_f_not_fertile, init_f_fertile, init_f_aged, init_date):
        self.date = init_date

        self.eggs = 0

        self.m_hatched = 0
        self.m_in_water = 0
        self.m_in_rif = 0
        self.m_juveniel = init_m_juveniel
        self.m_subadult = init_m_subadult
        self.m_adult = init_m_adult
        self.m_breeding = 0

        self.f_hatched = 0
        self.f_in_water = 0
        self.f_in_rif = 0
        self.f_juveniel = init_f_juveniel
        self.f_subadult = init_f_subadult
        self.f_not_fertile = init_f_not_fertile
        self.f_fertile = init_f_fertile
        self.f_breeding = 0
        self.f_fertilized = 0
        self.f_aged = init_f_aged

    def getMalePopulation(self):
        return self.m_in_water + self.m_hatched + self.m_in_rif + self.m_juveniel + self.m_subadult + self.m_adult + \
               self.m_breeding

    def getFemalePopulation(self):
        return self.f_hatched + self.f_in_water + self.f_in_rif + self.f_juveniel + self.f_subadult + \
               self.f_not_fertile + self.f_fertile + self.f_breeding + self.f_fertilized + self.f_aged

    def getTotalPopulation(self):
        return self.getMalePopulation() + self.getFemalePopulation()

    def updateTime(self):
        self.date += timedelta(1)

    def updateEggs(self, oldPop):
        """:type oldPop Population"""

        pass

    def updateFHatched(self, oldPop):
        """:type oldPop Population"""

        from_egg = 0  # TODO
        to_death = oldPop.f_hatched * 0.02
        to_water = oldPop.f_hatched * 0.98
        self.f_hatched += (-to_death - to_water + from_egg)

    def updateMHatched(self, oldPop):
        """:type oldPop Population"""

        from_egg = 0  # TODO
        to_death = oldPop.m_hatched * 0.02
        to_water = oldPop.m_hatched * 0.98
        self.m_hatched += (from_egg - to_death - to_water)

    def updateFInWater(self, oldPop):
        """:type oldPop Population"""

        # TODO: do they go from water to juveniel (only 40%) or goes 40% from water to rif and then all to juveniel?
        from_hatched = oldPop.f_hatched * 0.98
        to_rif = oldPop.f_in_water
        self.f_in_water += (from_hatched - to_rif)

    def updateMInWater(self, oldPop):
        """:type oldPop Population"""

        # TODO: do they go from water to juveniel (only 40%) or goes 40% from water to rif and then all to juveniel?
        from_hatched = oldPop.m_hatched * 0.98
        to_rif = oldPop.m_in_water
        self.m_in_water += (from_hatched - to_rif)

    def updateFInRif(self, oldPop):
        """:type oldPop Population"""

        pass

    def updateMInRif(self, oldPop):
        """:type oldPop Population"""

        pass

    def updateFJuveniel(self, oldPop):
        """:type oldPop Population"""

        from_rif = 0    # TODO
        to_death = (oldPop.f_juveniel * 0.1196) / (14.5 * 365)
        to_subadult = (oldPop.f_juveniel * 0.8804) / (14.5 * 365)
        self.f_juveniel += (from_rif - to_death - to_subadult)

    def updateMJuveniel(self, oldPop):
        """:type oldPop Population"""

        from_rif = 0    # TODO
        to_death = (oldPop.m_juveniel * 0.1196) / (14.5 * 365)
        to_subadult = (oldPop.m_juveniel * 0.8804) / (14.5 * 365)
        self.m_juveniel += (from_rif - to_death - to_subadult)

    def updateFSubAdult(self, oldPop):
        """:type oldPop Population"""

        pass

    def updateMSubAdult(self, oldPop):
        """:type oldPop Population"""

        pass

    def __repr__(self):
        ret = Color.BOLD + "Population on: %s\n" % self.date + Color.END
        ret += "  ---> Male population: %i\n" % self.getMalePopulation()
        ret += "  ---> Female population: %i\n" % self.getFemalePopulation()
        ret += "  ---> Total population: %i\n" % self.getTotalPopulation()
        ret += "  ---> Number of eggs: %i\n" % self.eggs
        ret += "\n"
        return ret
