from SeaTurtleSimulator import *
from util import *

startpopcount = 40000

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

startdate = date(1700, 4, 1)
startpopulation = Population(init_m_juveniel, init_m_subadult, init_m_adult, init_f_juveniel, init_f_subadult,
                             init_f_not_fertile, init_f_fertile, init_f_aged, startdate)

sim = SeaTurtleSimulator(startdate, startpopulation)
sim.simulate(timedelta(toDays(years=300)), 29.348)
sim.plot()

# print femaleHatchRate(29.3 + 0.4)
# temps = readTemps()
# adulttemp = []
# juvtemp = []
# subadulttemp = []
# for k, v in temps.items():
#     if k <= 1993:
#         adulttemp.append(v)
#     elif k <= 2000:
#         subadulttemp.append(v)
#     elif k <= 2010:
#         juvtemp.append(v)
#
# print sum(adulttemp) / float(len(adulttemp))
# print sum(subadulttemp) / float(len(subadulttemp))
# print sum(juvtemp) / float(len(juvtemp))
