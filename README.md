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
Let's consider a family $(W_t^{(i)})_{t\ge 0}$ of i.i.d Wiener Processes where $i = 1, \dots, N$.

For each time $t\ge 0$, the respectives Monte Carlo's estimators of expectation and variance are given by :
$$\hat{\mu_t} = \frac{1}{N} \sum_{i=1}^N W_t^{(i)} \quad \text{ and } \quad \hat{\sigma_t^2} = \frac{1}{N} \sum_{i=1}^N (W_t^{(i)})^2.$$

Now, the interest is to check if those estimators are **consistants** and **convergents**. 
For that, we use the following theorems which gives us the convergence and the speed of that convergence.

$\textbf{Theorem 1 :}$
- $\textit{Strong Law of Large Numbers}$ : For $t\ge 0$ fixed, since $(W_t^{(i)})_{i=1}^N$ are i.i.d random variables and $\mathbb{E}(W_t^{(1)}) < \infty$, we can apply the LLN and get :
$$\hat{\mu_t} \xrightarrow[N \to \infty]{\mathbb{P}-a.s} \mathbb{E}(W_t^{(1)}) = 0.$$

- $\textit{Convergence of the estimator}$ :  To get the convergence, we can add and substract the true expectation $\mu_t$ in the square and use the remarkable identity $(a + b)^2 = a^2 + b^2 + 2ab$ in order to get the true variance $\sigma_t$ and some other terms which converge towards 0. Hence, we obtain :
$$\hat{\sigma_t^2} \xrightarrow[N \to \infty]{} \sigma_t^2 = t.$$

- $\textit{Central Limit Theorem}$ : Now that we have the convergence toward the true expectation and the results on the variance, one would know what's the error we made and the rate of convergence. For this purpose, we use the CLT and get that :
$$\sqrt{N} \frac{\hat{\mu_t} - \mu_t}{\sigma_t} = \sqrt{N} \frac{\hat{\mu_t}}{\sqrt{t}} \xrightarrow[N \to \infty]{law} \mathcal{N}(0, t).$$

We'll pay attention to check if experimental results match theoretical ones.

## 1.2. Geometric Brownian Motion (GBM)

### 1.2.1. Definition

The GBM $(S_t)_{t\ge 0}$ is the stochastic process define by the stochastic differential equation (SDE) 
$$dS_t = \mu S_t dt + \sigma S_t d W_t \quad \text{where } \mu \in \mathbb{R} \text{ and } \sigma > 0.$$

### 1.2.2. Analytical form

Let's consider the stochastic process $Y_t = \log S_t$.
By Itô formula, we have :
$$dY_t = d\log S_t = {1 \over S_t}dS_t - {1 \over 2 S_t^2}\sigma^2S_t^2 dt$$

And replacing the dynamic of $S_t$ gives us :
$$dY_t = \left(\mu - \frac12 \sigma^2\right)dt + \sigma dW_t$$

And then, 
$$Y_t = Y_0 + \left(\mu - \frac12 \sigma^2\right)t + \sigma \int_0^t dW_s = Y_0 + \left(\mu - \frac12 \sigma^2\right) + \sigma W_t$$

We finally get :
$$S_t = S_0 \exp(\left(\mu - \frac12 \sigma^2\right)t + \sigma W_t) \quad \text{with } S_0 = e^{Y_0}.$$

### 1.2.3. Some ``good`` Properties

From the previous section, we can deduce some interesting property that we'll verify with the simulations. Here they are :
- $Y_t = \log S_t \sim \mathcal{N}\left(\log S_0 + (\mu - \frac12 \sigma^2)t, \sigma^2t\right)$ since $W_t \sim \mathcal{N}(0, t)$
- $\mathbb{E}(S_t) = \mathbb{E}(S_t | \mathcal{F}_0) = S_0 \exp\left((\mu - \frac12 \sigma^2)\right)\mathbb{E}(e^{\sigma \sqrt{t} W_1}) = S_0e^{\mu t}$ because $\mathbb{E}(e^{aX}) = e^{a^2 \over 2}$ when $X \sim \mathcal{N}(0, 1)$. (where $\mathcal{F}_0 = \{\emptyset, \Omega\}$)
- Using the same reasoning yield $\mathbb{V}(S_t) = S_0^2 e^{2\mu t}(e^{\sigma^2 t} - 1)$.

To illustrate these results, we will plot the histograms of $\log S_T$ (for some horizon time $T$) and check if the distribution match the gaussian with the same parameters. Also, we'll see if the convergence theorem holds. And at the end, check the impact of the varying of the volatility and the drift on the shape of that distribution.


## 1.3. Pricing of European Options

In our implementation, we'll only focus on the pricing of an european **Call Option** since the price of the **Put** can be deduce by the no-arbitrage relation.

Let's call this price $C$.

We suppose that the underlying follows is a GBM, the time horizon (maturity) is $T$, the interest rate is $r$ and the exercise price (strike) $K$.

For the **Call Option**, the payoff is define as $$\Pi_{call} = \max(S_T - K, 0)$$ since we exerce the option only if the underlying price at maturity $T$ is higher than the strike. In which case we get $S_T - K$, otherwise 0 since we do not exerce and buy directly from the market.

To have a better understanding, we could say that the price of the option at $t$ is the amount of money we need to invest at that time in the cash in order to get the payoff at maturity $T$. In other words, the amount we need to cover the potential lose of money (i.e in case of exercising of the option).

### 1.3.1. Theoretical Price

Under the risk-neutral measure $\mathbb{Q}$, the actualised price of the underlying is a martingale. 
So, $$\forall t < T, C_t e^{-rt} = e^{-rT}\mathbb{E}^{\mathbb{Q}}[(S_T - K)^{+}]$$. And in particular,

$$C_0 = e^{-rT}\mathbb{E}^{\mathbb{Q}}[(S_T - K)^{+}]$$

### 1.3.2. Monte Carlo Estimator

Let $N \ge 1$.
Then for $N$ simulated i.i.d trajectories $(S^{(i)})_{i=1}^N$ until the maturity date $T$, we have the following estimator :
$$\hat{C_0} = e^{-rT}\frac{1}{N}\sum_{i=1}^N (S_T^{(i)} - K)^{+}$$.

By the strong law of large number, this estimator converge almost surely to the theoretical price $C_0$ from the previous section.

Also, the error of estimation is in $\mathcal{O}(\sqrt{N})$ by CLT.

### 1.3.3. Black-Scholes (B.S) Formula 

Using the B.S formula, we can compute the price of an european option given the parameters. And the price is given by :

$$C_{BS} = S_0 \Phi(d_1) - Ke^{-rT}\Phi(d_2) \quad \text{where } d_{1,2} = {\ln(\frac{S_0}{K}) + (r ± \frac12 \sigma^2) T \over \sigma \sqrt{T}} \text{ and } \Phi \text{ the CDF of } \mathcal{N}(0, 1).$$


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