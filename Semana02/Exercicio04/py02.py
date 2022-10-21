print('Hello World')
message = 'Hello World'
print(message)
print(len(message))
print(message.lower())
print(message.upper())
print(message.count('Hello'))
print(message.find('World'))
new_message = message.replace('World', 'Universe')
greeting = 'Hello'
name = 'Pedro'
message = greeting + name
message = '{}, {}. Welcome!'.format(greeting, name)
message = f'{greeting}, {name}. Welcome!'
print(dir(name))
print(help(str.lower))