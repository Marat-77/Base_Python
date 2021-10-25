# zakiev_marat_lesson_3_5
#
# 5. Реализовать функцию get_jokes(), возвращающую n шуток,
# сформированных из трех случайных слов,
# взятых из трёх списков (по одному из каждого):
# nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
# adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
# adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
#
# Например:
# >>> get_jokes(2)
# ["лес завтра зеленый", "город вчера веселый"]
#
# Документировать код функции.
# Сможете ли вы добавить еще один аргумент — флаг,
# разрешающий или запрещающий повторы слов в шутках
# (когда каждое слово можно использовать только в одной шутке)?
# Сможете ли вы сделать аргументы именованными?

# ################# import #####################
from random import choice
from random import sample


# ------------------functions------------------
def input_number():
    """
    Function return integer from user input
    :return: int
    """
    # проверка введенных данных
    # -------------------------------------------------------------
    str_jokes = ''
    while not str_jokes.isdigit():
        str_jokes = input('Введите количество шуток (от 1 до 5): ')
    num_jokes = int(str_jokes)
    if num_jokes in range(1, 5):
        n_jokes = num_jokes
    else:
        n_jokes = 5
    return n_jokes
    # -------------------------------------------------------------


def get_jokes(n: int):
    """
    Function get number and return n*jokes
    :param n: int
    :return: print str
    """
    print(f'----- get_jokes ----- n = {n}')
    nouns = ['автомобиль', 'лес', 'огонь', 'город', 'дом']
    adverbs = ['сегодня', 'вчера', 'завтра', 'позавчера', 'ночью']
    adjectives = ['веселый', 'яркий', 'зеленый', 'утопичный', 'мягкий']
    for i in range(n):
        fanny = f'"{choice(nouns)} {choice(adverbs)} {choice(adjectives)}"'
        print(fanny,  end=' ')
    print()
    print('-' * 80)


def get_jokes_zip(n):
    """
    Function get number and return n*jokes
    :param n: int
    :return: print list
    """
    print(f'----- get_jokes_zip ----- n = {n}')
    nouns = ['автомобиль', 'лес', 'огонь', 'город', 'дом']
    adverbs = ['сегодня', 'вчера', 'завтра', 'позавчера', 'ночью']
    adjectives = ['веселый', 'яркий', 'зеленый', 'утопичный', 'мягкий']
    # zip ?????????????????????????????????????????????????????????????????
    sample_nouns = sample(nouns, n)
    sample_adverbs = sample(adverbs, n)
    sample_adjectives = sample(adjectives, n)
    x = zip(sample_nouns, sample_adverbs, sample_adjectives)
    print(list(x))
    print('-' * 80)


def main():
    while True:
        print('\n----- основное меню: -----')
        user_choice = input(
            '1 - слова в шутках могут повторяться\n2 - слова в шутках не повторяются\n0 - Выход\nВведите: '
        )
        print(f'\nВы выбрали: {user_choice}')
        if user_choice == '1':
            print('слова в шутках могут повторяться')
            num = input_number()
            get_jokes(num)
        elif user_choice == '2':
            print('слова в шутках не повторяются')
            num = input_number()
            get_jokes_zip(num)
        elif user_choice == '0':
            print('Вы вышли из программы')
            break
        else:
            print(f'Вы ввели: {user_choice} - в этом меню не используется')


if __name__ == '__main__':
    main()

# думаю, что здесь надо было каким-то образом использовать sample (из random),
# но я так и не придумал как сделать перебор,
# чтоб каждый элемент sample(nouns, n) + sample(adverbs, n) + sample(adjectives, n) собрался соответственно
# можно конечно все это сделать с помощью if и проверять каждый раз повтор/не_повтор,
# но думаю что-то можно другое использовать (map/zip...), но не придумал как их тут использовать...

# P.S.: В итоге что-то придумал с sample и zip, но надо с этим еще разбираться...
