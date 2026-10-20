# Payoff and profit functions for basic financial derivatives

import numpy as np

def call(spot, strike, premium):
    """Return payoff and profit for a long call."""
    spot = np.asarray(spot, dtype=float)
    payoff = np.maximum(spot - strike, 0)
    profit = payoff - premium
    return payoff, profit


def forward(spot, delivery_price):
    """Return payoff and profit for a long forward."""
    spot = np.asarray(spot, dtype=float)
    payoff = spot - delivery_price
    profit = payoff.copy()
    return payoff, profit


def futures(spot, futures_price):
    """Return terminal payoff and simplified profit for long futures."""
    spot = np.asarray(spot, dtype=float)
    payoff = spot - futures_price
    profit = payoff.copy()
    return payoff, profit


def bull_call_spread(
    spot, lower_strike, upper_strike, lower_premium, upper_premium
):
# Return (payoff, profit) for a bull call spread.
    if lower_strike >= upper_strike:
        print("lower_strike must be less than upper_strike")

    spot = np.asarray(spot, dtype=float)
    payoff = (
        np.maximum(spot - lower_strike, 0)
        - np.maximum(spot - upper_strike, 0)
    )
    net_premium = lower_premium - upper_premium
    return payoff, payoff - net_premium


def bear_put_spread(
    spot, lower_strike, upper_strike, lower_premium, upper_premium
):
# Return (payoff, profit) for a bear put spread.
    if lower_strike >= upper_strike:
        print("lower_strike must be less than upper_strike")

    spot = np.asarray(spot, dtype=float)
    payoff = (
        np.maximum(upper_strike - spot, 0)
        - np.maximum(lower_strike - spot, 0)
    )
    net_premium = upper_premium - lower_premium
    return payoff, payoff - net_premium