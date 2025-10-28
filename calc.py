print ('Калькулятор   ')
z = 1
try:
    z = int(input(' Введите количество действий целым числом :\n Если хотите проще то введите 0 :'))


except ValueError:
    print("Вы ввели что-то не так")
    exit()
import webbrowser
if z == 0:
    def validator(func):
        def wrapper(url):
            if "." in url:
                func(url)
            else:
                print("Неверный URL")

        return wrapper


    @validator
    def open_url(url):
        webbrowser.open(url)


    open_url("https://www.desmos.com/scientific?lang=ru")
else:
    i = 0
    r = 0
    try:
        if i == 0 :
            q = float(input('Введите первое число :'))
            w = float(input('Введите второе число :'))
            e = input('Введите знак :')
            i = i + 1
            if e =="-":
                 r = q - w
            elif e =="+":
                r = q + w
            elif e =="*":
                r = q * w
            elif e =="/":
                if w != 0:
                    r = q / w
                else:
                    print ('На ноль нельзя делить')
            elif e =="%":
                r = q % w
            elif e == "**":
                r = q ** w
            print (r)

            while i < z >= 1 :
                w = float(input('Введите следующее число :'))
                e = input('Введите знак :')
                i = i + 1
                if e == "-":
                    r = r - w
                elif e == "+":
                    r = r + w
                elif e == "*":
                    r = r * w
                elif e == "/":
                    if w != 0:
                        r = r / w
                    else:
                        print('На ноль нельзя делить')
                elif e == "%":
                    r = r % w
                elif e == "**":
                    r = r ** w
                print(r)

    except ZeroDivisionError:
        print("одуль не может быть 0")
    except ValueError:
        print("Вы ввели что-то не так")
