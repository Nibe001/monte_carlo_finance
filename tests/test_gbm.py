import numpy as np
from mc_finance.gbm import gbm_paths


def test_gbm_paths_shape():
    """
    Verify that the shape of the returned paths is correct.
    """
    S0 = 100.0
    paths = gbm_paths(S0=S0, mu=0.05, sigma=0.2,
                      n=10, m=5, T=1.0, random_state=0)
    assert paths.shape == (5, 10 + 1)


def test_gbm_paths_positive():
    """
    Verify that GBM prices are strictly positive.
    """
    S0 = 100.0
    paths = gbm_paths(S0=S0, mu=0.05, sigma=0.2,
                      n=10, m=5, T=1.0, random_state=0)
    assert np.all(paths > 0.0)