
# Compare bull call and bear put spread profits.

from pathlib import Path

import numpy as np

from finmath import bull_call_spread, bear_put_spread, plot_strategies


data_file = (
    Path(__file__).resolve().parents[1]
    / "data"
    / "sample_prices.csv"
)
prices = np.loadtxt(data_file, delimiter=",", skiprows=1)

strategies = [
    (
        "Bull call spread",
        bull_call_spread,
        (90, 110, 15, 5),
    ),
    (
        "Bear put spread",
        bear_put_spread,
        (90, 110, 15, 5),
    ),
]

plot_strategies(
    prices,
    strategies,
    metric="profit",
    title="Bull Call vs Bear Put Spread",
)

# Check one numerical result.
payoff, profit = bull_call_spread(
    120, 90, 110, 15, 5
)
print(f"Bull call spread payoff: {payoff:.2f}")
print(f"Bull call spread profit: {profit:.2f}")
