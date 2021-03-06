def convert_SI_units(inputUnit, outputUnit, inputVal):
    SI_factors = {'nm':0.000000001, 'um':0.000001, 'mm':0.001, 'cm':0.01, 'm':1.0, 'km':1000.}
    return inputVal*SI_factors[inputUnit]/SI_factors[outputUnit]

def convert_SI_to_imperial(inputUnit, outputUnit, inputVal):
    imp_SI_factors = {'inch':0.0254, 'foot':0.3048, 'yard':0.9144, 'm':1.0, 'mile':1609.344}
    si_meters_input = convert_SI_units(inputUnit,'m',inputVal)
    return si_meters_input * imp_SI_factors['m']/imp_SI_factors[outputUnit]

def convert_imperial_to_SI(inputUnit, outputUnit, inputVal):
    #convert input to inches
    SI_imp_factors = {'nm':0.00000000393701, 'um':0.00000393701, 'mm':0.0393701, 'cm':0.393701, 'inch':1.0, 'm':39.3701, 'km':39370.1}
    inch_input = convert_imperial_units(inputUnit,'inch',inputVal)
    return inch_input * SI_imp_factors['inch']/SI_imp_factors[outputUnit]

def convert_imperial_units(inputUnit, outputUnit, inputVal):
    imp_factors = {'inch':1.0, 'foot':12.0, 'yard':36.0, 'mile':63360.0}
    return inputVal*imp_factors[inputUnit]/imp_factors[outputUnit]

si_units = ('nm', 'um', 'mm', 'cm', 'm', 'km')
imperial_units = ('inch', 'foot', 'yard', 'mile')
units = ('nm', 'um', 'mm', 'cm', 'm', 'km', 'inch', 'foot', 'yard', 'mile')