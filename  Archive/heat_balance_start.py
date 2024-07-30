import requests
import random
import string
from datetime import datetime
import sys
import json


dict_toAPI = {
    'UserInput': ['Отбензиненное сырье', 'Теплоноситель ТЛВ-330',
                      [
                          [
                              ['i-Pentane / i-C5 / C5H12', 'n-Pentane / Pentane / C5H12', '22-Mbutane / 22-MC4 / C6H14',
                               'Cyclopentane / CC5 / C5H10', '23-Mbutane / 23-MC4 / C6H14', '2-Mpentane / 2-MC5 / C6H14',
                               '3-Mpentane / 3-MC5 / C6H14', 'n-Hexane / C6 / C6H14', 'Mcyclopentan / MCC5 / C6H12',
                               '22-Mpentane / 22-MC5 / C7H16', '24-Mpentane / 24-MC5 / C7H16', 'Benzene / Benzene / C6H6',
                               'Cyclohexane / CC6 / C6H12'],
                              [95, 105, 115, 125, 135, 145, 155, 165, 175, 185, 195, 205, 215, 225, 235,
                               245, 255, 265, 275, 285, 295, 305, 315, 325, 335],
                              'prsv',
                              [0.05, 0.21, 0.05, 0.13, 0.18, 1.05, 0.67, 2.25, 1.55, 0.08, 0.15, 0.13, 3.06],
                              [6.85, 18.36, 26.81, 34.93, 44.3, 50.38, 55.02, 59.81, 63.42999999999999, 66.27,
                               68.91, 71.02, 72.75, 74.92, 76.91, 79.22, 80.90000000000001, 82.47, 83.91, 85.22, 86.40000000000001,
                               87.46000000000001, 88.38000000000001, 89.16000000000001, 89.88000000000001],
                              [172.2, 182.5],
                              421.325,
                              None,
                              'mass',
                              20,
                              50
                          ],
                          [
                              [],
                              [],
                              None,
                              [],
                              [],
                              [290, 215],
                              1601.325,
                              148036,
                              'mass',
                              50,
                              50
                          ]
                      ]
                  ],
    'HBArrCOLD': [],
    'HBArrHOT': [
        {'FLOW':
             {'Components': [],
              'HL_Comps': 0,
              'HL_MoleFr': 0,
              'Heat Flow': 0,
              'Heavy Liquid': 0,
              'Inerts': 0,
              'LL_Comps': 0,
              'LL_MoleFr': 0,
              'Light Liquid': 41.12,
              'Mass Flow': 41.12,
              'Pressure': 1600000.0,
              'Temperature': 215,
              'V_Comps': [],
              'V_MoleFr': [],
              'Vapour': 0
              },
    'PROPERTIES': {
        'Enthalpy': 398888,
        'Heavy Liquid':{
            'absolute_viscosity': None,
            'constant_p_specific_heat': None,
            'density': None,
            'thermal_conductivity': None,
            'surface_tension': None
            },
        'Inerts': {
            'absolute_viscosity': None,
            'constant_p_specific_heat': None,
            'density': None,
            'thermal_conductivity': None
            },
        'Light Liquid': {
            'absolute_viscosity': 1.04,
            'constant_p_specific_heat': 2258,
            'density': 856.9,
            'thermal_conductivity': 0.1457,
            'surface_tension': None
            },
        'Vapour': {
            'absolute_viscosity': None,
            'constant_p_specific_heat': None,
            'density': None,
            'thermal_conductivity': None
            }
        }
    },
        {'FLOW':
             {'Components': [],
              'HL_Comps': 0,
              'HL_MoleFr': 0,
              'Heat Flow': 0,
              'Heavy Liquid': 0,
              'Inerts': 0,
              'LL_Comps': 0,
              'LL_MoleFr': 0,
              'Light Liquid': 41.12,
              'Mass Flow': 41.12,
              'Pressure': 1600000.0,
              'Temperature': 290,
              'V_Comps': [],
              'V_MoleFr': [],
              'Vapour': 0
              },
         'PROPERTIES': {
             'Enthalpy': 578220,
             'Heavy Liquid':
                 {
                     'absolute_viscosity': None,
                     'constant_p_specific_heat': None,
                     'density': None,
                     'thermal_conductivity': None,
                     'surface_tension': None
                 },
            'Inerts': {
                'absolute_viscosity': None,
                'constant_p_specific_heat': None,
                'density': None,
                'thermal_conductivity': None
                    },
             'Light Liquid':
                 {'absolute_viscosity': 0.4499,
                  'constant_p_specific_heat': 2520,
                  'density': 800.9,
                  'thermal_conductivity': 0.1305,
                  'surface_tension': None},
             'Vapour':
                 {'absolute_viscosity': None,
                  'constant_p_specific_heat': None,
                  'density': None,
                  'thermal_conductivity': None}}
         }
    ],
    'type': 'mix', 'mode': 'hotside','hss_url': 'http://10.10.10.32:5000'}
type_calculation = "heat_balance"
lang = 'en'
r = random.randint(0, 4)
a = [1455, 1877, 1355, 9548, 6432]
b = {
    '1455': 19052013,
    '1877': 28791562,
    '1355': 59843251,
    '9548': 91245684,
    '6432': 72648953
}
login = a[r]
password = b[str(login)]
dict_toAPI_str = json.dumps(dict_toAPI)
API_URL = 'http://192.168.1.145:8000/task_create'
data = {'login': login, 'password': password, 'dict_toAPI_str': dict_toAPI_str, 'lang': lang, "type_calculation": type_calculation}
result = requests.post(API_URL, params=data)
print(result)
print(result.text)




