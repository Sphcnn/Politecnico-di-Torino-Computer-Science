#Exercises of Lab4  
''' 1
PIN=1234

for i in range(2):
    password = int(input("Enter your password : "))
    if password == PIN:
        print("You have entered successfuly !")
        break
    else:
        if not i >= 2:
            print("Try Again")
        else:
            print("Your card is blocked")

'''

number = int(input("Enter a number : "))
i=2
while(number!=0):
    if number % i == 0:
        print(i)
        number = number / i
        if number == 1:
            break
    else:
        i+=1
        
print("adsa")