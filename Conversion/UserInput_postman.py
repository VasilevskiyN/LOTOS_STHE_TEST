# 1. Выбрать систему единиц исчесления си?
# 2.

v2 = {
    "method": "heat_balance",
    "data": {
        "UserInput": {
            "cold": {
                "flow_name": "Осушенный газ",         # Name of cold flow, don't used in calculation
                "t_in": 20,                           # Inlet temperature for cold fluid, °С
                "t_out": 45,                          # Outlet temperature for cold fluid, °С
                "P_ab": 5101.325,                     # Inlet total pressure, kPa
                "G": 4629,                            # Mass flow rate for cold fluid, kg/hour
                "components": [                       # You can specify any number of components
                    {
                        "name": "Nitrogen / N2 / N2", # Name component
                        "fraction": 0.002             # Fraction this component
                    },
                    {
                        "name": "Methane / C1 / CH4", # Name component
                        "fraction": 0.881             # Fraction this component
                    },
                    {
                        "name": "Ethane / C2 / C2H6", # Name component
                        "fraction": 0.117             # Fraction this component
                    }
                ],
                "property_package": "prsv",           # Property Generation Package
                "fraction_type": "mass",              # Fraction type: mass or mole
                "vacuum_distillation": [                        # It is used in devices of the petrochemical industry,
                    {"temperature": 100, "fraction": 0.005},    # specify the temperatures at which the yield
                    {"temperature": 110, "fraction": 0.012},    # of volatile substances is known.The concentration
                    {"temperature": 120, "fraction": 0.014},    # of boiled components should be indicated
                    {"temperature": 130, "fraction": 0.025},    # relative to the completely liquid phase.
                    {"temperature": 140, "fraction": 0.054},    # The temperature is indicated in °С,
                ]                                               # fraction is indicated in mass fraction.
                                                                # You can specify any number of points.
            },

            "hot": {
                "flow_name": "50% р-р пропиленгликоля",         # Name of hot flow, don't used in calculation
                "t_in": 90,                          # Inlet temperature for hot fluid, °С
                "t_out": 7,                          # Outlet temperature for hot fluid, °С
                "P_ab": 701.325,                     # Inlet total pressure, kPa
                "G": 4176,                           # Mass flow rate for hot fluid, kg/hour
                "components": [                      # You can specify any number of components
                    {
                        "name": "12-C3diol / 1;2-Propylene_Glycol / C3H8O2",  # Name component
                        "fraction": 0.5                                       # Fraction this component
                    },
                    {
                        "name": "H2O / H2O / H2O",  # Name component
                        "fraction": 0.5             # Fraction this component
                    },
                ],
                "property_package": "glycolpkg",     # Property Generation Package
                "fraction_type": "mass",             # Fraction type: mass or mole
                "vacuum_distillation": []                       # It is used in devices of the petrochemical industry,
                                                                # specify the temperatures at which the yield
                                                                # of volatile substances is known.The concentration
                                                                # of boiled components should be indicated
                                                                # relative to the completely liquid phase.
                                                                # The temperature is indicated in °С,
                                                                # fraction is indicated in mass fraction.
                                                                # You can specify any number of points.
            }
        }
    }
}
