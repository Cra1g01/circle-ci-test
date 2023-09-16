from main import add, sub


def test_add():
    assert add(1, 1) == 2
    assert add(2, -3) == -1
    assert add(5.5, 2) == 7.5


def test_sub():
    assert sub(10, 2) == 8
    assert sub(10, 20) == -10
    assert sub(-5, -5) == 0
