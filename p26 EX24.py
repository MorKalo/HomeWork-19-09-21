#תרגיל רשות
num1=int(input('plz insert the first num'))
num2=int(input('plz insert the second num'))
div=1
max=0
while (num1 >= div) and (num2 >= div):
    if (num1%div==0) and (num2%div==0):
   #     print('מחלק של 2 המספרים שהוכנסו',div)
        if div>max:
           max=div
    div = div + 1
print('המחלק הגדול ביותר של 2 המספרים שהוכנסו הוא',max)




