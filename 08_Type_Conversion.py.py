x=9         #Integer or int
y=9.5       #Floating
z="Hello"   #string or str


#implicit type of conversion
x=x*y
print(x,type(x))
#after to it you can run line 5 to increase the answer
print(x,"Type of x is:",type(x))

print(type(z))
print("Type of z is:",type(z))

#explicit type of conversion
age=input("What is your age? ")
# print(type(age)) It give me age in str because I don't use int function.
#There are two ways of int function to run in code
# print(type(int(age)))
# The next line show the age with the int function
# print(age,type(float(age))) for float
print(age,type(int(age)))  #for int
# age=int(age)

#name
name=input("What is your name? ")
print(name,type(str(name)))