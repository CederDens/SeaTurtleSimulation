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


startdate = date(2000, 1, 1)
startpopulation = Population(200, 200, 200, 200, 200, 200, 200, startdate)

sim = SeaTurtleSimulator(startdate, startpopulation)
sim.simulate(20)
