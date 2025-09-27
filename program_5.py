#Title: Budget Calculator
#Author: Arianna Endres
#Date: 09/26/2025

total = 0
budget = float(input('What was your budget? $'))
print('Enter expenses or enter 0 to end.')
expense = float(input('Expense: $'))
while expense != 0:
    total += expense
    expense = float(input('Next expense: $'))

print(f'Your total expenses are ${total:.2f}')
if total > budget:
    print('You’re over budget, try to cut back on your spending.')
else:
    print('You’re under budget, great job!')
