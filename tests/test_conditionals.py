from scripts.conditionals import *


def test_is_criticality_balanced_returns_true():
    is_criticality_balanced(750, 600) == True


def test_is_criticality_balanced_returns_false_product_fail():
    is_criticality_balanced(799, 700) == False
