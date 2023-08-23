class ElectricSocket:
    def supply_electricity(voltage):
        print("current!")

# Американская вилка
class UsaFork(ElectricSocket):
    def power_usa(self):
        print('power on. Usa')

    def supply_electricity(voltage):
        return super().supply_electricity()    


# Европейская вилка
class EuroFork(ElectricSocket):
    def power_euro(self):
        print('power on. Euro')

    def supply_electricity(voltage):
        return super().supply_electricity()    


# Американская розетка
class UsaSocket:
    def __init__(self, fork):
        self.fork = fork

    def connect(self):
        self.fork.power_usa()
       
# Американская розетка
class EuroSocket:
    def __init__(self, fork):
        self.fork = fork

    def connect(self):
        self.fork.power_euro()

# Вставляем американскую вилку в американскую розетку.
uf = UsaFork()
us = UsaSocket(uf)
us.connect()
uf.supply_electricity()
# >>> power on. Usa

# Вставляем evroвилку в evro розетку.
ef = EuroFork()
us = EuroSocket(ef)
us.connect()
ef.supply_electricity()
# >>> power on. Usa

# При попытке вставить европейскую вилку в американскую розетку, будет ошибка
ef = EuroFork() 
us = UsaSocket(ef) 
#us.connect() 
# >>> AttributeError: 'EuroFork' object has no attribute 'power_usa'

class USPlugAdapter:
    
    def __init__(self):
        self._euro_fork = EuroFork()

    def power_usa(self):
        self._euro_fork.power_euro()
        self._euro_fork.supply_electricity()

# Вставляем американскую вилку в американскую розетку. 
uf = UsaFork() 
us = UsaSocket(uf) 
us.connect() 
uf.supply_electricity()
# >>> power on. Usa

# Вставляем евро-адаптер в американскую розетку. 
ad = USPlugAdapter()
us = UsaSocket(ad)
us.connect() 
# >>> power on. Euro        