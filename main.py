# 1
res = 0 # результат

str = "-5-45/9+7-1+14/7+10*2-3*7"

list_plus = str.split("+") # списки со слагаемыми
for elem_plus in list_plus:
    if not elem_plus.isdigit():
        list_minus = elem_plus.split("-") # списки с вычитаемыми
        for elem_minus in range(len(list_minus)):
            if not list_minus[elem_minus].isdigit():
                list_mult = list_minus[elem_minus].split("*") # списки с множителями
                for elem_mult in range(len(list_mult)):
                    if not list_mult[elem_mult].isdigit():
                        list_div = list_mult[elem_mult].split("/") # списки с делимым и делителем
                        if list_mult[elem_mult] != "":
                            new_res2 = int(list_div[0])
                        for i in range(len(list_div)):
                            if i != 0: # деление
                                new_res2 = new_res2 / int(list_div[i])
                                if str.find(list_minus[elem_minus]) - 1 >= 0: # проверка на наличие минуса перед частным
                                    if str[str.find(list_minus[elem_minus]) - 1] == "-":
                                        res = res - new_res2
                                    else:
                                        res = res + new_res2
                                else:
                                    res = res + new_res2
                    else:
                        if elem_mult == 0: # умножение
                            new_res = int(list_mult[0])
                        elif elem_mult != 0:
                            new_res = new_res * int(list_mult[elem_mult])
                            if str.find(list_mult[elem_mult]) - 1 >= 0:  # проверка на наличие минуса перед произведением
                                if str[str.find(list_minus[elem_minus]) - 1] == "-":
                                    res = res - new_res
                                else:
                                    res = res + new_res
                            else:
                                res = res + new_res            
            else:
                if elem_plus.count("-") != 0 and elem_minus != 0:
                    res = res - int(list_minus[elem_minus]) # вычитание
                else:
                    res = res + int(list_minus[elem_minus])
    else:
        res = res + int(elem_plus) # сложение!
print(res)

# 2
#Задача 43: Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.
#Пример:
#[1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]