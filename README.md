# Monte Carlo Option Pricing Simulator

This project estimates the fair price of European call and put options using **Monte Carlo simulations** based on **Geometric Brownian Motion (GBM)**. The results are compared with the analytical solution from the **Black-Scholes formula**.

## 📌 Overview

The simulator:
- Models stock price evolution using GBM
- Simulates thousands of possible future stock paths
- Computes option payoffs at maturity and discounts them to present value
- Compares Monte Carlo prices with Black-Scholes prices
- Visualizes the distribution of simulated prices

## 💡 Mathematical Model

Stock prices follow the stochastic differential equation:

\[
S_{t+1} = S_t \cdot \exp\\left((\\mu - \\frac{1}{2}\\sigma^2)\\Delta t + \\sigma \\sqrt{\\Delta t} Z\\right)
\]

Where:
- \( S_t \): stock price at time \( t \)
- \( \mu \): drift (expected return)
- \( \sigma \): volatility
- \( Z \sim \mathcal{N}(0,1) \): standard normal noise

## ⚙️ Parameters

The following parameters can be modified in the script:

| Parameter | Description              | Default |
|----------:|--------------------------|---------|
| `S0`      | Initial stock price      | 100     |
| `K`       | Strike price             | 105     |
| `T`       | Time to maturity (years) | 1.0     |
| `r`       | Risk-free interest rate  | 0.05    |
| `sigma`   | Volatility               | 0.2     |
| `n_simulations` | Number of paths   | 100,000 |

## 📊 Example Output

