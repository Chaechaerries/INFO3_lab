#lab2_5.5: Compute 음식별 환경오염정도
def computeEnvironmentalImpact(mymeal, myamounts, LUdic, GHGdic, Aciddic, Eutrophdic, SWWdic):
    LU = 0
    GHG = 0
    Acid = 0
    Eutroph = 0
    SWW = 0
    for a, b in enumerate(mymeal): 
        LU += myamounts[a]*LUdic[b]             #각 음식의 양*음식별 환경오염 정도
        GHG += myamounts[a]*GHGdic[b]
        Acid += myamounts[a]*Aciddic[b]
        Eutroph += myamounts[a]*Eutrophdic[b]
        SWW += myamounts[a]*SWWdic[b]
    return [LU, GHG, Acid, Eutroph, SWW]

#lab2_5.6: Unit test - computeEnvironmentalImapct의 return 값을 받아 실행.
def printEnvironmentalImpact(myimpact):
    print("This meal uses  {0:6.1f} square meters of land.".format(myimpact[0]))
    print("This meal emits {0:6.1f} kg CO2 eq. (greenhous gas emissions).".format(myimpact[1]))
    print("This meal emits {0:6.1f} g SO2 eq. (acidifying emissions).".format(myimpact[2]))
    print("This meal emits {0:6.1f} g PO43- eq. (eutrophying emissions).".format(myimpact[3]))
    print("This meal uses  {0:6.0f} L of freshwater.".format(myimpact[4]))

#lab2_5.7: 
def BelowThresholds(myimpact, Thresholds):
    mealOK = False
    for i in range(len(Thresholds)):
        if myimpact[i] < Thresholds[i]:
            mealOK = True
            break
    if mealOK:      #기본적으로 True
        return True
    else:
        return False
            
    

#lab2_5.4: 5개 list 만들기(LU, GHG, Acid, Eutroph, SWW)
if __name__ == "__main__":
    LU_dict = {'Wheat & Rye (Bread)': 2.7,
                    'Maize (Meal)': 1.8,
                    'Potatoes': 0.8,
                    'Beet Sugar': 1.5,
                    'Tofu': 3.4,
                    'Rapeseed Oil': 9.4,
                    'Olive Oil': 17.3,
                    'Tomatoes': 0.2,
                    'Root Vegetables': 0.3,
                    'Other Vegetables': 0.2,
                    'Bananas': 1.4,
                    'Apples': 0.5,
                    'Berries & Grapes': 2.6,
                    'Coffee': 11.9,
                    'Dark Chocolate': 53.8,
                    'Bovine Meat (beef herd)': 170.4,
                    'Poultry Meat': 11.0,
                    'Eggs': 5.7
                  }

    GHG_dict = {'Wheat & Rye (Bread)': 1.3,
                    'Maize (Meal)': 1.2,
                    'Potatoes': 0.5,
                    'Beet Sugar': 1.8,
                    'Tofu': 2.6,
                    'Rapeseed Oil': 3.5,
                    'Olive Oil': 5.1,
                    'Tomatoes': 0.7,
                    'Root Vegetables': 0.4,
                    'Other Vegetables': 0.4,
                    'Bananas': 0.8,
                    'Apples': 0.4,
                    'Berries & Grapes': 1.4,
                    'Coffee': 8.2,
                    'Dark Chocolate': 5.0,
                    'Bovine Meat (beef herd)': 60.4,
                    'Poultry Meat': 7.5,
                    'Eggs': 4.2
                  }

    Acid_dict = {'Wheat & Rye (Bread)': 13.3,
                    'Maize (Meal)': 10.2,
                    'Potatoes': 3.6,
                    'Beet Sugar': 12.4,
                    'Tofu': 6.0,
                    'Rapeseed Oil': 23.2,
                    'Olive Oil': 33.9,
                    'Tomatoes': 5.2,
                    'Root Vegetables': 2.9,
                    'Other Vegetables': 3.7,
                    'Bananas': 6.1,
                    'Apples': 4.0,
                    'Berries & Grapes': 6.9,
                    'Coffee': 87.2,
                    'Dark Chocolate': 29.0,
                    'Bovine Meat (beef herd)': 270.9,
                    'Poultry Meat': 64.7,
                    'Eggs': 54.2
                  }

    Eutroph_dict = {'Wheat & Rye (Bread)': 5.4,
                    'Maize (Meal)': 2.4,
                    'Potatoes': 4.4,
                    'Beet Sugar': 4.3,
                    'Tofu': 6.6,
                    'Rapeseed Oil': 16.4,
                    'Olive Oil': 39.1,
                    'Tomatoes': 1.9,
                    'Root Vegetables': 1.0,
                    'Other Vegetables': 1.8,
                    'Bananas': 2.1,
                    'Apples': 2.0,
                    'Berries & Grapes': 1.0,
                    'Coffee': 49.9,
                    'Dark Chocolate': 67.3,
                    'Bovine Meat (beef herd)': 320.7,
                    'Poultry Meat': 34.5,
                    'Eggs': 21.3
                  }

    SWW_dict = {'Wheat & Rye (Bread)': 12822,
                    'Maize (Meal)': 350,
                    'Potatoes': 78,
                    'Beet Sugar': 115,
                    'Tofu': 32,
                    'Rapeseed Oil': 14,
                    'Olive Oil': 24396,
                    'Tomatoes': 4481,
                    'Root Vegetables': 38,
                    'Other Vegetables': 2940,
                    'Bananas': 31,
                    'Apples': 1025,
                    'Berries & Grapes': 16245,
                    'Coffee': 341,
                    'Dark Chocolate': 220,
                    'Bovine Meat (beef herd)': 441,
                    'Poultry Meat': 334,
                    'Eggs': 18621
                  }

    Meals = ['Poultry Meat', 'Wheat & Rye (Bread)', 'Olive Oil', 'Root Vegetables', 'Berries & Grapes', 'Coffee']
    Amounts = [0.05, 0.12, 0.016, 0.125, 0.05, 0.008]    #5.4에서 사용했던, 음식종류 & 양
    Impact = computeEnvironmentalImpact(Meals, Amounts, LU_dict, GHG_dict, Acid_dict, Eutroph_dict, SWW_dict)
    printEnvironmentalImpact(Impact)     #computeEnvironmentalImpact의 값을 list로 받아 실행.
    print("A meal of unit test is below some thresholds:")
    print(BelowThresholds(Impact, [2.0, 1.5, 7.0, 7.0, 1000])==True) #thresholds의 값은 주어짐(문제에는 없지만..?)   
    
    