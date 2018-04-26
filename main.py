from BelgiumPopSimulator import *
from util import *
from SeaTurtleSimulator import *
from datetime import date

# Estimation of the population in 2013
# init_child_count = 2553720          # = 23.26%
# init_adult_count = 2910078          # = 26.51%
# init_aged_count = 5516392           # = 50.23%

# Estimation of the population in 1950
# totPop = 8639000
# init_child_count = totPop*0.2326          # = 23.26%
# init_adult_count = totPop*0.2651          # = 26.51%
# init_aged_count = totPop*0.5023           # = 50.23%
#
# sim = BelgiumPopSimulator(init_child_count, init_adult_count, init_aged_count)
#
# print "Total initial population:", sim.getPopulationCount()
#
# sim.simulate(Time(years=66))
# sim.plotHistorical()
#

startpopcount = 40000

init_m_juveniel = (1 / 7.66) * startpopcount * (14.5 / 80)
init_m_subadult = (1 / 7.66) * startpopcount * (7.0 / 80)
init_m_adult = (1 / 7.66) * startpopcount * (58.5 / 80)

init_f_juveniel = (6.66 / 7.66) * startpopcount * (14.5 / 80)
init_f_subadult = (6.66 / 7.66) * startpopcount * (7.0 / 80)
init_f_not_fertile = (6.66 / 7.66) * startpopcount * (8.5 / 80)
init_f_fertile = (6.66 / 7.66) * startpopcount * (20.0 / 80)
init_f_aged = (6.66 / 7.66) * startpopcount * (30.0 / 80)

startdate = date(2000, 1, 1)
startpopulation = Population(init_m_juveniel, init_m_subadult, init_m_adult, init_f_juveniel, init_f_subadult,
                             init_f_not_fertile, init_f_fertile, init_f_aged, startdate)

sim = SeaTurtleSimulator(startdate, startpopulation)
sim.simulate(20)
