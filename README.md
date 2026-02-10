
# Pisinger KP Solvers for Python

[![Build](https://github.com/amarrerod/pisingerpy/actions/workflows/python-app.yml/badge.svg)](https://github.com/amarrerod/pisingerpy/actions/workflows/python-app.yml)

A high-performance Python interface for David Pisinger’s renowned Knapsack Problem (KP) solvers. This package leverages **pybind11** to wrap the original C implementations, providing Python developers with efficient, low-level solver access while adhering to the `DIGNEApy` interfaces.

## 🚀 Overview

The Knapsack Problem is a classic algorithmic problem in combinatorial optimization. While Python is excellent for modeling, native Python implementations of KP solvers can be slow for large instances.

This project bridges that gap by compiling Pisinger's C algorithms (such as `minknap`, `combo`, etc.) into a Python extension module. It integrates seamlessly with **NumPy** for efficient data handling and strictly follows the **DIGNEApy** `Knapsack` and `Solution` protocols.

## ✨ Features

* **High Performance:** Direct bindings to optimized C code.
* **Standardized Interface:** Fully compatible with `DIGNEApy` data structures.
* **NumPy Integration:** Efficient array passing without unnecessary copying.
* **Ease of Use:** Simple Python API for complex C-level solvers.

---

## 🛠️ Prerequisites

Before installing, ensure you have the following dependencies:

* **Python >=3.12+**
* **C++ Compiler:** (GCC, Clang, or MSVC) supporting C++11 or later.
* **DIGNEApy:** (Ensure this package provides the `Knapsack` and `Solution` classes).


---

## 📦 Installation

### From Source

Clone the repository and build the extension using `pip`:

```bash
git clone https://github.com/yourusername/pisinger-kp.git
cd pisinger-kp
uv pip install .

```

*Note: The `setup.py` script automatically handles the compilation of the C++ sources and pybind11 bindings.*

---

## 💻 Usage

Here is a complete example of how to define a Knapsack problem using `DIGNEApy` and solve it using this package.

```python
import numpy as np
from pisinger_kp import minknap, Knapsack, Solution

# 1. Define your problem data
profit = np.array([10, 10, 12, 18], dtype=np.int32)
weights = np.array([2, 4, 6, 9], dtype=np.int32)
capacity = 15

# 2. Create a DIGNEApy Knapsack instance
# (Assuming the constructor follows: Knapsack(profits, weights, capacity))
instance = Knapsack(profit, weights, capacity)

# 3. Solve the instance
# The solver returns a DIGNEApy Solution object
solution = minknap(instance)

# 4. Process results
print(f"Optimal Objective Value: {solution.objectives}")

```

### Supported Solvers

Currently, the package wraps the following algorithms:

| Solver      | Description                                        | Best For                                |
| ----------- | -------------------------------------------------- | --------------------------------------- |
| **MinKnap** | The "Minimal Knapsack" algorithm.                  | Hard instances with small coefficients. |
| **Combo**   | A combination of dynamic programming and bounding. | Highly correlated data instances.       |
| **ExpKnap** | Expanding core algorithm.                          | Very large instances.                   |

---

## ⚙️ Development & Building

If you wish to modify the C++ bindings or add new solvers:

1. **Project Structure:**
* `src/`: Contains Pisinger's original C source files.


1. **Local Build:**
To build the extension in-place for testing:
```bash
uv pip install -e .

```



---

## 📜 License

This project is licensed under the [MIT License](https://www.google.com/search?q=LICENSE).

**Note on Pisinger's Code:** The underlying C solvers are the intellectual property of **David Pisinger**. Please refer to the original source distribution for specific licensing terms regarding the C implementations used within this wrapper.

---

## 🙌 Acknowledgements

* **David Pisinger** for the original C implementations of the Knapsack solvers.

---
