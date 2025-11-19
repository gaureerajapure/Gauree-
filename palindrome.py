n=int(input("Enter number:"))
n = str(n)
length = len(n)
if(n == n[::-1]):
    print("Your number is palindrome")
else:
    print("Your number is not palindrome")