#1:While loops
#2: For loops


# While loop
# 1.
# x=0
# while(x<5):
#     print(x)
#     x=x+1


#For Loop
#1
# for x in range(50,100):
    # print(x)

#2
#array
days=["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
for a in days:
    # if (a=="Fri"):break #It break the loop from Fri-Sun
    if (a=="Fri"):continue #It skip the Friday.
    print(a)

