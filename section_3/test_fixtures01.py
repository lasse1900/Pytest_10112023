import pytest


@pytest.fixture()
def setup_list():
    print("\n In Fixtures DEBUG... \n")
    city = ['New York', 'London', 'Riyadh', 'Singapore', 'Mumbai' ]
    return city

def test_getItem(setup_list):
    print(setup_list[1:3])
    print("Debug print --------------------------------------")
    assert setup_list[0] == 'New York'
    assert setup_list[::2] == ['New York', 'Riyadh', 'Mumbai']

def myReverse(lst):
    lst.reverse()
    return lst

def test_reverseList(setup_list):
    print(setup_list[::-2])
    assert setup_list[::-2] == ['Mumbai', 'Riyadh', 'New York']
    assert setup_list[::-1] == myReverse(setup_list)