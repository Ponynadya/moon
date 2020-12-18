def calculate(moon_map) -> list:
    """

    :param moon_map: 
    :return: 
    """
    hole = 1

    to_check = []
    global_holes = 0

    for y, y_value in enumerate(moon_map):
        for x, x_value in enumerate(y_value):
            if moon_map[y][x] == hole:
                a = moon_map[y][x]
                to_check.append((y, x))

                while to_check:
                    # find near
                    target = to_check.pop()
                    for y_step in range(-1, 2):
                        if target[0] + y_step < 0:
                            continue
                        try:
                            if moon_map[target[0] + y_step][target[1]] == hole:
                                to_check.append((target[0] + y_step, target[1]))

                        except IndexError:
                            continue

                    for x_step in range(-1, 2):
                        if target[1] + x_step < 0:
                            continue
                        try:
                            if moon_map[target[0]][target[1] + x_step] == hole:
                                to_check.append((target[0], target[1] + x_step))

                        except IndexError:
                            continue

                    moon_map[target[0]][target[1]] = 0

                global_holes += 1

    return global_holes


if __name__ == "__main__":

    file_name = input('Введите название файла: ')
    with open(file_name + '.txt', 'r') as f:
        file_data = f.read()
        raw_moon_data = file_data.split('\n')
        raw_moon_data.pop()


    moon = []
    for _str in raw_moon_data:
        row = []
        _str = _str.split()
        for symbol in _str:
            row.append(int(symbol))
        moon.append(row)

    print('MOON MAP:')
    for y in moon:
        for x in y:
            print(x, ' ', end='')
        print()

    print('Quantity of holes: ', calculate(moon))
