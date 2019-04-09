# Presents the purpose of the program
print('This program will calculate your Body Mass Index')

# Asks the user for their name
users_name = input('Hello, what is your name? ')

# Asks the user for their weight in pound, height in feet, and then inches afterwards
# weight = input(int('Please enter your weight in pounds'))
input_weight = int(input('Please enter your weight in pounds '))
input_feet = int(input('Please enter your height in feet, whole numbers only '))
input_inches = int(input('... and how many inches on top of that? '))

# divides users feet by 12 to get inches, adds this number on to the inches given already
total_inches = (input_feet * 12) + input_inches

# Uses the BMI formula to create the proper calculation
BMI = float((input_weight * 703) / (total_inches ** 2))

# Uses f-strings per Python 3.6 to construct a interpolated string, saves to variable BMI_phrase
BMI_phrase = str(f'Hello {users_name}, Your BMI is {BMI:.1f}, Would you like fries with that?')

# prints the string
print(BMI_phrase)
