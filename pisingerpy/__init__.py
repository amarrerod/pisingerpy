#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   __init__.py
@Time    :   2024/09/17 12:40:27
@Author  :   Alejandro Marrero
@Version :   1.0
@Contact :   amarrerd@ull.edu.es
@License :   (C)Copyright 2024, Alejandro Marrero
@Desc    :   None
"""

__all__ = ["minknap", "combo", "expknap", "Knapsack", "Solution"]

from dataclasses import dataclass
from typing import List, Sequence

import numpy as np
from pisinger_cpp import combo_cpp, expknap_cpp, minknap_cpp


@dataclass
class Knapsack:
    """Class representing a knapsack problem instance.
    It contains the profits, weights, and capacity of the knapsack.
    Resembles DIGNEApy Knapsack class."""

    profits: Sequence[int]
    weights: Sequence[int]
    capacity: int

    def __len__(self):
        return len(self.profits)


@dataclass
class Solution:
    """Class representing a solution to a knapsack problem instance.
    It contains the variables (the items selected), the objectives (the profit), and the fitness (the profit).
    Resembles DIGNEApy Solution class."""

    variables: Sequence[int]
    objectives: Sequence[float]
    fitness: float

    def __len__(self):
        return len(self.variables)


def minknap(problem: Knapsack, only_time: bool = True) -> List[Solution]:
    if problem is None:
        msg = "No problem found in args of minknap heuristic"
        raise ValueError(msg)

    x = np.zeros(len(problem))
    time, best = minknap_cpp(
        len(problem), problem.profits, problem.weights, x, problem.capacity
    )
    f = time if only_time else best
    return [Solution(variables=x, objectives=(f,), fitness=f)]


def expknap(problem: Knapsack, only_time: bool = True) -> List[Solution]:
    if problem is None:
        msg = "No problem found in args of expknap heuristic"
        raise ValueError(msg)

    x = np.zeros(len(problem))
    time, best = expknap_cpp(
        len(problem), problem.profits, problem.weights, x, problem.capacity
    )
    f = time if only_time else best
    return [Solution(variables=x, objectives=(f,), fitness=f)]


def combo(problem: Knapsack, only_time: bool = True) -> List[Solution]:
    if problem is None:
        msg = "No problem found in args of combo heuristic"
        raise ValueError(msg)

    x = np.zeros(len(problem))
    time, best = combo_cpp(
        len(problem), problem.profits, problem.weights, x, problem.capacity
    )
    f = time if only_time else best
    return [Solution(variables=x, objectives=(f,), fitness=f)]
