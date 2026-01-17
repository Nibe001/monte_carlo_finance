"""
Contains functions for pricing european call/put using Monte Carlo methods under GBM.
"""

from __future__ import annotations
import numpy as np
from .gbm import gbm_paths

def price_european_call_mc(
    S0: float,
    K: float,
    T: float,
    r: float,
    sigma: float,
    n: int = 100,
    m: int = 10_000,
    random_state: int | None = None
    ) -> float:
    
    """
    Prices a European call option using Monte Carlo simulation under Geometric Brownian Motion (GBM).
    
    Parameters
    ----------
    S0 : float
        Initial stock price.
    K : float
        Strike price of the option.
    T : float
        Time horizon (maturity of the option).
    r : float
        Risk-free rate.
    sigma : float
        Volatility coefficient.
    n : int
        Number of time steps.
    m : int
        Number of paths to simulate.
    random_state : int | None, optional
        Seed for the random number generator. Default is None.
        
    Returns
    -------
    price : float
        Estimated price of the European call option.
        
    Algorithm
    ---------
    1. Simulate `m` paths of GBM using the `gbm_paths` function.
    2. Calculate the payoff for each path at maturity T.
    3. Compute the average payoff and discount it back to present value.
    4. Return the estimated option price.
    """
    
    paths = gbm_paths(S0, r, sigma, n, m, T, random_state) # mu is set to r for risk-neutral pricing
    
    payoffs = np.maximum(paths[:, -1] - K, 0)
    discounted_payoff = np.exp(-r * T) * np.mean(payoffs)
    
    return discounted_payoff


def price_european_put_mc(
    S0: float,
    K: float,
    T: float,
    r: float,
    sigma: float,
    n: int = 100,
    m: int = 10_000,
    random_state: int | None = None
    ) -> float:
    
    """
    Prices a European put option using the previous function and the put-call parity.
    The relation states that:
        C - P = S0 - K * exp(-r * T)
    where C is the call price, P is the put price, S0 is the initial stock price,
    and r is the risk-free rate.
    """
    
    call_price = price_european_call_mc(S0, K, T, r, sigma, n, m, random_state)
    put_price = call_price - S0 + K * np.exp(-r * T)
    
    return put_price