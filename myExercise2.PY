#Cinema Booking App (will be improved)
LETTERS = ["A","B","C","D","E","F","G","H","I","J"]
TICKET_PRICE = 10

def main():
    name = input("Enter your name : ")
    planCinema = create_cinema_plan()
    print_cinema_plan(planCinema)

    sold_seats, total_cost = choose_tickets(planCinema)
    print_receipt(name,sold_seats, total_cost)


def create_cinema_plan():

    planCinema = []
    for i in range(10):
        row = [j + 1 for j in range(10)]
        planCinema.append(row)
    return planCinema


def print_cinema_plan(planCinema):

    for i, letter in enumerate(LETTERS):
        print(f'{letter} {planCinema[i]}')
        print()


def choose_tickets(planCinema):
   
    ticketNumber = int(input("How many tickets do you want to buy? "))
    ticketCost = 0
    sold_seats = []  

    for k in range(ticketNumber):
        while True:
            ticket = input("Choose your ticket (example: A1): ")
            if len(ticket) < 2:
                print("Invalid format. Try again (example: A1).")
                continue

            ticketRow = ticket[0].upper()
            try:
                ticketColumn = int(ticket[1:])
            except ValueError:
                print("Invalid seat number. Try again.")
                continue

            
            if ticketRow not in LETTERS or not (1 <= ticketColumn <= 10):
                print("You can only choose among valid seats (A-J and 1-10).")
                print_cinema_plan(planCinema)
                continue

            
            row_index = LETTERS.index(ticketRow)
            col_index = ticketColumn - 1

         
            if planCinema[row_index][col_index] == 0:
                print("Sorry, this seat is already sold. Choose another seat.")
                print_cinema_plan(planCinema)
                continue
            else:
                print(f'Okay, you can buy this seat for {TICKET_PRICE} euro.\n')
                ticketCost += TICKET_PRICE
                planCinema[row_index][col_index] = 0
                sold_seats.append(ticketRow + str(ticketColumn))
                print_cinema_plan(planCinema)
                break  

    return sold_seats, ticketCost


def print_receipt(name,sold_seats, total_cost):
    """
    Kullanıcının aldığı tüm koltukları ve toplam ödemeyi yazdıran fiş fonksiyonu.
    """
    print(name)
    print("\n" + "-" * 40)
    print("RECEIPT")
    print("-" * 40)

    if not sold_seats:
        print("You did not buy any tickets.")
    else:
        print("You bought the following seats:")
        for seat in sold_seats:
            print(f"- Seat {seat}: {TICKET_PRICE} euro")
        print("-" * 40)
        print(f"Total cost of your tickets: {int(total_cost)} euro")

    print("-" * 40)
    print("Enjoy the movie!")
    print("-" * 40)




main()






'''TO DO LİST 

LEVEL 1 - Basic Improvements

 Kullanici büyük/küçük harf fark etmeksizin koltuk girebilsin (.upper()).

 Koltuk numarasinin geçerli olup olmadiğini kontrol et (1-10 arasi ve harf A-J arasi olmali).

 Satin alinan koltuklari bir listede tut ve sonunda yazdir (boughtTickets = []).

 Fiyati koltuk tipine göre değiştir:

İlk 3 sira: 15 €

Orta 4 sira: 10 €

Son 3 sira: 8 €

 Toplam ücret yazarken biçimi düzelt (print(f"Total cost: {ticketCost} €")).

🟡 LEVEL 2 - Smart Features

 Satilmiş ve boş koltuk sayisini hesapla (örnek: sold = sum(row.count(0) for row in planCinema)).

 Koltuk haritasini daha görsel göster:

“O” → boş koltuk

“X” → satilmiş koltuk

 Satin alma sonrasi “✅ Seat A5 successfully booked!” mesaji göster.

 Bilet satin alimi tamamlandiğinda toplam gelir ve kalan koltuk sayisini yazdir.

 Satin alma işlemi bitince “Devam etmek ister misiniz? (Y/N)” sorusu ekle.

🔵 LEVEL 3 - Advanced

 Bilet iptal etme sistemi ekle (iptal edilen koltuğu tekrar aç).

 Birden fazla film için farkli salon planlari oluştur (cinemaPlans = {"Matrix": plan1, "Avatar": plan2}).

 Satiş verilerini .txt veya .json dosyasina kaydet (program yeniden açildiğinda kaldiği yerden devam etsin).

 Satin alma geçmişini göster (print("You bought:", ", ".join(boughtTickets))).

🔴 LEVEL 4 - Pro Mode

 Tkinter veya pygame ile arayüzlü versiyon oluştur (koltuklara tiklayarak seçim).

 Kullanici hesap sistemi ekle (isim, bakiye, satin alinan biletler).

 Rastgele dolu koltuklar oluşturmak için başlangiçta random atama yap:


'''