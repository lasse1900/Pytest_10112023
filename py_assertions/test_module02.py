
def test_a1():
    assert 4 != 3

def test_a2():
    assert True

def test_a3():
    assert "abcd" == 'abcd'

def test_a4():
    assert ((3-1)*4/2)  == 4.0

def test_a5():
    assert 1 in divmod(9,5) # tuple, can't edit
    assert 4 in divmod(9,5) # tuple, can't edit
    assert 'pyt' in 'this is abot pytest'
    assert 'pi' not in 'this is abot pytest'
    assert 1 in [1,2,4]
    assert [1,2] < [1,2,4]
    assert [1,2,4] == [1,2,4]
