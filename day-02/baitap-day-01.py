'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    THAM KHAO:  https://wiki.python.org/moin/HowTo/Sorting
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


'''
    SAP XEP MANG TANG DAN
'''
print "\nSap xep mang tang dan"
myList = [9, 5, 10, 100, 0, -10, 3.5, -2.001, 33.33]

# Sort myList then return new list
sortedList = sorted(myList)

print "\nmyList: ", myList
print "sortList: ", sortedList

# Sort myList ifself
myList.sort()
print "\nmyList: ", myList
print "myList.sort() return: ", myList.sort()

'''
    SAP XEP MANG GIAM DAN
'''
print "\nSap xep mang giam dan"
myList = [9, 5, 10, 100, 0, -10, 3.5, -2.001, 33.33, 9]
sortedList = sorted(myList, reverse=True)
print sortedList, "\n"



