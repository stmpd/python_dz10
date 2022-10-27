from datetime import datetime as dt
from os.path import getsize


def save_record_to_log_file(data):

    right_ls_len = 3
    log_file_name = 'calclog.csv'

    data_header = ['Date', 'Time', 'Type operation', 'Source Data', 'Result']
    data_row = []

    if len(data) != right_ls_len:
        print(f'Количество параметров не равно {right_ls_len}!')
        return False
    try:
        with open(log_file_name, 'a', encoding='utf-8') as flog:
            if getsize(flog.name) == 0:

                flog.write(str(";".join(data_header) + '\n'))
            data_row.append(dt.now().strftime('%d.%m.%Y'))
            data_row.append(dt.now().strftime('%H:%M:%S'))
            for cur_param in data:
                if cur_param == '':
                    print(f'Один из параметров строки пуст. Строка: {data}')
                    return False
                data_row.append(cur_param)
            flog.write(str(";".join(data_row)) + '\n')
    except PermissionError:
        print('Доступ к файлу запрещён (возможно другой программой).')
        return False
    return True


ls = ['+', '2, 5', '10']
Status = save_record_to_log_file(ls)

if Status == True:
    print('Логгирование выполнено успешно!')
else:
    print('Логгирование НЕ выполнено!')