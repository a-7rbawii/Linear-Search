def linearSearch(item, myList):
    found = -1
    for i in range(0, len(myList)):
        if myList[i] == item:
            found = i
    return found

myList = [99, 5, -11, 0]
item = int(input("Item to be searched:\n"))

result = linearSearch(item, myList)

if result < 0:
    print("Item NOT found")
else:
    print("Item has been found at index {}".format(result))