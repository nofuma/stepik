import math
def encrypt(res, rot):
    for i in text:
        if i == '!' or i == ',' or i == '?' or i =='.' or i == ' ':
            res += i
            continue
        if answer == 'да':
            if language == 'да':


                if i in rusLower:
                   ind = (rusLower.find(i) + rot) % 32
                   res += rusLower[ind]
                if i in rusUpper:
                    ind = (rusUpper.find(i) + rot) % 32
                    res += rusUpper[ind]
            else:
                if i in engLower:
                    ind = (engLower.find(i) + rot) % 26
                    res += engLower[ind]
                if i in engUpper:
                    ind = (engUpper.find(i) + rot) % 26
                    res += engUpper[ind]

        elif answer == 'нет':
            if language == 'да':


                if i in rusLower:
                   ind = (rusLower.find(i) - rot) % 32
                   res += rusLower[ind]
                if i in rusUpper:
                    ind = (rusUpper.find(i) - rot) % 32
                    res += rusUpper[ind]
            else:
                if i in engLower:
                    ind = (engLower.find(i) - rot) % 26
                    res += engLower[ind]
                if i in engUpper:
                    ind = (engUpper.find(i) - rot) % 26
                    res += engUpper[ind]
    print(res)






def isvalue(x):
    if x == 'да' or x == 'нет':
        return True



def is_value(x):
    if x.isdigit():
        return True


engLower = 'abcdefghijklmnopqrstuvwxyz'
engUpper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
rusLower = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
rusUpper = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
while True:
    while True:
        answer = input("текст надо разшифровать")
        if isvalue(answer) == True:
            break
    while True:
        text = input('Введите предложение для разшифровки')
        if text.isdigit() != True:
            break
    while True:
        language = input('этот текст на русском?')
        if isvalue(language) == True:
            break
    res = ''
    while True:
        rots = input('известен ли сдвиг')
        if isvalue(rots) == True:
            break
    if rots == 'да':
        while True:
            rot = input('какой должен быть сдвиг сдвиг')
            if is_value(rot) == True:
                break

    else:
        vord = int(input('до какого числа может быть сдвиг'))
        for i in range(vord):
            s = encrypt(res, i)
            guestion = input("это подходит")
            if guestion == "нет":
                continue
            else:
                break



    resh = encrypt(res, int(rot))
    break










