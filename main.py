import datetime
date_now=datetime.datetime.now()
print(date_now.year)

# Say Hello
print('Hello, world!')
# ask for their name
print('What is your name? ')
myName = input()
# Greets them by name
print('It is good to meet you, ' + myName)
print('The length of your name is:')
# counts how many letters are in their name
print(len(myName))
# ask for their age
print('What is your age?')
myAge = input()
# shows how old they will be in a year
print('You will be ' + str(int(myAge) + 1) + ' in a year.')
# Shows what year they were born by subtracting their age from current year
birthYear = (date_now.year - (int(myAge)))
print("Your Birth year was:")
print(birthYear)
