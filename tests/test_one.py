import pytest
from main import checking

fixture = ['(((([{}]))))', '[([])((([[[]]])))]{()}', '{{[()]}}']
fixture_ = ["}{}", "{{[(])]}}", "[[{())}]]", '(}{))))']


@pytest.mark.parametrize('a', fixture)
def test_checking(a):
    check = checking(a)
    assert check == "Cбалансированно"


@pytest.mark.parametrize('a', fixture_)
def test_checking_(a):
    check = checking(a)
    assert check == "Несбалансированно"
