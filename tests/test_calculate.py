from calculator import calculate

def test_calculate():
    result = calculate("3", "-", "1")
    assert result == 2
