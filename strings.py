#string can be represented in single ,double,triple quotes
name='bharat'
name2="bharat"
name="""bharat"""

'''string slicing
syntax for string slicing is sl=name[ind_start:ind_end],even negative indexing can be used
    ex:sl[3:5]'''
a="   bharath ,reddy  "
print(a[:5])#from starting
print(a[2:])
b=a[1:5]
print(b)

'''
Python has some built-in functions which could be used '''
#upper()
print(a.upper())
#lower()
print(a.lower())
#strip()
#here it removes the white spaces at the atarting and end of the string
print(a)#here it returns "bharath"
#replace()
print(a.replace("h","e"))
#split()
print(a.split(","))

"""concatinate strings"""

c="bharath"
d="reddy"
e=c+d#combining strings
print(e)
f=c+" "+d#adding space
print(f)


"""FORMAT STRINGS"""
#earlier it was difficult to add strings and numbers ,to specify f-strings we can use "f"infront of string literaland add curly brackets{}
#place holder can contain variables,functions,operationsand modifiers
age=21
txt=f"I am bharath,and i am {age}years old"
print(txt)
xtx=f"price of carrot is{56*80}"
print(xtx)

