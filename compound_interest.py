def compound_interest(principal, rate, time):
    amount = principal * (pow((1+rate/100),time))
    CI = amount - principal
    print(f"compound interest is {CI}")
compound_interest(10000, 10.25, 5)


##### User input 
def comound_interest(principal, rate, time):
    amount = principal*(pow((1 + rate/100),time))
    CI = amount - principal
    print(f"compound interest is {CI}")

principal = int(input("enter the principal amount: "))
rate = int(input("enter the rate of interest: "))
time = int(input("enter the time in year: "))
comound_interest(principal, rate, time)


##### Without using pow() function 
p = 1200
t = 2
r = 5.4
a = p*(1+r/100)**t
ci = a - p
print(ci)


##### Using for loop
def compound_interest(principal, rate, time):
    amount = principal
    for i in range(time):
        amount = amount *(1 + rate /100)
    CI = amount - principal
    print(f"compound interest is {CI}")
compound_interest(1200, 5.4, 2)
