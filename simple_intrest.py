def simple_interest(p,t,r):
    print(f'the principle is {p}')
    print(f'the time is {t}')
    print(f'the rate is {r}')
    si = (p*t*r)/ 100
    print(f"the simple intrest is {si}")
    return si
simple_interest(8,6,8)



def simple_intrest(p,t,r):
    print(f"the principle is {p} ")
    print(f"the time is {t} ")
    print(f"the rate is {r} ")

    si = (p* t* r)/100
    print(f"the simple interest is {si}")

P = int(input("enter the principal amount: "))
T = int(input("enter the time period: "))
R = int(input("enter the rate of interest: "))
simple_intrest(P,T,R)



    