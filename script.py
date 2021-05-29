mystring = None
myfloat = None
myint = None

if mystring == "hello":
    print("String: {0} {1}".format(mystring, type(mystring)))
elif(isinstance(myfloat, float)):
    print("Float: {0}".format(myfloat))
elif(isinstance(myint, (str, int))):
    print("None or Int {0}". format(myint))
else:
    print("None in above")
