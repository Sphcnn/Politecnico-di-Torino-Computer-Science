#Exercises of Lab4
numbers = []
sum_numbers = 0

while True:
    number = input("Enter a number (0 to quit): ")
    if number == "0":
        break   
    numbers.append(int(number))
    sum_numbers += int(number)

if numbers:  
    print(f"Sum of your numbers: {sum_numbers}")
    print(f"Max and min of your numbers: {max(numbers)}, {min(numbers)}")
else:
    print("You didn't enter any numbers.")
