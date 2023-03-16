import pytest

from code.utils import get_data, get_last_data, get_filtered_data, get_formatted_data
from code.conftest import test_data


def test_get_data():
    """
    Функция, котораая тестирует функцию get_data
    """

    url = "https://file.notion.so/f/s/d22c7143-d55e-4f1d-aa98-e9b15e5e5efc/operations.json?spaceId=0771f0bb-b4cb-4a14-bc05-94cbd33fc70d&table=block&id=f11058ed-10ad-42ea-a13d-aad1945e5421&expirationTimestamp=1678992616942&signature=iMLCdLiDNDIsEKIz-rIzWhW-v9X53p11o1g3rNfRbX4&downloadName=operations.json"
    assert get_data(url) is not None
    url = "https://file.notion.so/f/s/d22c7143-d55e-4f1d-aa98-e9b15e5e5efc/operations.json?spaceId=0771f0bb-b4cb-4a14-bc05-94cbd33fc70d&table=block&id=f11058ed-10ad-42ea-a13d-aad1945e5421&expirationTimestamp=1678992616942&signature=iMLCdLiDNDIsEKIz-rIzWhW-v9X53p11o1g3rNfRbX4&downloadNam=operations.json"
    data, info = get_data(url)
    assert data is None
    assert info == 'WARNING:400 Ошибка при получении данных.'
    url = "https://fil.notion.so/f/s/d22c7143-d55e-4f1d-aa98-e9b15e5e5efc/operations.json?spaceId=0771f0bb-b4cb-4a14-bc05-94cbd33fc70d&table=block&id=f11058ed-10ad-42ea-a13d-aad1945e5421&expirationTimestamp=1678992616942&signature=iMLCdLiDNDIsEKIz-rIzWhW-v9X53p11o1g3rNfRbX4&downloadName=operations.json"
    data, info = get_data(url)
    assert data is None
    assert info == 'ERROR: requests.exceptions.ConnectionError'


def test_get_filtered_data(test_data):
    """
    Функция, котораая тестирует функцию get_filtered_data
    """
    assert len(get_filtered_data(test_data)) == 2
    assert len(get_filtered_data(test_data, filtered_empty_from=True)) == 1


def test_get_last_data(test_data):
    """
    Функция, котораая тестирует функцию get_last_data
    """

    data = get_last_data(test_data, count_last_values=3)
    assert data[0]['date'] == '2018-09-23T10:45:06.972075'
    assert len(data) == 3


def test_get_formatted_data(test_data):

    """
    Функция, котораая тестирует функцию get_last_data
    """
    data = get_formatted_data(test_data[:1])
    assert data == ['\n\n26.08.2018 Перевод организации\nMaestro 1596 83** **** 5199 -> Счет **9589\n31957.58 руб.']
    data = get_formatted_data(test_data[-1:])
    assert data == ['\n\n23.09.2018 Открытие вклада\n[ИНФОРМАЦИЯ ОТСУТСТВУЕТ]  -> Счет **2431\n48223.05 руб.']





