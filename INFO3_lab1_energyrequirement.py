#lab1_2.3
def basalMetabolicRate(Gender, BodyWeight, Height, Age):
    BMR = 10*BodyWeight + 6.25*Height - 5.0*Age
    if Gender == 'F':
        BMR -= 161
    elif Gender == 'M':
        BMR += 5
    return BMR


#lab1_2.5(unit test)
print(basalMetabolicRate('F', 60, 165, 40)==1270.25)
print(basalMetabolicRate('M', 60, 165, 40)==1436.25)


#lab1_2.7
def basalMetabolicRate(Gender, BodyWeight, Height, Age):
    BMR = 10*BodyWeight + 6.25*Height - 5.0*Age
    if Gender == 'F':
        BMR -= 161
    elif Gender == 'M':
        BMR += 5
    return BMR

def dailyEnergyRequirement(Gender, BodyWeight, Height, Age, PhysicalActivitylevel):
    if PhysicalActivitylevel == 'sedentary':
        k = 1.4
    elif PhysicalActivitylevel == 'light':
        k = 1.6
    elif PhysicalActivitylevel == 'moderate':
        k = 1.75
    elif PhysicalActivitylevel == 'intense':
        k = 1.9
    elif PhysicalActivitylevel == 'very intense':
        k = 12.1
    return k*basalMetabolicRate(Gender, BodyWeight, Height, Age)


#lab1_2.8, 3
g = 'F'
w = 60.0
h = 165
a = 40
k = 'light'
needed_calories = dailyEnergyRequirement(g, w, h, a, k)
print(needed_calories)


#lab1_4
def multiply_by_two(nb):
    return nb*2

x = 12
print(x)
x = multiply_by_two(x)
print(x)
