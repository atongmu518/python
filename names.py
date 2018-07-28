from name_function import get_formatted_name

print('Enter "q" at any time to quit.')
while Trur:
    first = input('\nPlease give me a first name: ')
    if first.lower() == 'q':
        break

    
    last = input('\nPlease give me a last name: ')
    if last.lower() == 'q':
        break

    full_name = get_formatted_name(first, last)
    print('The full name is :' + full_name.title())
