from SeaTurtleSimulator import *
from util import *

startpopcount = 200000000

maleRate = 1 / 7.66
femaleRate = 6.66 / 7.66

init_m_juveniel = maleRate * startpopcount * (14.5 / 80)
init_m_subadult = maleRate * startpopcount * (7.0 / 80)
init_m_adult = maleRate * startpopcount * (58.5 / 80)

init_f_juveniel = femaleRate * startpopcount * (14.5 / 80)
init_f_subadult = femaleRate * startpopcount * (7.0 / 80)
init_f_not_fertile = femaleRate * startpopcount * (8.5 / 80)
init_f_fertile = femaleRate * startpopcount * (20.0 / 80)
init_f_aged = femaleRate * startpopcount * (30.0 / 80)


# for lam in getTestRange(3.14597/pow(10, 11), 1/pow(10, 17)):
#     startdate = date(1700, 4, 1)
#     startpopulation = Population(init_m_juveniel, init_m_subadult, init_m_adult, init_f_juveniel, init_f_subadult,
#                                  init_f_not_fertile, init_f_fertile, init_f_aged, startdate)
#
#     sim = SeaTurtleSimulator(startdate, startpopulation, lam)
#     sim.simulate(timedelta(toDays(years=1000)), 29.348)
#     sim.plot()



startdate = date(1700, 4, 1)
startpopulation = Population(init_m_juveniel, init_m_subadult, init_m_adult, init_f_juveniel, init_f_subadult,
                             init_f_not_fertile, init_f_fertile, init_f_aged, startdate)

sim = SeaTurtleSimulator(startdate, startpopulation, 3.1459/pow(10, 11))
sim.simulate(timedelta(toDays(years=1000)), 29.348)
sim.plot()


# startdate = date(1700, 4, 1)
# startpopulation = Population(init_m_juveniel, init_m_subadult, init_m_adult, init_f_juveniel, init_f_subadult,
#                              init_f_not_fertile, init_f_fertile, init_f_aged, startdate)
#
# sim = SeaTurtleSimulator(startdate, startpopulation, 3.145972*pow(10, -11))
# sim.simulate(timedelta(toDays(years=100)), 29.348)
# sim.plot()
# sim.plot(True)

# readStablePops()