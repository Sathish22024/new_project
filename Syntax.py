#syntax
"""if condition:
       //code"""

"""a=10
if a==10:
    print('a is 10')


mark=int(input())
if mark>35:
    print("pass")
print('program is excuted')

a=-1
if a>0:
    print('Number is positive')
print('excuted')

a=10
if a>0:
    print('positive')
else:
    print('negative')

a=10
if a>18:
    print('eligable')
else:
    print('not eligable')


a=110
if a>18:
    print('eligable')
else:
    print('not eligable')


a=int(input('enter amount:'))
if a>2000:
    print('loan is appoval')
else:
    print('not eligable')


a=50
if a>0 and a<=30:
    print('rage 1 to 30')
elif a>31 and a<=49:
    print('31 to 49')
elif a>=50 and a<60:
    print('50 to 59')
else:
    print('60 above')


a=int(input())
if a>0 and a<=17:
    print('child')
elif a>18 and a<=27:
    print('adult')
elif a>=28 and a<40:
    print('old')
else:
    print('40 above')"""


#Nested if...else
"""a=50
if a>=10 and a<20:
    if a>5:
        print('above 5')
    else:
        print('below 5')
else:
    print('above 20')


a=int(input('Enter number:'))
if a>5 and a<30:
    if a>10:
        print('above 10')
    else:
        print('below 10')
elif a>31 and a<50:
    if a>40:
        print('above 40')
    else:
        print('below 40')
else:
    print('above 51')


s=int(input('Enter number:'))
if s>=90 and s<=100:
    print('Grade:A')
elif s>=80 and s<=89:
    print('Grade:B')
elif s>=70 and s<=79:
    print('Grade:C')
elif s>=60 and s<=69:
    print('Grade:D')
else:
    "60 below"
    print('Grade:F')


age=int(input('Enter Age:'))
days=str(input('Enter days:'))
if days in(['monday','tuesday','wednesday','thursday','friday']):
         if age<18:
             print('Ticket is $12')
         else:
             age>=18
             print('Ticket is $15')
if days in(['saturday','sunday']):
         if age<18:
             print('Ticket is $15')
         else:
             age>=18
             print('Ticket is $20')


amount=int(input('Enter the total purchase amount:'))
member=str(input('Are you a premium member:'))
if member=='yes':
    print('Total amount to be paid:',amount)
elif amount>=50:
    print('Total amount to be paid:',amount)
else:
    print('Total amount to be paid:',amount+10)"""

# Loops
# 1.while
# 2.for

#while
   # continue
   # break
"""a=0
while a<=5:
    print(a)
    a=a+1
a=0
while a<=10:
    print(a)
    a=a+1
a=45
while a<=95:
    if a%2==0:
        print(a)
    a=a+1

a=0
while a<=10:
    a+=1
    if a==5:
        continue
    print(a)


a=57
while a<=98:
    a+=1
    if a==59 or a==69 or a==79 or a==89:
        continue
    print(a)"""
        
'''a=0
n=int(int(input()))
while a<=n:
    print(a)
    a+=1
    if a==25:
        break'''

'''a=90
n=int(input())
while a<=199:
    a+=1
    if a==159:
        continue
    print(a)'''


'''a=1001
n=int(input())
while a<=n:
    print(a)
    a+=1
    if a==1112:
        break

v=list(range(1,10,2))
print(v)'''

#for
'''for i in range(10):
    print(i)
    
for i in range(10):
    print(i,end='')

for i in ['a','b','c','d','e']:
    print(i)'''

for i in range(0,51):
    if i%2==0:
        print('even')
    else:
        print('odd')

    
    
    
    

























        



























































