import numpy as np


def bernoulli(n,p):
    random_numbers = []
    for _ in range(n):
        r = np.random.random()
        x = 1 if r <= p else 0
        random_numbers.append(x)
    return random_numbers


def binomial(n, m, p):
    random_numbers = []
    for _ in range(n):
        count = 0
        for _ in range(m):
            r = np.random.random()
            if r <= p:
                count += 1
        random_numbers.append(count)
    return random_numbers


def unbiased_mean(random_numbers):
    return np.mean(random_numbers)


def unbiased_variance(random_numbers):
    return np.var(random_numbers, ddof=1)


def true_mean_bernoulli(p):
    return p


def true_variance_bernoulli(p):
    return p * (1 - p)


def true_mean_binomial(m, p):
    return m * p


def true_variance_binomial(m, p):
    return m * p * (1 - p)