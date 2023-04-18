import json

def open_json_file(file: str):
    try:
        with open(file) as json_file:
            data = json.load(json_file)
            return data
    except:
        print(f"An error has ocurred, can't open the file {file}")
        exit()


def finder(verb):
    for v in verbs['verbs']:
        if verb in v.values(): 
            return v        
            

def find():
    print('* ' * 27)
    print('Press enter to leave or write the verb you want')

    while True:
        val_2_find = input('write the verb you want to find: ')

        if val_2_find == '':
            break

        result = finder(val_2_find)

        if result == None:
            print(f'Verb {val_2_find} is not found')
            continue

        print('Base:            ' + result['Base'])
        print('Past simple:     ' + result['Past-simple'])
        print('Past participle: ' + result['Past-Participle'])

def game():
    while True:
        print('* ' * 27)
        print('Chose an option:')
        print('1 10 verbs')
        print('2 20 verbs')
        print('3 30 verbs')
        print('4 50 verbs')
        print('5 100 verbs')
        print('0 to exit')

        try:
            option = int(input('Write your answer: '))
        except ValueError:
            print('Please enter a valid option')
            continue
            

        if option == 0:
            print('* ' * 27)
            break
            


verbs = open_json_file('verbs.json')

while True:
    print('Choose an option:')
    print('1 to Find a verb')
    print('2 to play')
    print('0 to exit')    
    try:
        option = int(input("Write a number: "))
    except ValueError:
        print('* ' * 27)
        print('Please enter a valid option')
        continue

    if option == 1:
        find()
    elif option == 2:
        game()
    elif option == 0:
        print('Good bye :)')
        break
    else:
        continue





    
        