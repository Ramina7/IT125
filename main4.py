flags = {
    'ru': {'red', 'blue', 'white'},
    'kg': {'red', 'yellow'},
    'ua': {'red', 'blue'},
    'uk': {'yellow', 'blue'},
    'kz': {'blue', 'yellow'},
    'it': {'green', 'white', 'red'},
    'us': {'red', 'blue', 'white'},
    'au': {'red', 'blue', 'white'}
}


while True:
    user_input = input('Введите цвет флага на англ (или "exit" для выхода): ')
    
    if user_input == 'exit':
        break

    for key, value in flags.items():
        if user_input in value:
            print(key)