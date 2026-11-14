from app import add_numbers, subtract_numbers


def test_add_numbers():
    assert add_numbers(10, 20) == 30


def test_subtract_numbers():
    assert subtract_numbers(20, 10) == 10


def test_add_negative_numbers():
    assert add_numbers(-5, -10) == -15
