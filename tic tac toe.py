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
    if ((a1 == 'x' and a2 == 'x' and a3 == 'x') or
       (b1 == 'x' and b2 == 'x' and b3 == 'x') or
       (c1 == 'x' and c2 == 'x' and c3 == 'x') or
       (a1 == 'x' and b1 == 'x' and c1 == 'x') or
       (a2 == 'x' and b2 == 'x' and c2 == 'x') or
       (a3 == 'x' and b3 == 'x' and c3 == 'x') or
       (a1 == 'x' and b2 == 'x' and c3 == 'x') or
       (a3 == 'x' and b2 == 'x' and c1 == 'x')):
        return 'ПОБЕДИЛИ КРЕСТИКИ!!!'
    if ((a1 == 'o' and a2 == 'o' and a3 == 'o') or
       (b1 == 'o' and b2 == 'o' and b3 == 'o') or
       (c1 == 'o' and c2 == 'o' and c3 == 'o') or
       (a1 == 'o' and b1 == 'o' and c1 == 'o') or
       (a2 == 'o' and b2 == 'o' and c2 == 'o') or
       (a3 == 'o' and b3 == 'o' and c3 == 'o') or
       (a1 == 'o' and b2 == 'o' and c3 == 'o') or
       (a3 == 'o' and b2 == 'o' and c1 == 'o')):
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
    print('')
    print('')
    print('ХОДЯТ КРЕСТИКИ (x)')
    turn = input('Впишите название клетки: ')
    turn = check(turn)
    if turn == '1a':
        a1 = 'x'
    elif turn == '1b':
        b1 = 'x'
    elif turn == '1c':
        c1 = 'x'
    elif turn == '2a':
        a2 = 'x'
    elif turn == '2b':
        b2 = 'x'
    elif turn == '2c':
        c2 = 'x'
    elif turn == '3a':
        a3 = 'x'
    elif turn == '3b':
        b3 = 'x'
    elif turn == '3c':
        c3 = 'x'
    else:
        print('что-то пошло не по плану')
    row_a = f'a  {a1} | {a2} | {a3} '
    row_b = f'b  {b1} | {b2} | {b3} '
    row_c = f'c  {c1} | {c2} | {c3} '
    spaces.remove(turn)
    field(row_a, row_b, row_c)
    if win(a1, a2, a3, b1, b2, b3, c1, c2, c3) == 0 and len(spaces) != 0:
        print('')
        print('')
        print('ХОДЯТ НОЛИКИ (o)')
        turn = input('Впишите название клетки: ')
        turn = check(turn)
        if turn == '1a':
            a1 = 'o'
        elif turn == '1b':
            b1 = 'o'
        elif turn == '1c':
            c1 = 'o'
        elif turn == '2a':
            a2 = 'o'
        elif turn == '2b':
            b2 = 'o'
        elif turn == '2c':
            c2 = 'o'
        elif turn == '3a':
            a3 = 'o'
        elif turn == '3b':
            b3 = 'o'
        elif turn == '3c':
            c3 = 'o'
        else:
            print('что-то пошло не по плану')
        row_a = f'a  {a1} | {a2} | {a3} '
        row_b = f'b  {b1} | {b2} | {b3} '
        row_c = f'c  {c1} | {c2} | {c3} '
        spaces.remove(turn)
        field(row_a, row_b, row_c)
print('')
print('')
if win(a1, a2, a3, b1, b2, b3, c1, c2, c3) == 0:
    print('ВЫШЛА НИЧЬЯ!!!')
else:
    print(win(a1, a2, a3, b1, b2, b3, c1, c2, c3))
print('')
print('')
