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
''' 2
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
'''  
''' 3
TICKET = 100
buyers = 0

while(TICKET != 0):
    ticket = int(input("How many tickets do you want to buy ? "))
    while(ticket > 4 ):
        ticket = int(input("You can buy 4 ticket at most. Try again : "))
    buyers += 1
    TICKET = TICKET - ticket
    print(f'{TICKET} tickets left')

print(f'The number of buyers : {buyers}')
'''

