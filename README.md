## Monte Carlo in Finance

This small pedagogical project is for similating stochastic processes in finance and pricing europeans options using Monte Carlo method.

The objective is to :
- Implement simple simulators of brownian motion and geometric brownian motion
- Use these simulator to approximate the price of europeans options (call and put) via Monte Carlo
- Illustrate the convergence of Monte Carlo estimators and the link with Black-Scholes formula
- Plot trajectories and prices for some exmaples

The project is made for fun, and I hope you'll take pleasure to read it too ;).

---


## 
```bash
monte_carlo_finance/
├── examples/
│   ├── price_european_options.ipynb
│   └── simulate_paths.ipynb
├── mc_finance/
│   ├── __init__.py
│   ├── brownian.py
│   ├── gbm.py
│   ├── option_pricing.py
│   └── utils.py
├── tests/
├── ├── test_brownian.py
├── ├── test_gbm.py
├── └── test_option_pricing.py
├── README.md
├── requirements.txt
└── .gitignore
```
