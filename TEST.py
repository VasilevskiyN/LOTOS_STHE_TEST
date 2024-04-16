import math

GENERAL = {}
SHELL = {
        't1': 0, 't2': 0,'G': 0, 'alfa': 0
         }
TUBE = {
        't1': 0, 't2': 0,  'G': 0, 'alfa': 0
         }




class HeatExchanger:
    pipe_diameter = int(input('Введите диаметр трубы, мм'))
    pipe_lengh = int(input('Введите длину трубы, мм'))
    global GENERAL
    GENERAL['pipe_diametr'] = pipe_diameter
    GENERAL['pipe_lengh'] = pipe_lengh


    def __init__(self, t1, t2, G, name):
        self.t1 = t1
        self.t2 = t2
        self.G = G
        self.name = name
        super().__init__()
    pass


class HeatExchangerSurface:
    def __init__(self):
            print('Расчет теплопередачи')
            print('Температурный напор =', ((SHELL['t1']-TUBE['t2'])-(SHELL['t2']-TUBE['t1']))/math.log((SHELL['t1']-TUBE['t2'])/(SHELL['t2']-TUBE['t1'])))
            print('Проверка поверхности')
            global GENERAL, SHELL, TUBE



class Condensation(HeatExchanger, HeatExchangerSurface):
    def __init__(self,t1, t2, G, name):
        super().__init__(t1, t2, G, name)
        print('Re не определяется')
        print('Nu не определяется')
        print('alfa зависит от температур', t1, t2)
        alfa = t1 + t2
        self.alfa = alfa
        if self.name.upper() == "SHELL":
            global SHELL
            SHELL = vars(self)
        if self.name.upper() == "TUBE":
            global TUBE
            TUBE = vars(self)



class PipeSpace(HeatExchanger, HeatExchangerSurface):
    def __init__(self, t1, t2, G, name):
        super().__init__(t1, t2, G, name)
        print('Re зависит от расхода', G)
        print('Nu зависит от температур', t1, t2)
        print('alfa')
        alfa = t1 + t2
        self.alfa = alfa
        if self.name.upper() == "SHELL":
            global SHELL
            SHELL = vars(self)
        if self.name.upper() == "TUBE":
            global TUBE
            TUBE = vars(self)

class InterpipeSpace(HeatExchanger, HeatExchangerSurface):
    def __init__(self, t1, t2, G, name):
        super().__init__(t1, t2, G, name)
        print('Re зависит от расхода', G)
        print('Nu зависит от температур', t1, t2)
        print('alfa')
        alfa = t1 + t2
        self.alfa = alfa
        if self.name.upper() == "SHELL":
            global SHELL
            SHELL = vars(self)
        if self.name.upper() == "TUBE":
            global TUBE
            TUBE = vars(self)

class Evaporation(HeatExchanger, HeatExchangerSurface):
    def __init__(self, t1, t2, G, name):
        super().__init__(t1, t2, G, name)
        print('Re не влияет')
        print('Nu зависит от температур', t1, t2)
        print('alfa')
        alfa = t1 + t2
        self.alfa = alfa
        if self.name.upper() == "SHELL":
            global SHELL
            SHELL = vars(self)
        if self.name.upper() == "TUBE":
            global TUBE
            TUBE = vars(self)

Shell = Condensation(105, 105, 50, 'Shell')
Tube = PipeSpace(20, 30 ,100, 'Tube')
