# Loops & Iterators

a=[]
while True:  
    b=input("Enter the number")
    if(b=='done'):
        break
    try:
       b=int(b) 
       a.append(b)
    except :
           print("Invalid input")
c=max(a)  
d=min(a)
print('Maximum is',c)
print('Minimum is',d)
       
