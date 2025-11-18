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
''' 3
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
'''
'''  4
numList = []
statement = True

while statement:
    number = input("Enter a number (empty line to quit): ")
    if number != "":
        numList.append(int(number))
    else:
        statement = False


if len(numList) < 3:
    print("There are no local maxima")
else:
    localMaxPos = []   
    for i in range(1, len(numList) - 1):
        if numList[i-1] < numList[i] and numList[i] > numList[i+1]:
            localMaxPos.append(i)
    if not localMaxPos:
        print("There are no local maxima")
    else:
        print("Local maxima positions:", localMaxPos)
        print("Values at those positions:", [numList[i] for i in localMaxPos])

        if len(localMaxPos) >= 2:
            min_dist = None
            best_pair = None

            for k in range(len(localMaxPos) - 1):
                d = localMaxPos[k+1] - localMaxPos[k]
                if min_dist is None or d < min_dist:
                    min_dist = d
                    best_pair = (localMaxPos[k], localMaxPos[k+1])

            print(f"The closest two local maxima are at positions {best_pair[0]} and {best_pair[1]}")
            print(f"Their values are {numList[best_pair[0]]} and {numList[best_pair[1]]}")
        else:
            print("There is only one local maximum, so there is no pair to compare.")
'''
''' 5
def read_list(which):
    """Kullanıcıdan bir liste okur (boş satır veya non-digit ile bitirir)."""
    nums = []
    print(f"Enter numbers for {which} list (empty line to stop):")
    while True:
        s = input()
        if s == "":
            break
        if s.lstrip("-").isdigit():   # negatif sayıları da kabul et
            nums.append(int(s))
        else:
            print("Not a valid integer, stopping input for this list.")
            break
    return nums


def unique_list(lst):
    """Bir listedeki tekrar edenleri atıp benzersiz elemanlardan oluşan liste döndürür."""
    result = []
    for x in lst:
        if x not in result:
            result.append(x)
    return result


def same_elements(list1, list2):
    """
    İki listenin, sıra ve tekrar sayısı önemsiz şekilde
    aynı elemanlara sahip olup olmadığını kontrol eder.
    True / False döner.
    """
    u1 = unique_list(list1)
    u2 = unique_list(list2)

    u1.sort()
    u2.sort()

    return u1 == u2, u1, u2   # bool + işlenmiş halleri geri döndürüyoruz


def non_equivalent_elements(list1, list2):
    """İki listenin eşsiz elemanları arasındaki farkları (sadece birinde olanlar) döndürür."""
    u1 = unique_list(list1)
    u2 = unique_list(list2)

    diff = []

    for x in u1:
        if x not in u2:
            diff.append(x)

    for x in u2:
        if x not in u1:
            diff.append(x)

    return diff


def main():
    # 1) Listeleri oku
    list1 = read_list("FIRST")
    list2 = read_list("SECOND")

    print(f"\nList1: {list1}")
    print(f"List2: {list2}")

    # 2) Eşdeğer mi kontrol et
    are_same, u1, u2 = same_elements(list1, list2)

    print(f"Unique of List1: {u1}")
    print(f"Unique of List2: {u2}")

    if are_same:
        print("Both lists have same elements (ignoring order and duplicates).")
    else:
        print("Lists are NOT equivalent.")
        diff = non_equivalent_elements(list1, list2)
        print(f"Non-equivalent elements : {diff}")

# Programı çalıştır
main()
'''
''' 6
import random
numbers = []
for num in range(20):
    numbers.append(random.randint(1,99))
print(f'{numbers} is our list \n It is sorted as {sorted(numbers)} \n Sorted from back to up {sorted(numbers, reverse = True)}')
'''

''' 7
numList = []
statement = True

while statement:
    number = input("Enter a number : ")
    if number.isdigit():
        numList.append(int(number))
    else:
        statement = False
numList.sort()
sum = 0
for i in range(1,len(numList)):
    sum = sum + numList[i]
print(f'Sum of the all elements of list : {sum}')
'''
''' 8
list1 = []
statement = True

while statement:
    number = input("Enter the experiment values (Press q for quit):")
    if number.lower() == "q":
        statement = False
    else:
        list1.append(float(number))

print(list1)

for i,element in enumerate(list1):
    if i == 0: 
        list1[i] = (list1[i]+list1[i+1])/2
    elif i == len(list1)-1:
        list1[i] = (list1[i]+list1[i-1])/2
    
    else:
        list1[i] = (list1[i-1]+list1[i]+list1[i+1])/3

for i in range(len(list1)):
    print(f'{i}. element of the list is {list1[i]}')
'''

# başlangıç
length = int(input("Kaç park yeri var? "))

# False = boş, True = dolu
row = [False] * length

def print_row():
    for slot in row:
        print("X" if slot else "_", end=" ")
    print()

print_row()

car_number = int(input("Kaç araba gelecek? "))

for car in range(car_number):

    # --- En uzun boş aralığı bul ---
    longest_start = 0
    longest_len = 0

    i = 0
    while i < length:
        if not row[i]:                 # boş yer buldu
            start = i
            while i < length and not row[i]:
                i += 1
            segment_length = i - start

            if segment_length > longest_len:
                longest_len = segment_length
                longest_start = start
        else:
            i += 1

    # Ortaya park et
    place = longest_start + longest_len // 2
    row[place] = True

    print_row()

    
                    
