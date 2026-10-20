
# Demonstrate options, forwards and futures.

from pathlib import Path

import numpy as np

from finmath import call, put, forward, futures, plot_strategies


# Load example prices relative to the project directory.
data_file = (
    Path(__file__).resolve().parents[1]
    / "data"
    / "sample_prices.csv"
)
prices = np.loadtxt(data_file, delimiter=",", skiprows=1)

# Each tuple contains a label, function and its arguments.
strategies = [
    ("Long call", call, (100, 5)),
    ("Long put", put, (100, 5)),
    ("Long forward", forward, (100,)),
    ("Long futures", futures, (100,)),
]

# Plot the profit of all four instruments.
plot_strategies(
    prices,
    strategies,
    metric="profit",
    title="Options, Forward and Futures: Profit at Maturity",
)

# Also demonstrate the numerical calculations at one price.
payoff, profit = call(120, 100, 5)
print(f"Call payoff at S_T = 120: {payoff:.2f}")
print(f"Call profit at S_T = 120: {profit:.2f}")
