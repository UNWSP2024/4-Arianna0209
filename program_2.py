#Title: Ticket Calculator
#Author: Arianna Endres
#Date: 09/26/2025

total = 0
print('Enter the movies you would like to see or enter 0 to end.')
movie = input('Movie name: ')

while movie != '0':
	tickets = int(input(f'How many tickets would to like for {movie}? '))
	total += tickets
	movie = input('Next movie name: ')

print(f'Total amount of tickets: {total}')
