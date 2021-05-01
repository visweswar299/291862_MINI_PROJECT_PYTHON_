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


def test_multiply_zero():
    output = calculator.multiply(10, 0)
    assert output == 0


def test_divide():
    output = calculator.divide(10, 5)
    assert output == 2


def test_divide_zero():
    output = calculator.divide(10, 0)
    assert output is None


def test_divide_():
    output = calculator.divide(0, 10)
    assert output == 0


def test_modulo():
    output = calculator.modulo(10, 5)
    assert output == 0


def test_modulo_zero():
    output = calculator.modulo(10, 0)
    assert output is None


def test_modulo_():
    output = calculator.modulo(0, 10)
    assert output == 0


def test_power():
    output = calculator.power(10, 5)
    assert output == 100000


def test_power_():
    output = calculator.power(0, 5)
    assert output == 0


def test_power_zero():
    output = calculator.power(10, 0)
    assert output == 1
