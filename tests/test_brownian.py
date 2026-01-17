import numpy as np
from mc_finance.brownian import brownian_paths


def test_brownian_paths_shape():
    """
    Verify that the shape of the returned paths is correct.
    """
    m = 5
    n = 10
    T = 1.0
    paths = brownian_paths(n=n, m=m, T=T, random_state=0)
    assert paths.shape == (m, n + 1)


def test_brownian_paths_starts_at_zero():
    """
    Verify that all paths start at zero.
    """
    paths = brownian_paths(n=10, m=3, T=1.0, random_state=0)
    assert np.allclose(paths[:, 0], 0.0)