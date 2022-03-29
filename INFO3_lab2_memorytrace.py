#lab2_1.2
from ast import Num


a = 208
b = 210
print("The addrss of variable a = ", a, " is ", id(a))
print("The addrss of variable b = ", b, " is ", id(b))


#lab2_1.3
def add_two_thousands(Number):
    print("The address of Number '", Number, "' is", id(Number))
    print("Assigning 2000 to a variable c:")
    c = 2000
    print("The addrss of variable c = ", c, " is ", id(c))
    
    return Number+c


#lab2_1.4
print("Call the function add_two_thousands with Number = a.", "\n")
add_two_thousands(a)                                    #전역변수 -> 지역변수(def) 넣은 것: 가능


#lab2_1.5
print("Address contained in variable c: ", id(c))       #지역변수 -> 전역변수(def) 넣은 것: 불가능. def에서 정의한 변수를 가져올 수 없음.


#lab2_2
# Program A
a = [1, 2, 3]
b = a                       #b는 a에 의존적. b를 수정하면, a에도 영향을 줌.
b[0] = 2                    # draw the state of memory now ==> drawing #A
print(a)                    # predict the answer [2, 2, 3]
print(b)                    # predict the answer [2, 2, 3]
# Program B
a = [1, 2, 3]
b = a + []                  #b는 a와 다른 새로운 list. b 수정은 a에 영향을 주지 않음.
b[0] = 2                    # draw the state of memory now ==> drawing #B
print(a)                    # predict the answer [1, 2, 3]
print(b)                    # predict the answer [2, 2, 3]
# suggest another way of Program B 
a = [1, 2, 3]
b = a[:]                    # independent copy of a 만드는 다른 방법
b[0] = 2
print(a)
print(b)


#lab2_3
# Program A
def evilGetLength1(ilist):
    length = len(ilist)
    del ilist[0:length]         # ilist의 모든 item 삭제 / ilist에 포함된 reference를 바꾸지 않고, item 배열에 있는 reference를 바꿈. item배열은 mylist object의 items attribute에 의해 참조되기에 main에서 확인할 수 있음.
    return length               # del된 ilist의 길이가 아니라, del되기 전에 길이를 가져왔기에 4

mylist = [12.8, -14.9, 16.6, -3.0]
l = evilGetLength1(mylist)
print(mylist)                   # predict the answer [] -> ilist를 지웠는데, 이걸 가져옴. def에 들어갈때, mylist가 ilist로 들어감.
print(l)                        # predict the answer 4

# Program B
def evilGetLength2(ilist):
    length = len(ilist)
    ilist = []                  # ilist에 포함된 reference 수정은 local이기에 main에 표시 x. def의 인수는 사라지고 main에 전달 x. (ilist를 재정의함.)
    return length               

mylist = [12.8, -14.9, 16.6, -3.0]
l = evilGetLength2(mylist)
print(mylist)                   # predict the answer [12.8, -14.9, 16.6, -3.0]
print(l)                        # predict the answer 4

   
    


