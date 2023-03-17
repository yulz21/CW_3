import pytest

@pytest.fixture
def test_data():
    return [
    {'id': 441945886, 'state': 'EXECUTED', 'date': '2018-08-26T10:50:58.294041',
     'operationAmount': {'amount': '31957.58', 'currency': {'name': 'руб.', 'code': 'RUB'}},
     'description': 'Перевод организации', 'from': 'Maestro 1596837868705199', 'to': 'Счет 64686473678894779589'},
    {'id': 41428829, 'state': 'CANCELED', 'date': '2017-07-03T18:35:29.512364',
     'operationAmount': {'amount': '8221.37', 'currency': {'name': 'USD', 'code': 'USD'}},
     'description': 'Перевод организации', 'from': 'MasterCard 7158300734726758', 'to': 'Счет 35383033474447895560'},
    {'id': 939719570, 'date': '2018-06-30T02:08:58.425572',
     'operationAmount': {'amount': '9824.07', 'currency': {'name': 'USD', 'code': 'USD'}},
     'description': 'Перевод организации', 'from': 'Счет 75106830613657916952', 'to': 'Счет 11776614605963066702'},
    {'id': 587085106, 'state': 'EXECUTED', 'date': '2018-09-23T10:45:06.972075',
     'operationAmount': {'amount': '48223.05', 'currency': {'name': 'руб.', 'code': 'RUB'}},
     'description': 'Открытие вклада', 'to': 'Счет 41421565395219882431'}
    ]


