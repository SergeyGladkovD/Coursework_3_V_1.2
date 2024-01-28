from scripts.scripts import time_correct, five_items, get_to, get_from


def test_five_items():
	assert five_items([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) == [1, 2, 3, 4, 5]
	assert len(five_items([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])) == 5


def test_time_correct():
	assert time_correct("2019-08-26T10:50:58.294041") == '26-08-2019'


def test_get_from():
	assert get_from({"description": "Открытие вклада", "to": "Счет 41421565395219882431"}) == ''
	assert get_from({"description": "Перевод организации", "from": "Maestro 1596837868705199",
								"to": "Счет 64686473678894779589"}) == 'Maestro 1596 83** **** 5199'


def test_get_to():
	assert get_to({'to': '00000000000000000000'}) == '-> 00000**0000'
