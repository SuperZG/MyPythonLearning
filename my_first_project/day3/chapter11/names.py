from name_function import get_formatted_name

print('Type in quit to exit the program.')
while True:
    first = input('Please input the first name: ')
    if first == 'quit':
        break
    last = input('Please input the last name: ')
    if last == 'quit':
        break
    neat_name = get_formatted_name(first, last)
    print('Neatly name:', neat_name)
