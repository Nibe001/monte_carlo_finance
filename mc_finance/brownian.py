"""
Contains functions for simulating 1-dimensional Brownian motion.
"""

from __future__ import annotations
import numpy as np
from .utils import get_rng


def brownian_paths(
    n: int,
    m: int,
    T: float,
    random_state: int | None = None
    ) -> np.ndarray:
    
    """
    Simulates `m` paths of 1-dimensional Brownian motion over time interval [0, T]
    using `n` time steps.
    
    Parameters
    ----------
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
    paths :np.ndarray
        A 2D array of shape (m, n+1) containing the simulated Brownian motion paths. Each row corresponds to a path,
        and each column corresponds to a time step.
        
    Algorithm
    ---------
    1. Initialize a random number generator with the given seed.
    2. Create an array of zeros with shape (m, n+1) to store the paths.
    3. Calculate the time increment `dt = T / n`.
    4. Generate random increments from a normal distribution with mean 0 and standard deviation `sqrt(dt)`.
    5. Compute the cumulative sum of the increments to obtain the Brownian paths.
    6. Return the array of simulated paths.
    """
    
    # TODO: Implement the function to simulate Brownian motion paths
    raise NotImplementedError("Function 'brownian_paths' is not yet implemented.")