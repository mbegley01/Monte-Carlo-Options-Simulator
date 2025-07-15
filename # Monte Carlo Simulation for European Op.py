# Monte Carlo Simulation for European Option Pricing

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Parameters
S0 = 100        # initial stock price
K = 105         # strike price
T = 1.0         # time to maturity in years
r = 0.05        # risk-free rate
sigma = 0.2     # volatility
n_simulations = 100000  # number of Monte Carlo simulations

# Set seed for reproducibility
np.random.seed(42)

# Simulate end-of-period stock prices
Z = np.random.standard_normal(n_simulations)
ST = S0 * np.exp((r - 0.5 * sigma**2) * T + sigma * np.sqrt(T) * Z)

# Calculate call and put payoffs
call_payoff = np.maximum(ST - K, 0)
put_payoff = np.maximum(K - ST, 0)

# Discounted expected value
call_price = np.exp(-r * T) * np.mean(call_payoff)
put_price = np.exp(-r * T) * np.mean(put_payoff)

print(f"Monte Carlo Call Price: ${call_price:.2f}")
print(f"Monte Carlo Put Price:  ${put_price:.2f}")

# Compare with Black-Scholes formula
def black_scholes_call(S, K, T, r, sigma):
    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    return S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)

def black_scholes_put(S, K, T, r, sigma):
    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    return K * np.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)

bs_call = black_scholes_call(S0, K, T, r, sigma)
bs_put = black_scholes_put(S0, K, T, r, sigma)

print(f"Black-Scholes Call Price: ${bs_call:.2f}")
print(f"Black-Scholes Put Price:  ${bs_put:.2f}")

plt.hist(ST, bins=100, density=True, alpha=0.6, color='blue')
plt.title("Simulated End-of-Period Stock Prices")
plt.xlabel("Stock Price at T")
plt.ylabel("Density")
plt.grid(True)
plt.show()
