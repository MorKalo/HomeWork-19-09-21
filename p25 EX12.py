#תרגיל רשות
num=int(input('plz insert a num'))
sum=0
while num != 0:
    dig=num%10
    sum=sum+dig
    num=num//10
#    print(dig)
print('the sum of the number that u input is:',sum)

