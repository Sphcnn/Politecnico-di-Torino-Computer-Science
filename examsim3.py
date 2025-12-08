def main():
    processNumber = int(input("Enter the process number : "))
    borrowed = []
    returned = []
    print("DATA ENTERANCE TYPE : process/username/bookname")
    for i in range(processNumber):
        sentence = input("Type your process (BORROW/RETURN):")
        sentence = sentence.split()
        if sentence[0].upper() == "BORROW": borrowed.append(sentence[1:])
        elif sentence[0].upper() == "RETURN": returned.append(sentence[1:])
        else: print("Invalid operation !")
    print(borrowed)
    print(returned)    
    borrowed, returned = compare(borrowed, returned)
    print(borrowed)
    print(returned)
    print(f'{"UserName :":<15}:\t {"Borrowed Books :":<15}')
    write(borrowed)

def compare(list1:list, list2:list):
    common = []
    for element1 in list1:
        for element2 in list2:
            if element1 == element2: common.append(element1)
            else: continue 
    for element in common:
        if element in list1: list1.remove(element)
        if element in list2: list2.remove(element)
    return list1, list2

def write(list1:list):
    borrowers = []
    tempDict = {}
    returnDict = {}
    for i in range(len(list1)):
        if list1[i][0] not in borrowers: borrowers.append(list1[i][0])
        else: continue

    for name in borrowers:
        bookList = []
        for i in range(len(list1)):
            if name == list1[i][0]: bookList.append(list1[i][1]) 
            else: continue
        tempDict = {f'{name}':f'{bookList}'}
        returnDict.update(tempDict)
    
    for key, value in returnDict.items():
        temp = "".join(value)
        print(f'{key:<15}:\t {temp:<15}')
    
    bookNum = []
    for i,name in enumerate(borrowers):
        bookNum.append(len(returnDict[name]))
    total = 0
    for num in bookNum:
        total = total + num    

    print(f'\n{"Number of borrowed books:":<15}\t {total:<15}')
    index = bookNum.index(max(bookNum))
    favBorrower = borrowers[index]
    print(f'\n{"Most active borrower :":<15}\t {favBorrower}')

main()