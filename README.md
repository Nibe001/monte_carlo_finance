# Monte Carlo in Finance

This small pedagogical project is for similating stochastic processes in finance and pricing europeans options using Monte Carlo method.

The objective is to :
- Implement simple simulators of brownian motion and geometric brownian motion
- Use these simulators to approximate the price of european options (call and put) via Monte Carlo
- Illustrate the convergence of Monte Carlo estimators and the link with Black-Scholes formula
- Plot trajectories and prices for some examples

The project is made for fun, and I hope you'll take pleasure to read it too ;).

---


# 1. Mathematical Framework

## 1.1. Brownian Motion (Wiener Process)

### 1.1.1. Definition

A standard brownian motion $(W_t)_{t\ge 0}$ is a stochastic process that verify the properties :

1) $W_0 = 0$
2) $(W_t)_{t\ge 0}$ is increment independant, i.e $W_t - W_s$ is independant from the $\sigma$-field $\sigma(W_u, u < s)$ where $s < t$.
3) $(W_t)_{t\ge 0}$ has gaussian increment i.e $W_t - W_s \sim \mathcal{N}(0, t - s)$ for $0 \leq s < t$.

Remark :

Using that definition, we can directly deduce that $W_t \sim \mathcal{N}(0, t)$ and then $\mu_t = \mathbb{E}(W_t) = 0$ and $\sigma_t^2 = \mathbb{V}(W_t) = t$.

### 1.1.2. Theorem

Let $N \ge 1$ an integer.
Let's consider a family $(W_t^{(i)})_{t\ge 0}$ of i.i.d Wiener Processes where $i \in \{1, \dots, N\}$.

For each time $t\ge 0$, the respectives Monte Carlo's estimators of expectation and variance are given by :
$$\hat{\mu_t} = \frac{1}{N} \sum_{i=1}^N W_t^{(i)} \quad \text{ and } \quad \hat{\sigma_t^2} = \frac{1}{N} \sum_{i=1}^N (W_t^{(i)})^2.$$

Now, the interest is to check if those estimators are **consistants** and **convergents**. 
For that, we use the following theorems which gives us the convergence and the speed of that convergence.

$\textbf{Theorem 1 :}$
- $\textit{Law of Large Numbers}$ : For $t\ge 0$ fixed, since $(W_t^{(i)})_{i=1}^N$ are i.i.d random variables, we can apply the LLN and get :
$$\hat{\mu_t} \xrightarrow[N \to \infty] \mathbb{E}(X) = 0 \quad \text{ with } X \sim \mathcal{N}(0, t).$$

- Convergence of Monte Carlo's Variance estimator :
$$\hat{\sigma_t^2} \xrightarrow[N \to \infty] T.$$

We'll pay attention to check if experimental results match theoretical ones.

$\textbf{\textit{Proof (Theorem 1) :}}$




# 2. Project Structure

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


# 3. Installation