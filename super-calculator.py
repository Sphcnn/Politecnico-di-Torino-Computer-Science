def main():
    content = []
    operations = {
        "+":lambda a,b:a+b,
        "-":lambda a,b:a-b,
        "*":lambda a,b:a*b,
        "/":lambda a,b:a/b
                }
    try:
        infile = open("input.txt","r")
        for line in infile:
            line = line.rstrip()
            print(line)
            content.append(line.rsplit(":"))
            print(content)
    except IOError: pass

    numbers = getNumbers(content)

    ops = []
    for i in range(len(content)):
        op_str = content[i][1].strip()   
        ops.append(list(op_str))         
        
    ops = getClean(ops)
    
    calculation(numbers,ops,operations)


def getNumbers(content:list):
    numbers = []
    for i in range(len(content)):
        temp = []
        number = content[i][0].split(" ")
        print(number)
        for n in number:
            print(n)
            if n == "": continue
            else:temp.append(int(n))
        numbers.append(temp)    
    return numbers

def getClean(abc:list):
    for i,dizi in enumerate(abc):
        for element in dizi:
            if element.strip() == "":
                abc[i].remove(element)
    return abc


def calculation(numbers: list, ops: list, operations: dict):
    for i in range(len(numbers)):
        nums = numbers[i]     
        op_list = ops[i]       

        if len(op_list) != len(nums) - 1:
            print(f"Line {i+1}: operator count does not match number count!")
            continue
        result = nums[0]

        for op, num in zip(op_list, nums[1:]): #zip fonksiyonu iki listeden eleman çifti oluşturuyo (op_list[1],nums[1]) (op_list[2], nums[2]) şeklinde
            func = operations[op]   
            result = func(result, num)

        # Sonucu yazdır
        expr = " ".join(str(x) for x in nums) + " " + "".join(op_list)
        print(f"{expr} = {result}")


main()