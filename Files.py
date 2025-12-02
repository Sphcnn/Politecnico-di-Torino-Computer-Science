file = open("input.txt","r")
word =[]

for line in file:
   line = line.strip()
   for i in line.split(" "):
        word.append(i)

print(word)

max = len(word[0])
min = len(word[0])
max_word = word[0]
min_word = word[0]

for element in word:
    if len(element) > max:
        max_word = element
        max = len(element)
    elif len(element) < min:
        min_word = element
        min = len(element)
    else: pass

print(f'Longest word is {max_word} longs {max}')
print(f'Longest word is {min_word} longs {min}')


file.close()