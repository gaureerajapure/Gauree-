vowels=['a','e','i','o','u','A','E','I','O','U']
def func(a):
    for char in a:
        if char in vowels:
            print("Vowels:",char)
        else:
            print("Consonants:",char)
    return char
a=func('e')
a=func('g')
