import random
def is_value(x):
    if x.isdigit():
        return True

digits = '123456789'
lowercase_letters = 'abcdefghjkmnpqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKMNPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
gog = 'il1Lo0O'
chars = ''
res = ''
c = ''

while True:
    while True:
        len = input('Введите длину пароля')
        if is_value(len) == True:
            break
        else:
            print('а может быть вы введете нормально число')
            continue



    while True:
        notsim = input('Включать ли неоднозначные символы il1Lo0O')
        if notsim == 'да':
            chars += gog
            break
        elif notsim == 'нет':
            break
        else:
            print('введите да или нет')
            continue

    while True:
        num = input('Включать ли цифры 0123456789')
        if num.lower() == 'да':
            chars += digits
            c += '+'
            break
        elif num == 'нет':
            break
        else:
            print('введите да или нет')
            continue


    while True:
        buk = input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz')
        if buk.lower() == 'да':
            chars += lowercase_letters
            c += '-'
            break
        elif buk == 'нет':
            break
        else:
            print('введите да или нет')
            continue


    while True:
        BUK = input('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        if BUK.lower() == 'да':
            chars += uppercase_letters
            c += '!'
            break
        elif BUK == 'нет':
            break
        else:
            print('введите да или нет')
            continue





    while True:
        sim = input('Включать ли символы !#$%&*+-=?@^_?')
        if sim.lower() == 'да':
            chars += punctuation
            c += '*'
            break
        elif sim == 'нет':
            break
        else:
            print('введите да или нет')
            continue





    while True:
        y = input('Введите количество поролей')
        if is_value(y) == True:
            break
        else:
            print('а может быть вы введете нормально число')
            continue



    for i in range(int(y)):
        for u in range(int(len)):
                res += random.choice(chars)
        print(res)
        res = ''
    if int(y) == i + 1:
        x = input('хотите ли вы еще сгенерировать пароли?')
        if x == 'да':
            c += '1'
            continue
        elif x == 'нет':
            break
        else:
            print('введите да или нет')
            continue