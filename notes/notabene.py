def summary():
    """
        "Talk is cheap. Show me the code." (с) Linus Torvalds"

    Интерактивный Python конспект заинтересовавших меня конструкций, функций, с описаниями. Сделан для личного
    использования, запоминания. Буду рад, если кому-то пригодится. Let's make the world a better place to live.

    1. При запуске конспекта - в консоль выведется оглавление. Расположено в конце кода. Сохраните вывод в отдельный
       файл, если необходимо. Так же можно поступать и с отдельными функциями, вместе с блоком запуска.

    2. После каждой функции - блок запуска, снимайте комментарии с нужных строк, ставьте на ненужные.
       Это основной принцип работы с данным конспектом.

    3. В описаниях функций есть ссылки на источники.

    4. Конспект дополняется.

    5. В некоторых случаях названия сохранены как в источнике, импорты сделаны перед функциями или внутри,
       для полноты контекста. Поэтому PEP 8 вполне может ругаться.
    """
    pass


def filter_tpl(it, key=None):
    """
    Функция типа lambda как фильтр, список фильтров помещен в кортеж, для демострации
    возможности подобного.

    https://stepik.org/lesson/567059/step/8

    полный конспект темы:
    https://github.com/yeralexey/Study/blob/master/notabene.py
    """
    if key is None:       # если функция вызвана без передачи lambda фильтра
        return tuple(it)  # вернуть кортеж из данных в параметре it
    res = ()              # объявляем пустой кортеж
    for x in it:          # для каждого элемента объекта из параметра it
        if key(x):        # если lambda в параметре key возвращает True
            res += (x,)   # новый кортеж из старого сложенный с данным элементом
    return res


filt = (lambda y: y < 0,         # для y в lambda, если y меньше ноля...
        lambda y: y >= 0,
        lambda y: 3 <= y <= 5)


# help(filter_tpl)
# inpt = '5 4 -3 4 5 -24 -6 9 0'
# inpt = [int(i) for i in inpt.split()]
# print(*filter_tpl(inpt))
# print(*filter_tpl(inpt, key=filt[0]))
# print(*filter_tpl(inpt, key=filt[1]))
# print(*filter_tpl(inpt, key=filt[2]))


def input_while_q():
    """
    Пример использования итератора c дополнительным параметром sentinel. "Пока пользователь не введет 'q'".
    Решение задачи для вывода количества уникальных вводов пользователя.

    https://stepik.org/lesson/567049/step/9

    полный конспект темы:
    https://github.com/yeralexey/Study/blob/master/notabene.py
    """
    print(len(set(iter(input, 'q'))))


# help(input_while_q)
# input_while_q()


def show_sorted(func):
    """
    Пример декоратора с использованием вложенной lambda функции, взято из задачи
    по созданию декоратора для возрата отсортированного списка, решение
    by @Алекс_Глозман.

    https://stepik.org/lesson/567062/step/4

    полный конспект темы:
    https://github.com/yeralexey/Study/blob/master/notabene.py
    """
    return lambda *args, **kwards: sorted(func(*args, **kwards))


@show_sorted
def get_list(s):
    return list(map(int, s.split()))


# help(show_sorted)
# print(*get_list("8 11 -5 4 3 10"))


def open_close_file():
    """
    Конструкция для работы с файлом, максимально учитывающая безопасность
    работы с данными от Сергея Балакирева.

    https://youtu.be/tM5qE8YLLuo

    полный конспект темы:
    https://github.com/yeralexey/Study/blob/master/notabene.py
    """
    try:
        with open("my_file.txt", encoding="utf-8") as file:  # открытие на чтение, или...
            s = file.readlines()                             # чтение построчно, или...
            int(s)                                           # имитация ошибки
    except FileNotFoundError:                                # обработка изключения "файл не найден"
        print("Невозможно открыть файл")
    except:
        print("Ошибка при работе с файлом")


# help(open_close_file)
# open_close_file()


def lambda_input():
    """
    Получение ввода функцией lambda c одновременным присвоением значения переменной a. В данной lambda
    происходит генерация кубов модулей чисел в диапазоне от -a < -a+4 с последующим выводном в
    консоль. Присвоение происходит в дополнительных скобках к lambda, сама lambda тоже в них. Т.е. общая форма:
    (lambda a: <do smth with a>)(<this is a>). Решение by
    @Irina_I

    https://stepik.org/lesson/567071/step/7

    полный конспект темы:
    https://github.com/yeralexey/Study/blob/master/notabene.py
    """
    (lambda a: print(*(abs(x) ** 3 for x in range(-a, -a + 4))))(int(input()))


# help(lambda_input)
# lambda_input()


def gen_lowercase():
    """
    Генерация последователности сочетаний букв из ascii_lowercase, с выводом пятидесяти из них в консоль. На основании
    решения выше.

    https://stepik.org/lesson/567071/step/8

    полный конспект темы:
    https://github.com/yeralexey/Study/blob/master/notabene.py
    """
    from string import ascii_lowercase
    (lambda a: [print(next(a), end=" ") for _ in range(50)])(i + j for i in ascii_lowercase for j in ascii_lowercase)


# help(gen_lowercase)
# gen_lowercase()


