# /Zakiev_Marat_dz_9/zakiev_marat_lesson_9_1.py
# zakiev_marat_lesson_9_1

# -------------------------------------------------------------------------------------------
# 1. Создать класс TrafficLight (светофор).
# - определить у него один атрибут color (цвет) и метод running (запуск);
# - атрибут реализовать как приватный;
# - в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
# - продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды,
# третьего (зелёный) — на ваше усмотрение;
# - переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
# - проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов.
# При его нарушении выводить соответствующее сообщение и завершать скрипт.
# -------------------------------------------------------------------------------------------
#
from time import sleep
from time import localtime
from time import strftime


class TrafficLight:
    def __init__(self, name='Unknown'):
        self.name = name
        self.type = 'TrafficLight'
        self.__color = ('red', 'yellow', 'green')

    # def print_current_mode(self, current_mode, control, t_):
    #     # ######################################################
    #     # сделать функцию( current_mode, control, t_ )
    #     if current_mode != control:
    #         print(f'светофор {self.name} неисправен')
    #         alarm = True
    #         return alarm
    #         # break
    #     else:
    #         print(current_mode, t_)
    #         sleep(t_)
    #     # ######################################################

    def running(self):
        status = 'working'
        timers = (7, 2, 5)  # таймеры для каждого цвета
        count = 0  # счетчик циклов while True
        max_count = 3  # для досрочного окончания бесконечного цикла while True -----------------------!
        control_tuple = ('red', 'yellow', 'green')  # контрольный образец
        control = None
        i_control = 0
        alarm = False
        while True:
            if alarm is True:
                print(f'светофор "{self.name}" неисправен')
                break
            print(f'\nсветофор "{self.name}". состояние: {status}')
            # print(f'count={count}')
            for color, t_ in zip(self.__color, timers):
                current_mode = color
                # Задачу можно усложнить, реализовав проверку порядка режимов.
                # При его нарушении выводить соответствующее сообщение и завершать скрипт.
                if control is None:
                    control = control_tuple[i_control]
                    # ######################################################
                    # self.print_current_mode(current_mode, control, t_)
                    # сделать функцию( current_mode, control, t_ ) - не получается завершение - цикл продолжается
                    if current_mode != control:
                        print(f'неверный порядок сигналов светофора "{self.name}"')
                        alarm = True
                        break
                    else:
                        print(current_mode, t_)
                        sleep(t_)
                    # ######################################################
                    # if alarm is True:
                    #     print(f'2.1 неверный порядок сигналов светофора {self.name}')
                    #     break
                elif control is not None:
                    i_control += 1
                    if i_control == len(control_tuple):
                        i_control = 0
                    control = control_tuple[i_control]
                    # ######################################################
                    # self.print_current_mode(current_mode, control, t_)
                    if current_mode != control:
                        print(f'неверный порядок сигналов светофора "{self.name}"')
                        alarm = True
                        break
                    else:
                        print(current_mode, t_)
                        sleep(t_)
                    # ######################################################
                    # if alarm is True:
                    #     print(f'2.2 неверный порядок сигналов светофора {self.name}')
                    #     break
                #
            count += 1
            if count == max_count:
                break  # ------------------------------------------------------------------------------!
        #

    def schedule_running(self, work_start: int = 8, work_end: int = 21):
        status = 'working'
        # work_start - время начала работы светофора по умолчанию = 08:00
        # work_end - время окончания работы светофора по умолчанию = 21:00
        timers = (7, 2, 5)  # таймеры для каждого цвета
        emulation_time = True  # True - эмулятор текущего часа включен, False -  выключен
        emulate_hour = 19  # эмуляция текущего часа  ----------------------------------------------
        if emulation_time is True:
            hour_now = emulate_hour
            print('Emulation')
        else:
            hour_now = int(strftime('%H', localtime()))  # =========== realtime
        while hour_now in range(work_start, work_end):
            print(f'\nсветофор "{self.name}". состояние: {status}')
            print(f'время работы с {work_start} час. до {work_end} час.')
            print(f'сейчас {hour_now} час.')
            for color, t_ in zip(self.__color, timers):
                current_mode = color
                print(current_mode, t_)
                sleep(t_)
            if emulation_time is True:
                hour_now += 1  # для эмуляции текущего времени  -----------------------------------
        #

    def __del__(self):
        status = 'stop'
        print(status)


#
tr_light = TrafficLight()
tr_light.running()
#
gorkogo_lenina = TrafficLight('перекресток Горького - Ленина')
gorkogo_lenina.running()
#
tr_new = TrafficLight('Новый')
tr_new.schedule_running(10, 22)  # запуск светофора, работающего по расписанию с 10:00 до 20:00
#
#
