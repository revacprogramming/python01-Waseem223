hrs = float(input("Enter Hours:"))
rate = float(input("enter rate"))
if hrs<40:
    pay=rate * hrs
    print(pay)
elif hrs>40:
    hrs=hrs-40
    print(40* rate + hrs*1.5*rate)