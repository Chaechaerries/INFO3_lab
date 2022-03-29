import numpy as np

#4. Project/Lists, 5. Project/Dictionaries and lists
#lab2_4.2: 6개 list 만들기(6가지 food type: CarbSource, Extra, FatSource, Fruit, ProteinSource, Vegetable)
#lab2_4.3: 가능한 meal의 list 만들고, return하는 함수(def) 작성(6가지 type 한 개씩 포함.) / unit test + docstring 작성
def AllPossibleMeals(pro, carb, fat, veg, fruit, ex):
  allmeals = []
  for a in pro:
      for b in carb:
          for c in fat:
              for d in veg:
                  for e in fruit:
                      for f in ex:
                          meals = [a, b, c, d, e, f]
                          allmeals.append(meals)
  return allmeals

#lab2_5.3: 아래와 같은 결과 나오게 하기. parameter 고민. +docstring&test
def MealInfo(mymeal, myamounts, kcaldic, gProdic, gFatdic, gCarbdic):
  template1 = '- {0:5.0f} g of {1:>20}, contributing {2:5.0f} kcal, {3:5.1f} g protein, {4:5.1f} g carb, {5:5.1f} g fat'
  template2 = 'TOTAL:' + ' '*42 + '{0:5.0f} kcal, {1:5.1f} g protein, {2:5.1f} g carb, {3:5.1f} g fat'
  print("The meal is composed of : ")
  print("-"*105)
  sum_kcal = 0
  sum_pro = 0
  sum_carb = 0
  sum_fat = 0
  for a, b in enumerate(mymeal):       #enumerate - iterable 객체와 번호를 인자로 전달받아 전달받은 번호를 전달받은 iterable 한 객체의 첫 번째 요소부터 번호를 매기는 함수: enumerate(iterable객체, 번호)
    kcal = myamounts[a] * kcaldic[b]   #a=번호, b=객체의 요소
    sum_kcal += kcal
    gPro = myamounts[a] * gProdic[b]   #각 음식의 양*음식의 성분(탄단지 등)
    sum_pro += gPro                    #한 끼에 먹는 모든 음식성분의 합
    gFat = myamounts[a] * gFatdic[b]
    sum_fat += gFat
    gCarb = myamounts[a] * gCarbdic[b]
    sum_carb += gCarb
    print(template1.format(1000*myamounts[a], b, kcal, gPro, gFat, gCarb))
  print("-"*105)
  print(template2.format(sum_kcal, sum_pro, sum_fat, sum_carb))
  
#lab2_7.1: serving size 물어보기
def AskServingSize(Extras):
  ServingSizeDic = {}   #list는 instr/slices만 받을 수 있음. 따라서, dictionary로 만들어주어야함.
  for i in Extras:
    ServingSizeDic[i] = float(input("What is your serving size for " + i + "(in L of kg)?"))  
  return ServingSizeDic

#lab2_7.2: Unit test - 영양소 고루 먹을 수 있게 각 meal에서 음식의 quatity 도출.
def computeQuantitities(mymeal, requireenergy, gProdic, gFatdic, gCarbdic, exquantities):
  mypro = mymeal[0]
  mycarb = mymeal[1]
  myfat = mymeal[2]
  myveg = mymeal[3]
  myfruit = mymeal[4]
  myextra = mymeal[5]

  # A meal should contain 125g of vegetable
  vegetable_qty = 0.125
  prot_from_vegetable = vegetable_qty*gProdic[myveg]
  fat_from_vegetable = vegetable_qty*gFatdic[myveg]
  carb_from_vegetable = vegetable_qty*gCarbdic[myveg]
  
  # A meal should contain 50g of fruit
  fruit_qty = 0.050
  prot_from_fruit = fruit_qty*gProdic[myfruit]
  fat_from_fruit = fruit_qty*gFatdic[myfruit]
  carb_from_fruit = fruit_qty*gCarbdic[myfruit]

  # extra: constant, predefined quantity (a typical serving size must be associated to each extra before calling the function, eg. 0.008 kg of coffee beans for a single espresso) 
  extra_qty = exquantities[myextra] 
  prot_from_extra = extra_qty*gProdic[myextra]
  fat_from_extra = extra_qty*gFatdic[myextra]
  carb_from_extra = extra_qty*gCarbdic[myextra]

  # 12% of meal kcal should come from proteins, and 1g of protein brings 4 kcal
  # 66% of meal kcal should come from carbs, and 1g of carb brings 4 kcal
  # 22% of meal kcal should come from fat, and 1g of fat brings 8.8 kcal
  # 4*(prot_from_prot_source + prot_from_carb_source + prot_from_fat_source + prot_from_vegetable + prot_from_fruit + prot_from_extra) = 0.12*MealKcalTarget
  # 4*(carb_from_prot_source + carb_from_carb_source + carb_from_fat_source + carb_from_vegetable + carb_from_fruit + carb_from_extra) = 0.63*MealKcalTarget
  # 8.8*(fat_from_prot_source + fat_from_carb_source + fat_from_fat_source + fat_from_vegetable + fat_from_fruit + fat_from_extra) = 0.25*MealKcalTarget

  a = np.array([ [ 4*gProdic[mypro], 4*gProdic[mycarb], 4*gProdic[myfat] ],                              #q(양)은 변수 x이기에 제외하고 생각, a = 6번 정답의 마지막 3개 방정식에서 좌변
                 [ 4*gCarbdic[mypro], 4*gCarbdic[mycarb], 4*gCarbdic[myfat] ],
                 [ 8.8*gFatdic[mypro], 8.8*gFatdic[mycarb], 8.8*gFatdic[myfat] ] ])
  b = np.array([ 0.12*requireenergy - 4*prot_from_vegetable - 4*prot_from_fruit - 4*prot_from_extra,      #상수값, b = 6번 정답의 마지막 3개 방정식에서 우변
                 0.66*requireenergy - 4*carb_from_vegetable - 4*carb_from_fruit - 4*carb_from_extra,
                 0.22*requireenergy - 8.8*fat_from_vegetable - 8.8*fat_from_fruit - 8.8*fat_from_extra])
  x = np.linalg.solve(a, b)                                                                               #x는 우리가 구하고자 하는 q(양). x 계산하기 위해서, numpy 필요함!(import numpy)

  return [x[0], x[1], x[2], vegetable_qty, fruit_qty, extra_qty]                                          #x[0]=pro양, x[1]=carb양, x[2]=fat양



    

