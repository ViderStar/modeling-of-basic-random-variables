# modeling-of-basic-random-variables

This repository contains code for two lab works related to random number generators and probability distributions.

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

## Usage

To run the code, make sure you have the required packages installed. You can run the code by executing the following
command:

```python main.py```

Make sure to modify the parameters in the code as needed for your specific experiments.

## Dependencies

The code relies on the following dependencies:

- `numpy`
- `matplotlib`

You can install these dependencies using `pip`:

```pip install numpy matplotlib```

