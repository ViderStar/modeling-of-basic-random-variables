# modeling-of-basic-random-variables

This repository contains code for 5 lab works related to random number generators and probability distributions.

## LabRabota1

The `LabRabota1` function demonstrates the usage of two random number generators: MKM (Mixed Congruential Method) and
MacLaren-Marsaglia. It generates a sequence of random numbers using these generators and prints the first, 14th, and
1000th elements of each sequence.

## LabRabota2

The `LabRabota2` function focuses on probability distributions, specifically the Bernoulli and binomial distributions.
It generates random numbers following these distributions and performs the following tasks:

- Plots the empirical cumulative distribution function (ECDF) for the Bernoulli distribution.
- Calculates the unbiased mean and variance for both the Bernoulli, Binomial, Geometric and Poisson distributions.
- Compares the calculated values with the true mean and variance of the distributions.

## LabRabota3

Modeling from Continuous Distributions: In this task, we need to simulate n = 10000 random variables from the given
continuous distributions. Calculate the unbiased estimates of the mean and variance and compare them with the true
values (if available). If the mean does not exist, calculate the sample median and compare it with the theoretical
value.

**Distributions:**

- Lognormal Distribution
- Logistic Distribution
- Laplace Distribution
- Exponential Distribution

Here are the implementations for LabWork 4 and 5:

## LabWork4

This lab work demonstrates the Monte Carlo integration technique. It computes the numerical integration of two functions over different domains using Monte Carlo integration.

The key steps are:

1. Define the integrand functions and their domains. 

2. Implement the Monte Carlo integration method - it samples random points from the domain and estimates the integral as the average of function evaluations at these points.

3. Compute integrals for varying number of samples and record the errors.

4. Plot the errors vs number of samples on a log-log scale to show convergence.

This verifies that the Monte Carlo method yields increasingly accurate results as more samples are taken.

## LabWork5

This lab work demonstrates Markov chain Monte Carlo (MCMC) to solve a system of linear equations. 

The key steps are:

1. Define the matrix A and vector b representing the linear system Ax = b.

2. Implement the MCMC algorithm - it performs random walks on the state space, where the transition probabilities are given by A. The solution is estimated as the average of function evaluations at visited states, weighted by the transition probabilities.

3. Run MCMC for varying number of chains and chain lengths. 

4. Compute and record the error compared to exact solution.

5. Plot the errors versus chain length on log-log scale for different number of chains.

This shows that longer chains and more chains result in smaller errors, demonstrating convergence of the MCMC method.

The implementations test the Monte Carlo integration and MCMC techniques on practical problems to demonstrate their applicability and convergence behavior.

## Usage

To run the code, make sure you have the required packages installed. You can run the code by executing the following
command:

```python main.py```

Make sure to modify the parameters in the code as needed for your specific experiments.

## Dependencies

The code relies on the following dependencies:

- `numpy`
- `matplotlib`
- `plotly`
- `scipy.stats`

You can install these dependencies using `pip`:

```pip install numpy matplotlib plotly scipy.stats```

