#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   test_pisingerpy.py
@Time    :   2026/02/10 12:47:10
@Author  :   Alejandro Marrero (amarrerd@ull.edu.es)
@Version :   1.0
@Contact :   amarrerd@ull.edu.es
@License :   (C)Copyright 2026, Alejandro Marrero
@Desc    :   None
"""

import numpy as np
import pytest

from pisingerpy import Knapsack, Solution, combo, expknap, minknap


@pytest.fixture
def default_instance():
    p = np.asarray(list(range(1, 101)))
    w = np.asarray(list(range(1, 101)))
    q = 50
    return Knapsack(p, w, q)


@pytest.fixture
def default_large_knap():
    rng = np.random.default_rng(seed=42)
    c = rng.integers(1e3, 1e5)
    w = rng.integers(1000, 5000, size=1000)
    p = rng.integers(1000, 5000, size=1000)
    kp = Knapsack(profits=p, weights=w, capacity=c)

    return kp


def test_combo(default_large_knap):
    solutions = combo(default_large_knap)
    assert solutions[0].fitness <= 1.0  # Here compares time
    solutions = combo(default_large_knap, only_time=False)
    assert len(solutions) == 1
    assert all(isinstance(i, Solution) for i in solutions)
    assert solutions[0].fitness >= 0.0
    assert len(solutions[0]) == 1000


def test_minknap(default_large_knap):
    solutions = minknap(default_large_knap)
    assert solutions[0].fitness <= 1.0  # Here compares time
    solutions = minknap(default_large_knap, only_time=False)
    assert len(solutions) == 1
    assert all(isinstance(i, Solution) for i in solutions)
    assert solutions[0].fitness >= 0.0
    assert len(solutions[0]) == 1000


def test_expknap(default_large_knap):
    solutions = expknap(default_large_knap)
    assert solutions[0].fitness <= 16.0  # Here compares time (15.0s max time allowed)
    solutions = expknap(default_large_knap, only_time=False)
    assert len(solutions) == 1
    assert all(isinstance(i, Solution) for i in solutions)
    assert solutions[0].fitness >= 0.0
    assert len(solutions[0]) == 1000


def test_pisinger_are_exact(default_large_knap):
    r_exknap = expknap(default_large_knap, only_time=False)
    r_combo = combo(default_large_knap, only_time=False)
    r_minknap = minknap(default_large_knap, only_time=False)
    all_solutions = [*r_exknap, *r_combo, *r_minknap]
    expected = r_combo[0].fitness
    assert len(all_solutions) == 3
    assert all(isinstance(i, Solution) for i in all_solutions)
    assert all(i.fitness == expected for i in all_solutions)


def test_pisingers_raises():
    """
    Raises an exception because the the problem is None
    """
    with pytest.raises(ValueError):
        expknap(None)
    with pytest.raises(ValueError):
        combo(None)
    with pytest.raises(ValueError):
        minknap(None)
