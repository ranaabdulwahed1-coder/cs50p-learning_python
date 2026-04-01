from plates import is_valid
def test_len():
    assert not is_valid('abcdefg')
    assert not is_valid('a')
def test_2():
    assert not is_valid("11")
    assert not is_valid("A1")
    assert not is_valid("AB.12")
    assert not is_valid("AB 12")
    assert not is_valid("AB!")
def test_zero():
    assert not is_valid('aj09')
    assert is_valid('aj12')
def test_LN():
    assert not is_valid('aj2aj')

