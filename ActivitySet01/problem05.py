# Functions
def computepay():
    if hrs<40:
        pay=hrs*rate
        return pay
    elif hrs>40:
        pay=40*rate+(hrs-40)*rate*1.5
        return pay
    


hrs=int(input("Enter hours"))
rate=float(input("Enter the rate"))
pay = computepay()
print("Pay", pay)

