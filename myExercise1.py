
sentence = input("Enter your sentence: ")


newSentence = ""
for ch in sentence:
    if ch == " ":
        newSentence += "--"
    else:
        newSentence += ch
        newSentence += "-"

print(f'---{newSentence}---')


