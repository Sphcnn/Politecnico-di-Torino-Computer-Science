''' 1
numbers = input("Enter a line of numbers :")
numList = []
for num in numbers.split(" "):
    try:
        numList.append(int(num))
    except ValueError:
        pass
calculation = 1
print(numList)
sumtotal = 0
for num in numList:
    if calculation == 1:
        sumtotal = sumtotal + num
        calculation = 1 - calculation
    else:  
        sumtotal = sumtotal - num
        calculation = 1 - calculation

print(sumtotal)
'''
''' 2
import random
numList = []

for i in range(10):
    numList.append(random.randint(1,100))

evenList = []
equalList = []
reverseList = []
reverseList2 = []
orderList = []
counter = 0
for i in range(10):
    if i % 2 == 0:
        evenList.append(numList[i])
    else: pass
    
    reverseList.append(numList[len(numList)-i-1]) 
    reverseList2 = sorted(numList, reverse = True)
for x in numList:
    if numList.count(x) > 1 and x not in equalList:
        equalList.append(x)

orderList.append(numList[len(numList)-len(numList)])
orderList.append(numList[len(numList)-1])

print(f'{numList} \n {evenList} \n {equalList} \n {reverseList} \t {reverseList2} \n {orderList}')
'''

numlist = []
length = int(input("Enter how many element will you add into list ? "))

for i in range(length):
    numlist.append(int(input("Enter a number : ")))

prev = numlist[0]      
min_index = 0          

for i in range(1, len(numlist)):
    if numlist[i] < prev:   
        prev = numlist[i]
        min_index = i

print(f'Your list was : {numlist}')
print(f'The minimum value of your list was {prev}\n')

lastList = []
for i in range(len(numlist)):
    if i != min_index:          
        lastList.append(numlist[i])

print(f'Your list became that list after removing the minimum value from your list {lastList}')
