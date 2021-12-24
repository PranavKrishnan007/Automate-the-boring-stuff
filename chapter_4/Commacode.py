def myfunc(a):
    if len(a) > 0:
        mystr = a[0]
        for x in range(1,len(a)) :
            mystr = mystr + ", " + a[x]
        print(mystr)
    else:
        print("There is nothing in the string!")

var = list(input().split())
myfunc(var)
