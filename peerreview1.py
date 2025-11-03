vowel=["a", "e", "i", "o", "u","A","E","I","O","U"]

exceptionCountries = ["Belize", "Cambodge", "Mexique", "Mozambique", "Zaïre", "Zimbabwe"]
pluralCountries = ["Etats-Unis", "Pays-Bas"]
countryName = input("Enter the name of country in French : ")

while(countryName==""):
    countryName = input("Enter a valid country : ")


if countryName in exceptionCountries:
    print(f'Your country is exception so : le {countryName}')

else:
    
    if countryName in pluralCountries:
        print(f"Your country\'s name is plural so : les {countryName}")
    
    elif countryName[-1].lower() == "e":
        if countryName[0] in vowel:
            print(f'Your country\'s name ends with \"e\" (feminine) and starts with vowel so : l\'{countryName}')
        else:
            print(f'Your country\'s name ends with \"e\" (feminine) so : la {countryName}')
            
    else:
        if countryName[0] in vowel:
           print(f'Your country\'s name does not end with \"e\" starts with vowel so : l\'{countryName}')
        else:
           print(f'Your country\'s name does not end with \"e\" so : le {countryName}')
            
        #adsa