from BelgiumPopSimulator import *
from util import *

# Estimation of population in 2013
init_child_count = 2553720
init_adult_count = 2910078
init_aged_count = 5516392

sim = BelgiumPopSimulator(init_child_count, init_adult_count, init_aged_count)

print "Total initial population:", sim.getPopulationCount()

sim.simulate(Time(years=5))
