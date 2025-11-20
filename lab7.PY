#Exercises of Lab 7
''' 1
def main():
    list1 = []
    list2 = []
    list1 = getList("List1")
    list2 = getList("list2")
    print(list1)
    print(list2)
    list3 = mergeList(list1,list2)
    print(list3)

def getList(name) :
    statement = True
    elementList = []
    while statement:
        element = input(f"Enter a value to add to {name}. Press q to quit : ")
        if element.lower() == "q": 
            statement = False
        else:
            elementList.append(int(element))
    return elementList

def mergeList(list1,list2):
    mergedList = []
    if len(list1) > len(list2):
        for i in range(len(list2)):
            mergedList.append(list1[i])
            mergedList.append(list2[i])
        for i in range(len(list2),len(list1)):
           mergedList.append(list1[i]) 
    
    elif len(list1) < len(list2):
        for i in range(len(list1)):
            mergedList.append(list1[i])
            mergedList.append(list2[i])
        for i in range(len(list1),len(list2)):
           mergedList.append(list2[i])

    else:
        for i in range(len(list2)):
            mergedList.append(list1[i])
            mergedList.append(list2[i])
    return mergedList
        
main()
'''
''' 2
def main():
    elements = input('Enter a list of numbers (put ":" between two numbers): ')
    
    intList = [int(x) for x in elements.split(":")]

    maxminList = withoutMaxMin(intList)
    evenNumList = findEven(intList)
    twoDigitList = findTwoDigit(intList)

    original_str = ":".join(str(x) for x in intList)
    maxmin_str = ":".join(str(x) for x in maxminList)
    even_str = ":".join(str(x) for x in evenNumList)
    twodigit_str = ":".join(str(x) for x in twoDigitList)

    print(f'Your list is: {original_str}')
    print(f'Without min and max: {maxmin_str}')
    print(f'Even numbers: {even_str}')
    print(f'Two-digit numbers: {twodigit_str}')

def withoutMaxMin(list):
    withoutMaxMinList = []
    maxList = max(list)
    minList = min(list)
    for number in list:
        if number == maxList or number == minList: pass
        else:
            withoutMaxMinList.append(number)
    return withoutMaxMinList

def findEven(list):
    evenList = []
    for number in list:
        if number % 2 == 0:
            evenList.append(number)
        else: pass
    return evenList

def findTwoDigit(list):
    twodigitList = []
    for number in list:
        if 1 <= number / 10 <10:
            twodigitList.append(number)
        else: pass
    return twodigitList
main()
'''
''' 3
def main():
    table = createTable()
    fill1(table)
    chessScheme(table)
    upperlowerZero(table)
    leftrightOne(table)
    total = sumTable(table)
    print(f'Sum of the all elements of your table is :  {total}')

def createTable():
    column = int(input("Enter the height of your table : "))
    row = int(input("Enter the width of your table : "))
    table = []
    for i in range(column):
        line = [0] * row
        table.append(line)
    print("Your table is : ")
    for row in table:
        print(row)
        print()
    return table

def fill1(table):
    for i in range(len(table)) :
        for j in range(len(table[i])):
            table[i][j] = 1
    print('Your table is based 1 : ')
    for row in table:
        print(row)
        print()
    return 

def chessScheme(table):
    for i in range(len(table)) :
        for j in range(len(table[i])):
            if (i + j) % 2 == 0:
                table[i][j] = 1
            else:
                table[i][j] = 0
    print('Your chess table : ')
    for row in table:
        print(row)
        print()
    return 

def upperlowerZero(table):
    for i in range(len(table)) :
        for j in range(len(table[i])):
            if i == 0 :
                table[i][j] = 0
            elif i == (len(table)-1):
                table[i][j] = 0
            else: pass
            
    print('Your table table which is zero upper and lower : ')
    for row in table:
        print(row)
        print()
    return 

def leftrightOne(table):
    for i in range(len(table)) :
        for j in range(len(table[i])):
            if j == 0 or j == (len(table[i])-1):
                table[i][j] = 1
            else: pass
    print('Your table which is one left and right : ')
    for row in table:
        print(row)
        print
    return 

def sumTable(table):
    total = 0
    for i in range(len(table)) :
        for j in range(len(table[i])):
            total += table[i][j]
    return total
main()
'''

''' 4
def main():
    list1 = getList()
    listOrder(list1)

def getList():
    name = []
    statement = True
    while statement:
        num = input("Insert value. Press q to quit : ")
        if num.lower() == "q":
            statement = False
        else:
            name.append(int(num))
    return name

def listOrder(name):
    order = len(name)
    newList = [""]*order
    for i,element in enumerate(name):
        index = (i+1) % order
        newList[index] = element
    
    print(f'The state of {name} that all elements are carried left is : {newList}')
    
main()
''' 
''' 5
def main():
    list1 = getList("First")
    list2 = getList("Second")
    mergedList = mergeList(list1,list2)
    print(f'Your first list : {list1} \n  Your second list : {list2} \n  The merged and sorted version of your lists : {mergedList}')
def getList(name):
    numList = []
    statement = True
    while statement:
        num = input(f"Enter number into {name} (Press q to quit) : ")
        if num.lower() == "q":
            statement = False
        else:
            numList.append(int(num))
    return numList

def mergeList(numlist1, numlist2):
    mergedList = []
    i = 0
    j = 0


    while i < len(numlist1) and j < len(numlist2):
        if numlist1[i] < numlist2[j]:
            mergedList.append(numlist1[i])
            i += 1
        elif numlist1[i] > numlist2[j]:
            mergedList.append(numlist2[j])
            j += 1
        else:
            mergedList.append(numlist1[i])
            mergedList.append(numlist2[j])
            i += 1
            j += 1

    while i < len(numlist1):
        mergedList.append(numlist1[i])
        i += 1

    while j < len(numlist2):
        mergedList.append(numlist2[j])
        j += 1

    return mergedList
      
main()
'''

list = [1,2,3,4,5]
print(list[7])
