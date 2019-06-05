from inc import inc, dec

def test_inc():
    assert inc(3) == 4
    assert inc(5) == 6

def test_dec():
    assert dec(3) == 2
