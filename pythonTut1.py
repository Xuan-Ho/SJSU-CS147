


from django.template.defaultfilters import upper, lower

#Print Hello World
print("//Hello Wrld")
print("hellow World")
print()

#Variable
print("//Varaible")
pi = 3.5
name ="Xuan"
age = 25

print(name)
print(age)
print(pi)
print()

#object check
x = 10
print()

#String
print("//String")
name = "Xuan"
print(len(name))

strLen = len(name)
print(strLen)

print(upper(name)) #function from Django lib
print(lower(name)) #need to import lower
title= "your grade is {}".format(79) #concatenation
print(title)
str2="I Love{}".format(" Xuan {}").format("FACE :)") #multi concatenation
print(str2)
print()

#Comment
str3 = "FUCKING   XUAN   IS  A     BITCH"
print(str3.split())