greeting = 'Hello'
name = 'pigasso'

message = '{}, {}. Welcome!'.format(greeting, name)
message1 = f'{greeting.lower()}, {name.upper()}. Welcome!'

print(message)
print(message1)

print(message.find('p'))

print(dir(message))
print(help(str))
print(help(str.lower))

