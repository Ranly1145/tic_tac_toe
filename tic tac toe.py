a1, a2, a3, b1, b2, b3, c1, c2, c3 = (' ', ' ', ' ', ' ',
                                      ' ', ' ', ' ', ' ', ' ')
row_a = f'a  {a1} | {a2} | {a3} '
row_b = f'b  {b1} | {b2} | {b3} '
row_c = f'c  {c1} | {c2} | {c3} '


def field(row_a, row_b, row_c):
    print('   1   2   3 ')
    print(row_a)
    print('  ———+———+———')
    print(row_b)
    print('  ———+———+———')
    print(row_c)


def check(space):
    while space not in spaces:
        space = input('Неподходящее значение. Попробуйте ещё раз: ')
    return space


def win(a1, a2, a3, b1, b2, b3, c1, c2, c3):
    winner = ''
    if b1 == b2 == b3 or a2 == b2 == c2 or a1 == b2 == c3 or a3 == b2 == c1:
        winner = b2
    if (a1 == a2 == a3 or a1 == b1 == c1) and a1 != ' ':
        winner = a1
    if (c1 == c2 == c3 or a3 == b3 == c3) and c3 != ' ':
        winner = c3
    if winner == 'x':
        return 'ПОБЕДИЛИ КРЕСТИКИ!!!'
    if winner == 'o':
        return 'ПОБЕДИЛИ НОЛИКИ!!!'
    return 0


print('')
print('')
print('ПРАВИЛА ИГРЫ')
print('')
print('- Игра на двух участников.')
print('')
print('- Существует поле 3x3 такого типа:')
field(row_a, row_b, row_c)
print('')
print('- Названием клетки является комбинация её столбца и ряда.')
print('К примеру, верхняя клетка третьего столбца называется 3a,')
print('средняя клетка первого столбца - 1b и так далее.')
print('')
print('- Первый участник играет за крестики (x).')
print('Он выбирает любую клетку, указывая её название, '
      'и в неё записывается крестик.')
print('')
print('- Второй участник играет за нолики (o).')
print('Он выбирает любую из оставшихся восьми клеток.')
print('')
print('- Затем процесс повторяется, и первый участник выбирает')
print('из оставшихся после прошлого хода клеток.')
print('')
print('- Победит тот, кто первым в линию запишет три своих элемента.')
print('Линия может получиться горизонтальная, вертикальная или диагональная.')
print('')
print('Что же, приступим к игре!')
spaces = {'1a', '1b', '1c', '2a', '2b', '2c', '3a', '3b', '3c'}

while win(a1, a2, a3, b1, b2, b3, c1, c2, c3) == 0 and len(spaces) != 0:
    for symbol in ['x', 'o']:
        print('')
        print('')
        if symbol == 'x':
            print('ХОДЯТ КРЕСТИКИ (x)')
        elif symbol == 'o':
            print('ХОДЯТ НОЛИКИ (o)')
        turn = input('Впишите название клетки: ')
        turn = check(turn)
        if turn == '1a':
            a1 = symbol
        elif turn == '1b':
            b1 = symbol
        elif turn == '1c':
            c1 = symbol
        elif turn == '2a':
            a2 = symbol
        elif turn == '2b':
            b2 = symbol
        elif turn == '2c':
            c2 = symbol
        elif turn == '3a':
            a3 = symbol
        elif turn == '3b':
            b3 = symbol
        elif turn == '3c':
            c3 = symbol
        else:
            print('что-то пошло не по плану')
        row_a = f'a  {a1} | {a2} | {a3} '
        row_b = f'b  {b1} | {b2} | {b3} '
        row_c = f'c  {c1} | {c2} | {c3} '
        spaces.remove(turn)
        field(row_a, row_b, row_c)
        if win(a1, a2, a3, b1, b2, b3, c1, c2, c3) != 0 or len(spaces) == 0:
            break
print('')
print('')
if win(a1, a2, a3, b1, b2, b3, c1, c2, c3) == 0:
    print('ВЫШЛА НИЧЬЯ!!!')
else:
    print(win(a1, a2, a3, b1, b2, b3, c1, c2, c3))
print('')
print('')
