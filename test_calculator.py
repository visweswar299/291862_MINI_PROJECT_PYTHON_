import calculator


def test_add():
    output = calculator.add(10, 5)
    assert output == 15


def test_subtract():
    output = calculator.subtract(10, -5)
    assert output == 15


def test_multiply():
    output = calculator.multiply(10, 5)
    assert output == 50


def test_divide():
    output = calculator.divide(10, 5)
    assert output == 2


def test_modulo():
    output = calculator.modulo(10, 5)
    assert output == 0


def test_power():
    output = calculator.power(10, 5)
    assert output == 100000