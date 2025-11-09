#Cinema Booking App (will be improved)
LETTERS = ["A","B","C","D","E","F","G","H","I","J"]
TICKET_PRICE = 10 
planCinema = []

for i in range(10):
    row = [j+1 for j in range(10)]  # her seferinde yeni satır
    planCinema.append(row)

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