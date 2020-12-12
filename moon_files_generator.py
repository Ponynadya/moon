import random

quantity = int(input('Сколько сгенерировать файлов: '))

for i in range(quantity):
    width = random.randint(1, 15)
    height = random.randint(1, 15)

    _list = []

    for h in range(height):
        output_string = ''
        for w in range(width):
            output_string += str(random.randint(0, 1))
        _list.append(output_string)

    with open('moon_' + str(i) + '.txt', 'w') as f:
        for _str in _list:
            f.write(_str + '\n')
