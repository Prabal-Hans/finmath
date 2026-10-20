# Payoff and profit functions for basic financial derivatives

import numpy as np

def call(spot, strike, premium):
    payoff = np.max(np.asarray(spot) - strike,0)
    profit = (payoff - premium)
    return payoff, profit 
# returns payoff and profit for a long call

def put(spot, strike, premium):
    payoff = np.maximum(strike - np.asarray(spot),0)
    profit = payoff - premium
    return payoff, profit
# returns payoff and prift for a long put

def forward(spot, delivery_price):
    payoff = np.asarray(spot) - delivery_price
    return payoff
# Return payoff for a long forward at maturity.
# The payoff is the same as profit for a long forward.

def futures(spot, futures_price):
    payoff = np.asarray(spot) - futures_price
    return payoff
# Return terminal payoff for a long futures at maturity.
# The simplified profit is the same as the payoff for a long futures.

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
