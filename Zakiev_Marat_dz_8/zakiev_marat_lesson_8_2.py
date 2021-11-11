# zakiev_marat_lesson_8_2

# 2. * (вместо 1) Написать регулярное выражение для парсинга файла логов web-сервера из ДЗ 6 урока nginx_logs.txt
# (https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs)
# для получения информации вида:
# (<remote_addr>, <request_datetime>, <request_type>, <requested_resource>, <response_code>, <response_size>),
# например:
# raw = '188.138.60.101 - - [17/May/2015:08:05:49 +0000] "GET /downloads/product_2 HTTP/1.1" 304 0 "-"
# "Debian APT-HTTP/1.3 (0.9.7.9)"'
# parsed_raw = ('188.138.60.101', '17/May/2015:08:05:49 +0000', 'GET', '/downloads/product_2', '304', '0')
# Примечание: вы ограничились одной строкой или проверили на всех записях лога в файле? Были ли особенные строки?
# Можно ли для них уточнить регулярное выражение?
import re


# func reg_ex_parse
def reg_ex_parse(input_str: str) -> tuple:
    """
    Function get string from log and return tuple <remote_addr>, <request_datetime>,
     <request_type>, <requested_resource>, <response_code>, <response_size>
    :param input_str: string from log
    :return: tuple
    """
    re_ip_addr = r'^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|[a-f0-9]{0,4}:{1,2}[a-z0-9]{0,4}:{1,2}[a-z0-9]{0,4}:{1,2}' \
                 r'[a-z0-9]{0,4}:{1,2}[a-f0-9]{0,4}:{1,2}[a-z0-9]{0,4}:{1,2}[a-z0-9]{0,4}:{1,2}[a-z0-9]{0,4}.*?)\s'
    remote_addr = re.findall(re_ip_addr, input_str)
    re_request_datetime = r'\s\[(\d+/[A-Z]\w+/\d{4}:\d{2}:\d{2}:\d{2}\s\+\d+)\]\s'
    request_datetime = re.findall(re_request_datetime, input_str)
    re_request_type = r'\s\"([A-Z]{3,})\s'
    request_type = re.findall(re_request_type, input_str)
    re_requested_resource = r'\s(\/\w+[\/\w+]*)\s'
    requested_resource = re.findall(re_requested_resource, input_str)
    re_response_code = r'"\s(\d{3})\s\d+ "'
    response_code = re.findall(re_response_code, input_str)
    re_response_size = r'"\s\d{3}\s(\d+)\s"'
    response_size = re.findall(re_response_size, input_str)
    output_list = remote_addr + request_datetime + request_type + requested_resource + response_code + response_size
    output_tuple = tuple(output_list)
    return output_tuple


# ############################################################################################################

if __name__ == '__main__':
    # ----------------------- file -----------------------
    with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
        remote_addr_dict = {}
        for line in f:
            # print(line)
            print(reg_ex_parse(line))
    # ----------------------- file -----------------------
# #
