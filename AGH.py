import random


n = [2,3,4,6,7,8,9,10,11]*4
z = input("Готовы поиграть? \n y/n : ")
if z == 'n':
    print('Досвидания')
elif z == 'y':
    c = 0
    random.shuffle(n)
    m = n.pop()
    c = c + m
    m = n.pop()
    c = c + m
    if c == 21:
        print('You win')
        exit()
    while True:
        print('У вас сейчас ',c, 'очков')
        z  = input('\n Возьмете еще? y/n  :'  )
        if z == 'y':
            m = n.pop()
            print('Вам выпала карта номиналом',m)
            c = c + m

            if c >= 21:
                print('You lose')
                break
            elif c == 21:
                print('You win')
                break
else:
    print('Вы ввели что-то иное. До свидания ')

