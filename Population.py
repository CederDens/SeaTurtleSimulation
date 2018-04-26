from datetime import timedelta


class Population:
    def __init__(self, init_m_juveniel, init_m_subadult, init_m_adult, init_f_juveniel, init_f_subadult, init_f_adult,
                 init_f_fertile, init_date):

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
        self.f_adult = init_f_adult
        self.f_fertile = init_f_fertile
        self.f_breeding = 0
        self.f_fertilized = 0

    def updateTime(self):
        self.date += timedelta(1)

    def updateEggs(self, eggs):
        self.eggs += eggs

    def __repr__(self):
        return 'Date: %s\nEggs: %i\n' % (self.date, self.eggs)
