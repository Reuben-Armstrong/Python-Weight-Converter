# Weight Converter
# Converts between kilograms and pounds

# Title
print('------------------------------------------------------------------------------')
print(' Weight Converter')
print('------------------------------------------------------------------------------')
print(' What would you like to do?:')
print('------------------------------------------------------------------------------')
print(' [1] (kg) Kilograms   ->  (lb) Pounds')
print(' [2] (lb) Pounds      ->  (kg) Kilograms')
print('------------------------------------------------------------------------------')
print('')

# Choose what will happen
while True:
    method_option = input('What would you like to do?: ')

    # (kg) Kilograms -> (lb) Pounds
    if method_option == '1':
        while True:
            try:
                print('')
                method = '(kg) Kilograms -> (lb) Pounds'
                old_unit = 'kg'
                new_unit = 'lb'
                current_weight = float(input('How many Kilograms (kg)?: '))

                new_weight = current_weight * 2.205

                break
            
            except ValueError:
                print('That is not a valid number! Try again.')

    # (lb) Pounds -> (kg) Kilograms
    elif method_option == '2':
        while True:
            try:
                print('')
                method = '(lb) Pounds -> (kg) Kilograms'
                old_unit = 'lb'
                new_unit = 'kg'
                current_weight = float(input('How many Pounds (lb)?: '))

                new_weight = current_weight / 2.205

                break
            
            except ValueError:
                print('That is not a valid number! Try again.')

    # If user does not input a valid option
    else:
        print('Please enter either 1 or 2')
        continue

    break

# Output
print('')
print('------------------------------------------------------------------------------')
print(f' {method}')
print(f' {current_weight} {old_unit} -> {round(new_weight, 1)} {new_unit}')
print('------------------------------------------------------------------------------')
print('')
input('Press the Enter Key to Exit...')