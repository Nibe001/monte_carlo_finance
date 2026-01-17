"""
Contains functions for simulating geometric Brownian motion.
"""

from __future__ import annotations
import numpy as np
from .brownian import brownian_paths

def gbm_paths(
    S0: float,
    mu: float,
    sigma: float,
    n: int,
    m: int,
    T: float,
    random_state: int | None = None
    ) -> np.ndarray:
    
    """
    Simulates `m` paths of Geometric Brownian Motion (GBM) over time interval [0, T]
    using `n` time steps.
    
    Parameters
    ----------
    S0 : float
        Initial stock price.
    mu : float
        Drift coefficient.
    sigma : float
        Volatility coefficient.
    n : int
        Number of time steps.
    m : int
        Number of paths to simulate.
    T : float
        Time horizon.
    random_state : int | None, optional
        Seed for the random number generator. Default is None.
        
    Returns
    -------
    paths : np.ndarray
        A 2D array of shape (m, n+1) containing the simulated GBM paths. Each row corresponds to a path,
        and each column corresponds to a time step.
        
    Algorithm
    ---------
    1. Simulate `m` paths of Brownian motion using the `brownian_paths` function.
    2. Calculate the time increment `dt = T / n`.
    3. Compute the GBM paths using the price S(t) analytic form.
    4. Return the array of simulated GBM paths.
    """
    
    paths = brownian_paths(n, m, T, random_state)
    
    time_grid = np.linspace(0, T, n + 1)
    gbm_paths = S0 * np.exp((mu - 0.5 * sigma**2) * time_grid + sigma * paths)
    
    return gbm_paths