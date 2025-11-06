#Cinema Booking App
LETTERS = ["A","B","C","D","E","F","G","H","I","J"]
TICKET_PRICE = 10 
planCinema = []

for i in range(10):
    row = [j+1 for j in range(10)]  # her seferinde yeni satır
    planCinema.append(row)


for i in range(10):
    planCinema.append(row)
    i+=1

for i in range(10):
    for j in range(10):
        planCinema[i][j] = j+1

for i,letter in enumerate(LETTERS):
    print(f'{letter} {planCinema[i]}')
    print()

ticketNumber = int(input("How many tickets do you want to buy ? "))
ticketCost = 0

for k in range(ticketNumber):
    ticket = input("Choose your ticket please : ")
    ticketRow = ticket[0]
    ticketColumn = int(ticket[1:])
    print(ticketRow,ticketColumn)

    for i,letter in enumerate(LETTERS):
        if letter == ticketRow:
            if planCinema[i][ticketColumn-1] == 0:
                print(f'Sorry this seat is already sold. Choose another seat.')
                ticket = input("Choose your ticket please : ")
                ticketRow = ticket[0]
                ticketColumn = ticket[1:]
                break
            else:
                print(f'Okay you can buy this seat for {TICKET_PRICE} euro \n ')
                ticketCost = ticketCost + TICKET_PRICE
                planCinema[i][ticketColumn-1] = 0
                for j,letter in enumerate(LETTERS):
                    print(f'{letter} {planCinema[j]}')
                    print()
                break
    else:
        print("You can only choose among these seats")
        for j,letter in enumerate(LETTERS):
            print(f'{letter} {planCinema[j]}')
            print()
        ticket = input("Choose your ticket please : ")
    k += 1
print(f'Total cost of your tickets {int(ticketCost)} ')