def sorted_sort_exaple():
    """
    Функция демонстрирует весь процесс преобразования данных методом .sort() и функцией sorted().
    Если раскомментированы тестовый ввод и выводы данных и закомментирован ввод с клавиатуры
    - виден процесс преобразования, сохраняет и выводит текст traceback.

    https://stepik.org/lesson/567076/step/3

    полный конспект темы:
    https://github.com/yeralexey/Study/blob/master/notabene.py
    """
    import traceback  # https://docs.python.org/3/library/traceback.html?highlight=traceback#module-traceback

    s = "-2 -1 8 11 4 5"                 # тестовый ввод
    # s = input()                          # ввод с клавиатуры

    lst = [int(i) for i in s.split()]       # генерация списка чисел
    tp_lst = tuple(lst)                     # преобразование в кортеж

    print(s)                 # введенные данные
    print(lst)               # тестовый вывод до
    print(tp_lst)            # тестовый вывод после

    def sortanyway(array):
        try:
            array.sort()
            print("Сейчас был использован метод .sort")
            return array
        except AttributeError:
            print(f"сработало исключение, и будет использована функция sorted(). \nошибка:\n{traceback.format_exc()} ")
            t_lst = sorted(array)

            return t_lst

    lst = sortanyway(lst)
    print(lst)               # тестовый вывод после

    tp_lst = tuple(sortanyway(tp_lst))
    print(tp_lst)            # тестовый вывод после


# help(sorted_sort_exaple)
# sorted_sort_exaple()


def mask_sort():
    """
    Пример сортирвки маской, на основании задания

    https://stepik.org/lesson/567077/step/6

    полный конспект темы:
    https://github.com/yeralexey/Study/blob/master/notabene.py
    """
    lst_in = ['Атос=лейтенант', 'Портос=прапорщик', "д'Артаньян=капитан",
              'Арамис=лейтенант', 'Балакирев=рядовой']        # тестовый ввод
    mask = ['рядовой', 'сержант', 'старшина', 'прапорщик', 'лейтенант',
            'капитан', 'майор', 'подполковник', 'полковник']  # маска, при обращении к которой возвращается индекс
    lst = [i.split("=") for i in lst_in]      # формируем список согласно задания
    lst.sort(key=lambda x: mask.index(x[1]))  # обращаемся к маске, получаем индекс значимости для сортировки
    return lst


# help(mask_sort)
# print(mask_sort())


def speed_limit_if_else_example(speed, speed_limit):
    """
    Функция для определения штрафа за превышение скорости с использованием условных операторов if-else. Демонстрирует
    классический подход в решении задач с множественными условиями. В следующей после данной функции приведен пример
    решения этой же задачи без использования if-else вообще.

    Args:
        speed (int): Скорость автомобиля.
        speed_limit (int): Ограничение скорости.

    Returns:
        int/str: Возвращает величину штрафа в случае превышения скорости или строку "it's ok", если скорость допустима.

    полный конспект темы:
    https://github.com/yeralexey/Study/blob/master/notabene.py
    """

    if speed_limit < speed <= speed_limit + 10:
        fee = 100
    elif speed_limit + 10 < speed <= speed_limit + 20:
        fee = 200
    elif speed_limit + 20 < speed:
        fee = 500
    else:
        fee = "it's ok"

    return fee


# help(speed_limit_if_else_example)
# print(speed_limit_if_else_example(speed=150, speed_limit=120))


def speed_limit_no_if_else_example(speed, speed_limit):
    """
    Функция для определения штрафа за превышение скорости без условных операторов if-else,
    используя словарь в качестве условий. Подобный подход встречаетмя в объектно-ориентированном программировании.
    Иногда можно столкнуться с тем, что в требованиях к коду прописано обязательное условие о том, что конструкции
    if-else не допустимы к применению.

    Логика приведенной конструкции в том, что условие используется в качестве ключа к словарю,
    и при внесении в словарь принимает булево значение True или False. Все дублирующиеся ключи перезаписываются
    поверх предыдущих, в результате остается словарь всего из двух элементов, с ключами True и False, далее происходит
    обращение к значению элемента с ключом True и его возврат.


    Args:
        speed (int): Скорость автомобиля.
        speed_limit (int): Ограничение скорости.

    Returns:
        int/str: Возвращает величину штрафа в случае превышения скорости или строку "it's ok", если скорость допустима.

    полный конспект темы:
    https://github.com/yeralexey/Study/blob/master/notabene.py
    """

    rule_condition = {
        speed < speed_limit: "it's ok",
        speed_limit < speed <= speed_limit + 10: 100,
        speed_limit + 10 < speed <= speed_limit + 20: 200,
        speed_limit + 20 < speed: 500
    }
    return rule_condition[True]


# help(speed_limit_no_if_else_example)
# print(speed_limit_no_if_else_example(speed=150, speed_limit=120))



# Оглавление

help(summary)

help(filter_tpl)
help(input_while_q)
help(show_sorted)
help(open_close_file)
help(lambda_input)
help(gen_lowercase)
help(sorted_sort_exaple)
help(mask_sort)
help(speed_limit_if_else_example)
help(speed_limit_no_if_else_example)
