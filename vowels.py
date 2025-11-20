name=input("Enter name:")
vowels=['a', 'e', 'i', 'o', 'u','A', 'E', 'I', 'O', 'U']
cons=0
for char in name:
    if char in vowels:
        print("Vowels",char)
    else:
         print("consonants",char)

