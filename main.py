import json

def open_json_file(file: str):
    try:
        with open(file) as json_file:
            data = json.load(json_file)
            return data
    except:
        print(f"Ha ocurrido un error, no se ha podido abrir el archivo {file}")


def finder(verb):
    for v in verbs['verbs']:
        if verb in v.values(): 
            return v        
            
verbs = open_json_file('verbs.json')

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



    
        