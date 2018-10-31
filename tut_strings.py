#Print Welcome Message
print('Hello World')

message = 'Hello World'

#Replaces characters within the string
new_message = message.replace('World','Universe')

#Simple Welcome String
welcome_message = 'Welcome'

print(welcome_message)

#Use \ to excempt one '
print('Bobby\'s World')

#Multiple line String
warning = '''This is a warning!! If you
do that againg you will be punised!!!
You won't receive another warning.'''

print(warning)

#Prints length of Message
print(len(welcome_message))

#Prints index(location) of specific character
print(welcome_message[0])
print(welcome_message[6])

#Prints index from start point to end point
#Blank means Beginning/End
print('Hello World'[0:5])
print('Hello World'[:5])
print('Hello World'[6:])

#Prints text in Upper/Lowercase
print('Hello World'.lower())
print('Hello World'.upper())

#Prints how many there are in the Message
print('Hello World'.count('Hello'))
print('Hello World'.count('l'))
print('Hello World'.count('ll'))

#Prints what index it starts at
print(message.find('World'))
#-1 means that it does not exist within message
print(message.find('Universe'))

print(new_message)

#Prints variable together
greeting = 'Hello'
name = 'Jason'

salutation = greeting + ', ' + name + '. Welcome!!'

print(salutation)

welcome = '{}, {}. Welcome!!'.format(greeting, name)

print(welcome)

first = 'Jaelin'
middle = 'Bryan'
last = 'Ford'

praise = f'{first} {middle} {last} is the best programmer, period.'

print(praise)
