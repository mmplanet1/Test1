#!"c:\python34\python.exe"
#title           :test1.py
# -*- coding: UTF-8 -*-

# enable debugging
import cgitb
#cgitb.enable()

from itertools import chain

print("Content-Type: text/html;charset=utf-8")
print()

iter1 = iter([1, 2, 3, 5, 6, 6, 8, 9])
iter2 = iter([2, 4, 6, 7])

iter5 = iter([4666, 332, 333333333, 12, 999999, 88])
iter6 = iter([980, 420, 568, 870, 738])

def list1Gen(item1):
    for item in item1:
        yield int(item)
#parsing each item from iter

def orderedIterators(list1, list2):
	sortedList = sorted(chain(list1Gen(list1), list1Gen(list2)))
	yield sortedList
#combining two given iters


orderedIterators12 = list(orderedIterators(iter1, iter2))
orderedList = list(chain.from_iterable(orderedIterators12))
print("<p>Ordered list for iter1, iter2 is: ")
print (orderedList)
print("</p>")
#writing log now
log = open("log.txt", "a")
line = log.writelines("Ordered list for iter1, iter2 is: " + str(orderedList) + "\n")
log.close()
#end of writing log

print("\n")


orderedIterators56 = list(orderedIterators(iter5, iter6))
orderedList = list(chain.from_iterable(orderedIterators56))
print("<p>Ordered list for iter5, iter6 is: ")
print (orderedList)
print("</p>")
log = open("log.txt", "a")
line = log.writelines("Ordered list for iter5, iter6 is: " + str(orderedList) + "\n")
log.close()
