import requests
from datetime import datetime

def get_data(url):

    """ Функция, которая получает данные со списком операций клиента из файла json
    и обрабатывает возможные ошибки"""

    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json(), "Данные получены успешно!"
        return None, f'WARNING:{response.status_code} Ошибка при получении данных.'
    except requests.exceptions.ConnectionError:
        return None, f"ERROR: requests.exceptions.ConnectionError"


def get_filtered_data(data, filtered_empty_from=False):

    """Функция, которая оставляет только операции со статусом EXECUTED и обрабатывает поле from"""

    data = [x for x in data if "state" in x and x['state'] == "EXECUTED"]
    if filtered_empty_from:
        data = [x for x in data if "from" in x]
    return data


def get_last_data(data, count_last_values):

    """Функция, которая получает 5 выполненных (EXECUTED) операций"""

    data = sorted(data, key=lambda x: x['date'], reverse=True)
    return data[:count_last_values]

def get_formatted_data(data):

    """Функция, которая ваводит данные в указанном формате:
     <дата перевода> <описание перевода>
    <откуда> -> <куда>
    <сумма перевода> <валюта>"""

    formatted_data = []
    for row in data:
        date = datetime.strptime(row['date'], '%Y-%m-%dT%H:%M:%S.%f').strftime('%d.%m.%Y')
        description = row["description"]

        if "from" in row:
            sender = row["from"].split()
            sender_bill = sender.pop(-1)
            sender_bill = f"{sender_bill[:4]} {sender_bill[4:6]}** **** {sender_bill[-4:]}"
            sender_info = " ".join(sender)
        else:
            sender_bill, sender_info = '', '[ИНФОРМАЦИЯ ОТСУТСТВУЕТ]'

        recipient = f"**{row['to'][-4:]}"
        amount = f'{row["operationAmount"]["amount"]} {row["operationAmount"]["currency"]["name"]}'
        formatted_data.append(f"""\n
{date} {description}
{sender_info} {sender_bill} -> Счет {recipient}
{amount}""")
    return formatted_data





