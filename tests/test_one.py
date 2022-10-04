import pytest
from main import checking
from main import Stack

fixture = ['(((([{}]))))', '[([])((([[[]]])))]{()}', '{{[()]}}']
fixture_ = ["}{}", "{{[(])]}}", "[[{())}]]", '(}{))))']


@pytest.mark.parametrize('a', fixture)
def test_checking(a):
    brackets = Stack(a)
    check = checking(brackets)
    assert check == "Cбалансированно"


@pytest.mark.parametrize('a', fixture_)
def test_checking_(a):
    brackets = Stack(a)
    check = checking(brackets)
    assert check == "Несбалансированно"
