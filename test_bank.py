from bank import value
def test_hello():
    assert value('  hello   ') == 0
    assert value('hello there') == 0
def test_h():
    assert value('h') == 20
    assert value('hi') == 20
def test_other():
    assert value('wsp') == 100
    assert value('soup') == 100
    assert value('') == 100

