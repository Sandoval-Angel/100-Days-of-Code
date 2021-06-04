print('Welcome to the bill splitter!\n')

bill_amount = float(input('Enter bill amount: '))
tip_percent = int(input('Enter tip percentage: ')) / 100
num_people = int(input('Enter number of people: '))

total_cost = bill_amount + (bill_amount * tip_percent)
per_person = round(total_cost / num_people, 2)

print(f'\nPer person cost: {per_person}')
