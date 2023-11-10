
def test_a1():
    assert 5 + 5 == 10
    assert 5 * 3 == 15

# This is a failing test
def test_a2():
    assert 10 - 9 == 1, "NOT failing test" 

def test_a3():
    assert 9//5 == 1 # integer truncation