from calculator import calculate

def test_calculate():
    result = calculate("3", "-", "1")
    assert result == 2
    new_result = calculate("3", "+", "1")
    assert new_result == 4
    other_result = calculate("3", "/", "1")
    assert other_result == 3
