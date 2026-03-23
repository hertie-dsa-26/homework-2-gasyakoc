import math

import pytest

from circle import Circle


def test_circle_perimeter_with_radius_one():
    circle = Circle(radius=1)
    assert circle.perimeter() == pytest.approx(2 * math.pi)


def test_circle_perimeter_with_radius_zero():
    circle = Circle(radius=0)
    assert circle.perimeter() == pytest.approx(0)


def test_circle_area_with_radius_one():
    circle = Circle(radius=1)
    assert circle.area() == pytest.approx(math.pi)


def test_circle_area_with_decimal_radius():
    circle = Circle(radius=2.5)
    assert circle.area() == pytest.approx(math.pi * (2.5 ** 2))
