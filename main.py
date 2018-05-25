from SeaTurtleSimulator import *
from util import *

startpopcount = 35000000

maleRate = 1 / 7.66
femaleRate = 6.66 / 7.66

init_m_juveniel = maleRate * startpopcount * (1000. * 14.5) / 17297.
init_m_subadult = maleRate * startpopcount * (316. * 7.0) / 17297.
init_m_adult = maleRate * startpopcount * (10. * 58.5) / 17297.

init_f_juveniel = femaleRate * startpopcount * (1000. * 14.5) / 18062.
init_f_subadult = femaleRate * startpopcount * (316. * 7.0) / 18062.
init_f_not_fertile = femaleRate * startpopcount * (100. * 8.5) / 18062.
init_f_fertile = femaleRate * startpopcount * (10. * 20.0) / 18062.
init_f_aged = femaleRate * startpopcount * (10. * 30.0) / 18062.

# for scenario in range(1, 6):
scenario = 5
startdate = date(1900, 4, 1)
startpopulation = Population(init_m_juveniel, init_m_subadult, init_m_adult, init_f_juveniel, init_f_subadult,
                             init_f_not_fertile, init_f_fertile, init_f_aged, startdate)

sim = SeaTurtleSimulator(startdate, startpopulation, 4.6407886/pow(10, 8))
sim.simulate(timedelta(toDays(years=250)), scenario)
sim.plot(scenario)
sim.plot(scenario, True)
sim.plotCompartments()

# readStablePops()


# startdate = date(1700, 4, 1)
# startpopulation = Population(init_m_juveniel, init_m_subadult, init_m_adult, init_f_juveniel, init_f_subadult,
#                              init_f_not_fertile, init_f_fertile, init_f_aged, startdate)
#
# sim = SeaTurtleSimulator(startdate, startpopulation, 1.624276/pow(10, 6))
# sim.plotTemperature()