# FinMath

FinMath is a small Python package for calculating and visualising the terminal payoffs and profits of basic financial derivatives.

## Features

- Long European call and put options
- Forward and futures contracts
- Bull call and bear put spreads
- Payoff and profit calculations
- Matplotlib graphs comparing multiple strategies

## Requirements

Python 3.8 or later, NumPy and Matplotlib.

## Installation

Clone the repository and navigate to its root directory. Then install the package in editable mode:

```bash
pip install -e .
```

## Example

```python
import numpy as np
from finmath import call

payoff, profit = call(120, 100, 5)
print(payoff)  # 20.0
print(profit)  # 15.0
```

The functions accept individual prices or NumPy arrays of prices.

## Running the demonstrations

From the project root, run:

```bash
python demo/demo01.py
python demo/demo02.py
```

The first demo compares options, forwards and futures. The second compares bull call and bear put spreads.

## Assumptions

Option profits subtract the premium paid. Forward and futures profits use a simplified terminal-payoff convention and exclude financing, transaction costs and margin cash flows. The package does not price derivatives or model a complete trading account.

## Project structure

- `finmath`: calculation and plotting modules
- `demo/`: demonstration scripts
- `data/`: sample underlying prices
- `pyproject.toml`: package configuration