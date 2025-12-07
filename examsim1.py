#22:17
def main():
    receipt = []
    try: 
        infile = open("transaction.txt","r")
        for line in infile:
            line = line.rstrip()
            receipt.append(line.split(" "))
    except IOError as e: print(f"Reading process has been canceled because of {e}")
    finally:
        if infile is not None: infile.close()
        if receipt: print("Operation has been done succesfuly")
        else: print("Operation has not been done succesfuly")

    id = int(input("Enter customer ID :"))
    summarize(id,receipt)
    
def summarize(id:int,receipt:list):
    check = 0
    for i in range(len(receipt)):
        if int(receipt[i][0]) == id: check = 1
    if check == 0: print("Your ID is invalid")
    else:
        productList = []
        qualityList = []
        priceList = []
        for i in range(len(receipt)):
            if int(receipt[i][0]) == id:
                productList.append((receipt[i][1]))
                qualityList.append((receipt[i][2]))
                priceList.append((receipt[i][3]))
        
        numOfDistinctProducts = len(set(productList))
        totalPrice = 0
        for i in range(len(priceList)):
            totalPrice += (float(priceList[i]) * int(qualityList[i]))

        print(f"Customer ID: {id} ")
        print(f"{'ID':<3}\t {'Product ':<10}\t {'Quality ':<10}\t {'Price ':<10}\t")
        biggestPrice = float(priceList[0])
        for i,element in enumerate(priceList):
            if float(element) > biggestPrice : biggestPrice = element
            else: continue 
        mostEx = productList[priceList.index(biggestPrice)]
        
        print("-"*50)
        for i in range(len(productList)):
            print(f"{i+1:<3}\t {productList[i]:<10}\t {qualityList[i]:<10}\t {priceList[i]:<10}\t")
        print("-"*50)
        print(f"Number of distinct products purchased: {numOfDistinctProducts}")                     
        print(f"Total price: {totalPrice}")
        print(f"Most expensice product(by unit): {mostEx}")

main()