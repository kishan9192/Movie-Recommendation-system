text = ["London Paris London", "Paris Paris London"]
#arr = []

mydict = {}
for i in text:
    arr = i.split(" ")
    for n in arr:
        if n in mydict:
            mydict[n] += 1
        else:
            mydict[n] = 1
    print(mydict)
    mydict.clear()
    
#print(arr)
#print(mydict)


