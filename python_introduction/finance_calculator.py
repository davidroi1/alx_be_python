income = int(input('Enter your monthly income: '))
expenses = int(input('Enter your total monthly expenses: '))
saved = income - expenses
projected_saving = saved * 12 + (saved * 12 * 0.05)

print(f'Your monthly savings are ${saved}.')
print(f'Projected savings after one year, with interest, is: ${projected_saving:.0f}.')