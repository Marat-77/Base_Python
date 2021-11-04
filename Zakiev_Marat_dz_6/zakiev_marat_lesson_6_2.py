# zakiev_marat_lesson_6_2

# draft_nginx_logs.txt
# получить список кортежей
# вида: (<remote_addr>, <request_type>, <requested_resource>).
# Например:
# [
#     ...
#     ('141.138.90.60', 'GET', '/downloads/product_2'),
#     ('141.138.90.60', 'GET', '/downloads/product_2'),
#     ('173.255.199.22', 'GET', '/downloads/product_2'),
#     ...
# ]
# ---------------------------------------------------------------------------
# 2. *(вместо 1)
# Найти IP адрес спамера и количество отправленных им запросов по данным файла логов из предыдущего задания.
# Примечание: спамер — это клиент, отправивший больше всех запросов; код должен работать даже с файлами,
# размер которых превышает объем ОЗУ компьютера.


def read_lines(input_line):
    output_list = []
    count_i = 0
    x = 0
    while count_i < 12:
        count_i += 1
        new_str = input_line[x:]
        find_space = new_str.find(' ')
        if count_i < 12:
            output_str = new_str[:find_space]
            x += find_space + 1
        else:
            output_str = input_line[x:]
            # последняя строчка - user_agent - оставил одной строкой (без разбивки по пробелам)
        i_list = [output_str]
        output_list += i_list
    remote_addr = output_list[0]
    # date_time = output_list[3].lstrip('[')  # при необходимости можно добавить в output_info
    # timezone = output_list[4].rstrip(']')  # при необходимости можно добавить в output_info
    # не стал пока заморачиваться с конвертацией date_time и timezone
    request_type = output_list[5].lstrip('"')
    requested_resource = output_list[6]
    # http_protocol = output_list[7].rstrip('"')  # при необходимости можно добавить в output_info
    # status_code = output_list[8]  # при необходимости можно добавить в output_info
    # user_agent = output_list[11]  # при необходимости можно добавить в output_info
    output_info = (remote_addr, request_type, requested_resource)
    return output_info


if __name__ == '__main__':
    # ----------------------- file -----------------------
    with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
        remote_addr_dict = {}
        for line in f:
            # чтение из файла построчно
            line_output = (read_lines(line))
            g_adr = line_output[0]
            if remote_addr_dict.get(g_adr) is None:
                remote_addr_dict[g_adr] = 1
            else:
                remote_addr_dict[g_adr] += 1
        max_value = max(remote_addr_dict.values())
        keys = remote_addr_dict.keys()
        for i in keys:
            if remote_addr_dict[i] == max_value:
                print(f'спамер: {i}: {max_value}')
    # ----------------------- file -----------------------
