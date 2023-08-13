# Conditional or logical operators
#Logical operators are either "True & False","Yes & No","0 & 1".


# equal to                              ==
# not equal to                          !=
# less than                             <
# greater than                          >
# less than equal to                    <=
# greater than equal to                 >=

#Equal to ==
# I know 4 is equal to 4 But how python So
print(4==4)
print(4==9) #The answer is false
print(5==2) #The answer is false

#NotEqual to !=
# I know 5 is not equal to 10
print(5!=10)#True
print(5!=1)#True
print(5!=0)#True
print(5!=5)#False

#less than <
# I know 3<4 mean 3 is smaller to 4 which is true
print(3<4)#True
print(9<100)#True
print(100<100)#False
print(96<2)#False

#Greater than >
# I know 4>3 4 is greater to 3 which is true
print(4>3)#True
print(100>105)#False
print(96>45)#True
print(2>3)#False

#Less than equal to <=
# I know that 4 <= 5 mean 4 less than equal to 5 which is true
print(4<=5)#True
print(5<=4)#False
print(100<=90)#False
print(90<=100)#True
print(5<=5)#True

#Greater than equal to >=
# I know that 100=>90 which is true
print(100>=90)#True
print(2022>=2021)#True
print(2000>=2001)#False
print(1947>=2000)#False

#input function and logical operators
# Dawood_age=6
# age_at_school=6
# print(Dawood_age==age_at_school)
#Dawood cannot take addmission in school because he is too yonger

#Can Huzaifa take addmission in school
age_at_school=7
Huzaifa_age=input("How old are you Huzaifa? ")
# print("You are "+Huzaifa_age+" years old")
print("You are "str+(Huzaifa_age)+" years old")
print(type(Huzaifa_age))
