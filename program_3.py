#Title: Average Rainfall Calculator
#Author: Arianna Endres
#Date: 09/26/2025

total_rainfall = 0
years = int(input('Enter the number of years you would like to calculate the average rainfall during: '))
months = years * 12
for years in range(years):
    for months in range(12):
        monthly_rainfall = float(input('Enter the inches of rainfall received this month: '))
        total_rainfall += monthly_rainfall

print(f'Total number of months: {months}')
print(f'Total amount of rainfall: {total_rainfall:.2f} inches')

average_rainfall = total_rainfall / months
print(f'Average amount of rainfall each month: {average_rainfall:.2f} inches')
