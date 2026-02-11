a = 3300
b = 200
'''if b > a:#syntax:if (conditional statement)
  print("b is greater than a")
'''
if b<a:
  print("good")
elif a == b:
  print("bad")
elif a > b :
  print("goodbad")
  #elif is used when there are multiple conditions

  #if there is only one statement we can use juat if statement
  #short end if..else.. statements
age=6
print("older")if age>10 else print("younger")

#when we have values syntax(variable = value_if_true if condition else value_if_false)
bigger=a if a>b else b
print("bigger value is ",bigger)


#logical operators
c=450
if a>b and b>c:
  print("both th conditions are true")