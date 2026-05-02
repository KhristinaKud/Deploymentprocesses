from main import add, sub, mul, div, print_hi


def test_add():
    assert add(2, 3) == 5


def test_sub():
    assert sub(10, 5) == 5


def test_mul():
    assert mul(2, 4) == 8


def test_div():
    assert div(10, 2) == 5


def test_print_hi(capsys):
    print_hi("Python")
    captured = capsys.readouterr()
    assert "Hi, Python" in captured.out
