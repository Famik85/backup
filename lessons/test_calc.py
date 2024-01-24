import pytest
import calc_func as c


def test_plus_positive():
    assert c.plus(4, 3) == 7


def test_minus_positive():
    assert c.minus(4, 3) == 1


def test_mult_positive():
    assert c.mult(4, 3) == 12


def test_divis_positive():
    assert c.divis(4, 2) == 2
