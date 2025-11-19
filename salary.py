salary = int(input("Enter your salary in Inr:"))
if salary<=10000:
    bonus = salary*0.1
    print("salary + bonus :", salary+bonus)
elif 10000< salary <= 20000:
    bonus = salary*0.2
    print("salary + bonus :", salary+bonus)
else:
    bonus = salary*0.4
    print("salary + bonus :", salary+bonus)