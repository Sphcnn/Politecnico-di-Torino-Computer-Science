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
"""   Buna tekrar bak 6
import random

def main ():
    table = createTable()
    print("Your table is : ")
    for line in table:
        print(line)
        print()
    neighbourhood(table)


def createTable():
    row = int(input("Enter the width of your table : "))
    column = int(input("Enter the height of your table :"))
    table = []
    for i in range(column):
        line = [0]*row
        table.append(line)

    for i in range(len(table)):
        for j in range(len(table[i])):
             table[i][j] = random.randint(1,100)
    
    return table

def neighbourhood(numTable):
    numNeighbour = []
    avgNeighbour = []
    total = 0
    avg = 0
    bound1 = len(numTable)
    bound2 = len(numTable[0])
    


main()"""
''' 7 Tekrar bak
THEATER_PLAN = [
    [10,10,10,10,10,10,10,10,10,10],
    [10,10,10,10,10,10,10,10,10,10],
    [10,10,10,10,10,10,10,10,10,10],
    [10,10,20,20,20,20,20,20,10,10],
    [10,10,20,20,20,20,20,20,10,10],
    [10,10,20,20,20,20,20,20,10,10],
    [20,20,30,30,40,40,30,30,20,20],
    [20,30,30,40,50,50,40,30,30,20],
    [30,40,50,50,50,50,50,50,40,30]
]

LETTERS = ["A","B","C","D","E","F","G","H","I","J"]
NUMBERS = [1,2,3,4,5,6,7,8,9,10]


def print_plan(table):
    print(NUMBERS)
    print("-" * 50)
    for i, row in enumerate(table):
        print(f"{LETTERS[i]} | {row}")
    print()


def main():
    # Orijinal planı kopyalayalım ki üstünde çalışalım
    table = [row[:] for row in THEATER_PLAN]

    bought_tickets = []  # (seat_str, price) tuple'ları burada tutulacak

    while True:
        print_plan(table)
        print(f'You can select among rows {LETTERS[:len(table)]} and seats {NUMBERS}')
        choice = input(
            'Would you like to see the available seats by price or choose ticket directly?\n'
            'Type "see" to filter by price,\n'
            'Type "select" to choose a seat,\n'
            'Type "quit" to finish and print receipt.\n'
            'Your choice: '
        ).strip().lower()

        if choice == "quit":
            break

        if choice == "see":
            # Fiyatına göre koltukları gösterme
            try:
                price = int(input("What price do you want to pay for a ticket? "))
            except ValueError:
                print("Invalid price.\n")
                continue

            # Fiyat filtresi için geçici tablo
            price_table = []
            for row in table:
                new_row = []
                for seat_price in row:
                    if seat_price == price:
                        new_row.append(seat_price)
                    else:
                        new_row.append("X")
                price_table.append(new_row)

            print("You can choose among these seats:\n")
            print(NUMBERS)
            print("-" * 50)
            for i, row in enumerate(price_table):
                print(f"{LETTERS[i]} | {row}")
            print()

            ticket = input("Enter the seat location (e.g. D5) or 'cancel' to go back: ").strip()
            if ticket.lower() == "cancel":
                continue

            if not ticket:
                print("Empty input.\n")
                continue

            ticket_row = ticket[0].upper()
            try:
                ticket_column = int(ticket[1:])
            except ValueError:
                print("Invalid seat format.\n")
                continue

            if ticket_row in LETTERS[:len(table)] and 1 <= ticket_column <= 10:
                i = LETTERS.index(ticket_row)
                j = ticket_column - 1

                if table[i][j] == "X":
                    print("This seat is already sold.\n")
                elif price_table[i][j] == "X":
                    print("This seat is not available for the selected price.\n")
                else:
                    price_paid = table[i][j]
                    table[i][j] = "X"
                    bought_tickets.append((ticket_row + str(ticket_column), price_paid))
                    print(f'You bought {ticket_row}{ticket_column} for {price_paid}€.\n')
            else:
                print("Invalid seat.\n")

        elif choice == "select":
            ticket = input("Enter the seat location (e.g. D5): ").strip()
            if not ticket:
                print("Empty input.\n")
                continue

            ticket_row = ticket[0].upper()
            try:
                ticket_column = int(ticket[1:])
            except ValueError:
                print("Invalid seat format.\n")
                continue

            if ticket_row in LETTERS[:len(table)] and 1 <= ticket_column <= 10:
                i = LETTERS.index(ticket_row)
                j = ticket_column - 1

                if table[i][j] == "X":
                    print("This seat is already sold.\n")
                else:
                    price_paid = table[i][j]
                    table[i][j] = "X"
                    bought_tickets.append((ticket_row + str(ticket_column), price_paid))
                    print(f'You bought {ticket_row}{ticket_column} for {price_paid}€.\n')
            else:
                print("Invalid seat.\n")
        else:
            print("Unknown choice.\n")

    # Fiş kısmı
    print("\n" + "=" * 50)
    print("RECEIPT")
    print("=" * 50)
    if not bought_tickets:
        print("You did not buy any tickets.")
    else:
        total = 0
        for seat_str, price in bought_tickets:
            print(f"Seat {seat_str}: {price}€")
            total += price
        print("-" * 30)
        print(f"Total: {total}€")
    print("=" * 50)

main()
'''

