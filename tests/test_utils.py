from code.utils import get_data, get_last_data, get_filtered_data, get_formatted_data


def test_get_data():
    """
    Функция, котораая тестирует функцию get_data
    """
    assert len(get_data('/Users/juliazhukova/Desktop/PycharmProjects/COURSE_WORK_3/tests/test_operations.json')) == 5


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





