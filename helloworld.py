# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


print("Welcome")
print("Now Loading")


users = ['Exclusive Contract', 'Client Sharing', 'Property Searching']

for user in users:
    print("Welcome, " + user.title() + " Agent.")
    print("Do you mind if I ask you a few questions?")


print("Which skills or property locations would you like to broadcast to other agents?")
selected = input()
print(selected)
print("Is this correct?")



a = 5
b = 12
print(a + b) 
print(b - 2*a)

x = 'hello world!'
print(x)
'''
x is a string
'''
i = False
o = True
f = 1.55
f = 'what1'
'''
f is float
'''

print(type(x))
print(type(i))
print(type(o))
print(type(f))

z = "Say"
y = "Hello "
print(z + y)

z = "1"
y = "2"
print(z + y)

z = "hello! "
print(z * 5)

#Loops
for n in [0,1,2,3,4,5,6,7,8,9,10,12,20,25]:
    print("hello")
    print("world")
    print(n)
print("Finished")


    
for n in range (0,1001):
    print(n)
    
def multiplier(a,b,c,d,e): 
    x = a*b*c*d*e
    return x

z = multiplier(5,2,1,3,2)
print(z)
    


#conditions
hungry = 1
thirsty = 1
if hungry==1 or thirsty==1:
    print("yes, hungry is one")
else:
    print("no it failed")

#hot = True
#temp = 80
#while hot:
#    print("It's hot!")
#    if temp < 90: 
#        hot = False
#print("done")


selected = input()
print(selected)
    
def menu():
    print("1. Trade")
    print("2.Show P/L")
    print("3.Quit")
    
def show_pl():
    print("Showing P/L")
done = False
while not done:
    menu()
    selected = input()
    if selected == "3":
        done=True
    if selected=="2":
        show_pl()
    if selected=="1":

        print("Thank you for trading with us!")

    print('Interest Calculator:')
    amount = float(input('Principal amount ?'))
    roi = float(input('Rate of Interest ??'))
    yrs = int(input('Duration (no. of years) ?'))
    total = (amount * pow(1+ (roi/100), yrs))
    interest = total - amount
    print('\nInterest = %.2f' % interest)

'''
A = P(1+r/n)^nt

'''

import keyword
keyword.iskeyword("try")



 
test1 = "learn Python"



    

