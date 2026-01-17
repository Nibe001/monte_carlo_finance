"""
Package initialization for mc_finance.
We will simulate some stochastic processes (Brownian motion, Geometric Brownian motion)
and price some european options using Monte Carlo methods.
"""

from .brownian import brownian_paths
from .gbm import gbm_paths
from .option_pricing import (
    price_european_call_mc,
    price_european_put_mc
)