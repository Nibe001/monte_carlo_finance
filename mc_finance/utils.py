"""
Return the random number generator based on the provided seed.
"""

from __future__ import annotations
import numpy as np

def get_rng(random_state: int | None = None) -> np.random.Generator:
    """
    Returns a NumPy random number generator initialized with the given seed.
    
    Parameters
    ----------
    random_state : int | None, optional
        Seed for the random number generator. Default is None.
        
    Returns
    -------
    rng : np.random.Generator
        A NumPy random number generator instance.
    """
    return np.random.default_rng(random_state)