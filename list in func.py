a=[1,2,3,4,5,6]
def func(a):
    largest=a[0]
    second=0
    for num in a:
        if num>largest:
            second=largest
            largest=num
        elif num>second and num!=largest:
            second=num
    
    return second
print(func(a))