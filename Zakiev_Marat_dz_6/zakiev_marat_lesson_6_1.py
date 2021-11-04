# zakiev_marat_lesson_6_1

# nginx_logs.txt

# 1. Не используя библиотеки для парсинга, распарсить (получить определённые данные) файл логов web-сервера
# nginx_logs.txt (https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs)
# — получить список кортежей вида:
# (<remote_addr>, <request_type>, <requested_resource>).
# Например:
# [
#     ...
#     ('141.138.90.60', 'GET', '/downloads/product_2'),
#     ('141.138.90.60', 'GET', '/downloads/product_2'),
#     ('173.255.199.22', 'GET', '/downloads/product_2'),
#     ...
# ]

# ---------------------------------------------------------------------------


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
        lines_output = list()
        for line in f:
            # чтение из файла построчно
            line_output = [(read_lines(line))]
            lines_output += line_output
        for i in lines_output:
            print(i)
    # ----------------------- file -----------------------
#
