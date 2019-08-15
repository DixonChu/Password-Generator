'''python
source code goes to Dixon
'''

import random
import time

        
def generate_pass():
    print("*Maximum lenght is 27")
    # Password length depends on user
    pass_length = int(input("Enter the lenght of the password you want: "))
 
    # Menu
    print('Password with:')
    print('1. Letter.')
    print('2. Letter and numbers.')
    print('3. Letter, numbers and symbols.')
    print('4. All of the above.')

    time.sleep(1) #user_choice will print out after 1 second
    user_choice = input('\nPlease choose one of the option: ') #Let user to choose which password they want
    
    option = pass_generator(user_choice, pass_length)

    print('Your password is generating. Please wait a moment.')
    time.sleep(2.5) 
    print('Your password is:', option)
    time.sleep(1)





def pass_generator(user_choice, pass_length):
    letter = 'abcdefghijklmnopqrstuvwxyz' # Only letter
    l_number = 'abcdefghijklmnopqrstuvwxyz1234567890' # Letter with numbers
    l_symbol = 'abcdefghijklmnopqrstuvwxyz!@#$%^&*()' # Letter with numbers and symbols
    l_num_symb = 'abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*' # Password with letters, numbers and symbol

    #if user choose choice 1, then print pass with just letter
    if user_choice == '1':
        option = ("".join(random.sample(letter, pass_length))) 
        return option
    
    #if user choose choice 1, then print pass with just letter with numbers
    elif user_choice == '2':
        option = ("".join(random.sample(l_number, pass_length)))
        return option

    #if user choose choice 1, then print pass with just letter with numbers and symbols
    elif user_choice == '3':
        option = ("".join(random.sample(l_symbol, pass_length)))
        return option

    #if user choose choice 1, then print pass just letter with numbers and symbols 
    elif user_choice == '4':
        option = ("".join(random.sample(l_num_symb, pass_length)))
        return option

    #if user choose choice out of range, then print pass just letter with numbers and symbols 
    else:
        option = ("".join(random.sample(l_num_symb, pass_length)))
        print("We will give you option 4 because you enter a number that is larger than 4 or something out of range")
        time.sleep(1)
        return option

generate_pass()