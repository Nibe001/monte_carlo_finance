from mc_finance.option_pricing import (
    price_european_call_mc,
    price_european_put_mc,
)


def test_call_price_is_positive():
    """
    Verify that the Monte Carlo price of a call is positive.
    """
    price = price_european_call_mc(
        S0=100.0, K=100.0, T=1.0, r=0.05, sigma=0.5,
        m=1000, n=50, random_state=0
    )
    assert price > 0.0


def test_put_price_is_positive():
    """
    Verify that the Monte Carlo price of a put is positive.
    """
    price = price_european_put_mc(
        S0=100.0, K=100.0, T=1.0, r=0.05, sigma=0.2,
        m=1000, n=50, random_state=0
    )
    assert price > 0.0