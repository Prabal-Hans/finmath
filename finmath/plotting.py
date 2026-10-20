
# Plot payoffs or profits for derivative strategies.

import matplotlib.pyplot as plt
import numpy as np


def plot_strategies(
    prices, strategies, metric="profit", title=None
):
    """Plot payoff or profit for one or more strategies.

    Parameters
    ----------
    prices : array-like
        Underlying prices at maturity.
    strategies : list
        Tuples of (label, function, arguments).
        Each function must return (payoff, profit).
    metric : str
        Either 'payoff' or 'profit'.
    title : str or None
        Optional title for the graph.

    Returns
    -------
    matplotlib.axes.Axes
        The axes containing the graph.
    """
    if metric not in ("payoff", "profit"):
        raise ValueError("metric must be 'payoff' or 'profit'")

    prices = np.asarray(prices, dtype=float)
    fig, ax = plt.subplots(figsize=(8, 5))

    for label, function, arguments in strategies:
        payoff, profit = function(prices, *arguments)
        values = payoff if metric == "payoff" else profit
        ax.plot(prices, values, label=label)

    ax.axhline(0, color="black", linewidth=0.8)
    ax.set_xlabel("Underlying price at maturity (£)")
    ax.set_ylabel(f"{metric.capitalize()} per unit (£)")
    ax.set_title(title or f"Derivative {metric.capitalize()}")
    ax.grid(alpha=0.3)
    ax.legend()
    fig.tight_layout()
    plt.show()

    return ax
