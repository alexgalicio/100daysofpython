print('Welcome to the tip calculator.')
bill = float(input('What was the total bill? $'))
tip = int(input('What percentage tip would you like to give? 10, 12, or 15? '))
people = int(input('How many people to split the bill? '))

convert_tip = tip / 100
total_tip = bill * convert_tip
total_bill = bill + total_tip
total_amount = total_bill / people

print(f'Each person should pay ${round(total_amount, 2)}')