''' Do not execute this code if you like your computer I was curious about whether I can find magic square but I could not due to lack of ram. My computer was about to crush.
import random

def main():
    tableSize = int(input("Enter the size of your table : "))
    emptyTable = createTable(tableSize)
    printTable(emptyTable)
    filledTable = fulfill(emptyTable,tableSize)
    numberofTry = 0

    if checker(filledTable,tableSize): print("Your matrix is a magic square"); print(f'Number of try : {numberofTry}')
    else: 
        statement = checker(filledTable,tableSize)
        while statement != True:
            try:
                filledTable = fulfill(emptyTable,tableSize)
                print("-"*10)
                printTable(filledTable)
                statement = checker(filledTable,tableSize)
                numberofTry += 1
                print(f'Number of try : {numberofTry}')
                if numberofTry > 10000:
                    print("I can not find the magic square version of your table")
                    statement = True
                else:pass
            except KeyboardInterrupt:
                print("I was about to find magic square version. You were not brave enough to find it ")
                statement = True
            finally:
                print("Programme was ended by user ! ")

def printTable(table):
    for line in table:
        print(line)
        print()

def createTable(n):
    table = []
    for i in range(n):
        line = [0]*n
        table.append(line)
    return table

def fulfill(table,n):
    numList = []
    lowBound = 1
    upBound = n*n
    for number in range(upBound):
        numList.append(lowBound)
        lowBound += 1
    
    for i in range(len(table)):
        for j in range(len(table[i])):
            print(numList)
            num = random.choice(numList)
            table[i][j] = num
            numList.remove(num)
            

    return table

def checker(table,n):
    sumListRow = []
    sumListColumn = []
    sumListDiagonal1 = []
    sumListDiagonal2 = []
    total = 0
    #sum of elements in row
    for i in range(len(table)):
        for j in range(len(table[i])):
            total = total + table[i][j]
            sumListRow.append(total)
        total = 0
    #sum of elements in column
    for j in range(len(table)):
        for i in range(len(table[i])):
            total = total + table[i][j]
            sumListColumn.append(total)
        total = 0
    #sum of diagonal 1
    i,j = 0,0
    while i <= n-1 and j <= n-1 :
        total = total + table[i][j]
        sumListDiagonal1.append(total)
        i += 1
        j += 1
    
    i = n-1
    j = 0

    while i >= 0 and j <= n-1 :
        total = total + table[i][j]
        sumListDiagonal2.append(total)
        i -= 1
        j += 1

    if set(sumListColumn) == set(sumListRow) == set(sumListDiagonal1) == set(sumListDiagonal2):
        return True

    else: return False          

main()
'''