if __name__ == "__main__":

  carb = ['Wheat & Rye (Bread)', 'Maize (Meal)', 'Potatoes']
  ex = ['Beet Sugar', 'Coffee', 'Dark Chocolate']
  fat = ['Rapeseed Oil', 'Olive Oil']
  fruit = ['Bananas', 'Apples', 'Berries & Grapes']
  pro = ['Tofu', 'Bovine Meat (beef herd)', 'Poultry Meat', 'Eggs']
  veg = ['Tomatoes', 'Root Vegetables', 'Other Vegetables']

  allmeals = AllPossibleMeals(pro, carb, fat, veg, fruit, ex)
  print("There are ", len(allmeals), "possible meals.")
  print("The first meal is ", allmeals[0])
  print("The last meal is ", allmeals[-1])
  print(len(allmeals)==len(pro)*len(carb)*len(fat)*len(veg)*len(fruit)*len(ex))
  print('')
  
  #lab2_5.1: main에 음식 칼로리에 관련된 dictionary 만드는 명령 추가
  kcal_dic = {'Wheat & Rye (Bread)': 2490, 
                  'Maize (Meal)': 3630,
                  'Potatoes': 670,
                  'Beet Sugar': 3870,
                  'Coffee': 560,
                  'Dark Chocolate': 3930,
                  'Rapeseed Oil': 8096,
                  'Olive Oil': 8096, 
                  'Bananas': 600,
                  'Apples': 480,
                  'Berries & Grapes': 530,
                  'Tofu': 765, 
                  'Bovine Meat (beef herd)': 1500, 
                  'Poultry Meat': 1220, 
                  'Eggs': 1630,
                  'Tomatoes' : 170,
                  'Root Vegetables': 380,
                  'Other Vegetables': 220}

  #lab2_5.2: 각 음식의 proteins, fat, carbohydrates 그램 도출
  gPro_dic = {'Wheat & Rye (Bread)': 82, 
                  'Maize (Meal)': 84,
                  'Potatoes': 16,
                  'Beet Sugar': 0,
                  'Coffee': 80,
                  'Dark Chocolate': 42,
                  'Rapeseed Oil': 0,
                  'Olive Oil': 0, 
                  'Bananas': 7,
                  'Apples': 1,
                  'Berries & Grapes': 5,
                  'Tofu': 82, 
                  'Bovine Meat (beef herd)': 185, 
                  'Poultry Meat': 123, 
                  'Eggs': 113,
                  'Tomatoes' : 8,
                  'Root Vegetables': 9,
                  'Other Vegetables': 14}

  gFat_dic = {'Wheat & Rye (Bread)': 12, 
                  'Maize (Meal)': 12,
                  'Potatoes': 1,
                  'Beet Sugar': 0,
                  'Coffee': 0,
                  'Dark Chocolate': 357,
                  'Rapeseed Oil': 920,
                  'Olive Oil': 920, 
                  'Bananas': 3,
                  'Apples': 3,
                  'Berries & Grapes': 4,
                  'Tofu': 42, 
                  'Bovine Meat (beef herd)': 79, 
                  'Poultry Meat': 77, 
                  'Eggs': 121,
                  'Tomatoes' : 2,
                  'Root Vegetables': 2,
                  'Other Vegetables': 2}

  gCarb_dic = {'Wheat & Rye (Bread)': 514.1, 
                  'Maize (Meal)': 797.1,
                  'Potatoes': 149.3,
                  'Beet Sugar': 967.5,
                  'Coffee': 60,
                  'Dark Chocolate': 155.1,
                  'Rapeseed Oil': 0,
                  'Olive Oil': 0, 
                  'Bananas': 136.4,
                  'Apples': 112.4,
                  'Berries & Grapes': 118.7,
                  'Tofu': 16.85, 
                  'Bovine Meat (beef herd)': 16.2, 
                  'Poultry Meat': 12.6, 
                  'Eggs': 28.3,
                  'Tomatoes' : 30.1,
                  'Root Vegetables': 81.6,
                  'Other Vegetables': 36.6}
  
  print("One example of the nutrition in each meal: ")
  Meals = ['Poultry Meat', 'Wheat & Rye (Bread)', 'Olive Oil', 'Root Vegetables', 'Berries & Grapes', 'Coffee']
  Amounts = [0.05, 0.12, 0.016, 0.125, 0.05, 0.008]
  MealInfo(Meals, Amounts, kcal_dic, gPro_dic, gCarb_dic, gFat_dic)

  print("Asking typical serving size: ")
  AskServingSize(ex)
  
  print("Unit test of computesQuantities")
  example_extra_quatities = {'Beet Sugar': 0.012, 'Coffee': 0.008, 'Dark Chocolate': 0.020}
  computeQuantitities(Meals, 1800, gPro_dic, gCarb_dic, gFat_dic, example_extra_quatities)      #2nd parameter - my daily energy requirement exmaple = 1800kcal