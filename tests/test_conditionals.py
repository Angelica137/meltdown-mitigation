from scripts.conditionals import *


def test_is_criticality_balanced_returns_true():
    assert is_criticality_balanced(750, 600) == True


def test_is_criticality_balanced_returns_false_product_fail():
    assert is_criticality_balanced(799, 700) == False


def test_is_criticality_balanced_returns_false_temp_fail():
    assert is_criticality_balanced(800, 600) == False


def test_reactor_efficiency_returns_orange():
    assert reactor_efficiency(200, 50, 15000) == 'orange'


def test_reactor_efficiency_returns_green():
    assert reactor_efficiency(200, 50, 10000) == 'green'


def test_reactor_efficiency_returns_red():
    assert reactor_efficiency(200, 50, 18000) == 'red'
