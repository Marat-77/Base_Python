# zakiev_marat_lesson_5_3.py

# 3. Есть два списка:
# tutors = [
#     'Иван', 'Анастасия', 'Петр', 'Сергей',
#     'Дмитрий', 'Борис', 'Елена'
# ]
# klasses = [
#     '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
# ]
# Необходимо реализовать генератор, возвращающий кортежи вида (<tutor>, <klass>), например:
# ('Иван', '9А')
# ('Анастасия', '7В')
# ...
# Количество генерируемых кортежей не должно быть больше длины списка tutors.
# Если в списке klasses меньше элементов, чем в списке tutors,
# необходимо вывести последние кортежи в виде: (<tutor>, None), например:
# ('Станислав', None)
# Доказать, что вы создали именно генератор. Проверить его работу вплоть до истощения.
# Подумать, в каких ситуациях генератор даст эффект.


def main():
    tutors = [
        'Иван', 'Анастасия', 'Петр', 'Сергей',
        'Дмитрий', 'Борис', 'Елена', 'Станислав', 'Василий'
    ]
    klasses = [
        '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
    ]
    len_tutors = len(tutors)
    num_klasses = len(klasses) - 1

    # gen_tuple_tutor_klasses
    def gen_tuple_tutor_klasses():
        """
        Function of generator
        :return:
        """
        # Количество генерируемых кортежей не должно быть больше длины списка tutors:
        for i in range(0, len_tutors):
            if i > num_klasses:
                # Если в списке klasses меньше элементов, чем в списке tutors,
                # необходимо вывести последние кортежи в виде: (<tutor>, None)
                tuple_tutors_klasses = (tutors[i], None)
            else:
                tuple_tutors_klasses = (tutors[i], klasses[i])
            yield tuple_tutors_klasses

    gen_tutors = gen_tuple_tutor_klasses()

    # Доказать, что вы создали именно генератор:
    print(f'type of gen_tutors: {type(gen_tutors)}')  # type of gen_tutors: <class 'generator'>

    for g in gen_tutors:
        print(g)

    # Проверить его работу вплоть до истощения:
    # # ----------------------------------------------------------- print next --------------------------
    # print('print next gen_tutors:')
    # print(f'next 1:{next(gen_tutors)}')  # 1 => next 1:('Иван', '9А')
    # print(f'next 2:{next(gen_tutors)}')  # 2 =>next 2:('Анастасия', '7В')
    # print(f'next 3:{next(gen_tutors)}')  # 3 => next 3:('Петр', '9Б')
    # print(f'next 4:{next(gen_tutors)}')  # 4 => next 4:('Сергей', '9В')
    # print(f'next 5:{next(gen_tutors)}')  # 5 => next 5:('Дмитрий', '8Б')
    # print(f'next 6:{next(gen_tutors)}')  # 6 => next 6:('Борис', '10А')
    # print(f'next 7:{next(gen_tutors)}')  # 7 => next 7:('Елена', '10Б')
    # print(f'next 8:{next(gen_tutors)}')  # 8 => next 8:('Станислав', '9А')
    # print(f'next 9:{next(gen_tutors)}')  # 9 => next 9:('Василий', None)
    # # print(f'next 10:{next(gen_tutors)}')  # 10 => StopIteration
    # # ----------------------------------------------------------- print next --------------------------


if __name__ == '__main__':
    main()

#
# well done!
