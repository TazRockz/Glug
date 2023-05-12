# Tip Calculator #
food_amount = float(input('Please Enter the Amount of Food Bought: '))
tip_amount = float(input('Please Enter the amount of Tip Percentage: '))
print(f'⚖️ The Tip Amount:Rs {tip_amount / 100 * food_amount} ⚖️')
print('|\n')
print(f'💵 Total Amount:Rs {tip_amount / 100 * food_amount + food_amount} 💵')