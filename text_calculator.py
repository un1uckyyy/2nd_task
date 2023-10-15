namesOfDigits = {"один": "1", "два": "2", "три": "3", "четыре": "4", "пять": "5", "шесть": "6", "семь": "7",
                 "восемь": "8", "девять": "9", "десять": "10", "одиннадцать": "11", "двенадцать": "12",
                 "тринадцать": "13", "четырнадцать": "14", "пятнадцать": "15", "шестнадцать": "16", "семнадцать": "17",
                 "восемнадцать": "18", "девятнадцать": "19", "двадцать": "20", "тридцать": "30", "сорок": "40",
                 "пятьдесят": "50", "шестьдесят": "60", "семьдесят": "70", "восемьдесят": "80", "девяносто": "90",
                 "сто": "100", "двести": "200", "триста": "300", "четыреста": "400", "пятьсот": "500",
                 "шестьсот": "600",
                 "семьсот": "700", "восемьсот": "800", "девятьсот": "900"}
namesOfOperations = {"плюс": "+", "минус": "-", "умножить": "*", "разделить": "/",
                     'открывается': "(", "закрывается": ")"}


def parser(string):  # функция перебирает ключи из словаря operations и ищет совпадающие элементы в введенной строке
    elements_array = []
    local_var = ''
    for el in string.split():
        if el == 'на' or el == 'скобка':
            continue
        elif el in namesOfOperations:
            if local_var != '':
                elements_array.append(local_var)
            local_var = ''
            elements_array.append(el)
        elif el in namesOfDigits:
            local_var += el + ' '
        else:
            return False, '',
    if local_var != '':
        elements_array.append(local_var)
    return True, elements_array



def text_to_digit(text_array): # функция преобразует текстовое выражение, состоящее из нескольких слов, в число, записанное цифрами
    digits_array = []
    for op in text_array:
        if op in namesOfOperations:
            digits_array.append(namesOfOperations[op])
        else:
            local_var = 0
            for op1 in op.split():
                if op1 not in namesOfDigits: # если элемент не находится в словаре с числительными, то функция прерывается
                    return False, None
                local_var += int(namesOfDigits[op1])
            digits_array.append(str(local_var))
    return True, digits_array


def digit_to_text(num): # функция, которая преобразует число в текст
    ans_array = []
    if num == 0:
        return 'ноль'
    while num != 0:
        head_order = str(num // int('1' + '0' * (len(str(num)) - 1))) + '0' * (len(str(num)) - 1) # старший разряд
        if head_order == '10' and len(str(num)) == 2: # если старший разряд 10, то это число от 10 до 19, они пишутся одним словом
            head_order = str(num)
            num = 0
        for k, v in namesOfDigits.items():
            if v == head_order: # находим текстовое представление старшего разряда
                ans_array.append(k)
                break
        num %= int('1' + '0' * (len(str(num)) - 1))
    return ' '.join(ans_array)


def calc(input_string):
    flag, text_operands = parser(input_string) # функция возвращает flag корректности выполнения
    # массив из текстовых операндов и операций
    if not flag:
        return "Некорректный ввод!"

    flag, digit_operands = text_to_digit(text_operands) # функция преобразует массив текстовых операндов в числовые
    if not flag:
        return 'Некорректный ввод!'

    digit_notion = eval(' '.join(digit_operands)) # встроенная функция eval вычисляет значение арифметического выражения
    minus = ''
    if digit_notion < 0:
        minus = "минус "
        digit_notion = abs(digit_notion)

    text_notion = digit_to_text(int(digit_notion))

    return minus + text_notion


print(calc('двадцать четыре плюс тринадцать умножить на скобка открывается два минус восемь умножить на три скобка закрывается плюс двести шестьдесят один'))
