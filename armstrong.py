g = int(input("Enter a number: ")) #153
g_str = str(g)  #153
list = []
length = len(g_str)  #3
for i in range(0, length):   #0,3
    digit = g_str[i]  #digit = 1
    digit = int(digit)
    digit = digit ** length
    list.append(digit) #list = [1,125,27]
if(g == sum(list)):
    print("Your number is armstrong")
else:
    print("Your number is not armstrong")