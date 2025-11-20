def rect(num1,num2):
    p=2*(num1+num2)
    print("The perimeter of the rectangle is:",p)
    return(p)
def rect_area(num1,num2):
    a=num1*num2
    print("The area of rectangle is:",a)
    return(a)
num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
r=rect(num1,num2)
b=rect_area(2,3)
def sqr(num1):
    c=4*num1
    print("The perimeter of square is:",c)
    return(c)
def sqr_area(num1):
    d=num1*num1
    print("The area of square is:",d)
    return(d)
e=sqr(4)
f=sqr_area(5)
