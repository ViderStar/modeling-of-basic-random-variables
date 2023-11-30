import numpy as np


def print_distribution_stats(distribution_name, unbiased_mean, true_mean, unbiased_variance, true_variance):
    print(f"\n{distribution_name} Distribution:")
    print("Unbiased mean:", unbiased_mean)
    print("True mean:", true_mean)
    print("Unbiased variance:", unbiased_variance)
    print("True variance:", true_variance)


# LabWork2
def generate_geometric(n, p):
    return np.random.geometric(p, size=n)


def generate_poisson(n, lambd):
    return np.random.poisson(lambd, size=n)


def bernoulli(n, p):
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


def generate_geometric(n, p):
    return np.random.geometric(p, size=n)


def generate_poisson(n, lambd):
    return np.random.poisson(lambd, size=n)


def calculate_unbiased_mean(random_numbers):
    return np.mean(random_numbers)


def calculate_unbiased_variance(random_numbers):
    return np.var(random_numbers, ddof=1)


def calculate_true_mean_geometric(p):
    return 1 / p


def calculate_true_variance_geometric(p):
    return (1 - p) / (p ** 2)


def calculate_true_mean_poisson(lambd):
    return lambd


def calculate_true_variance_poisson(lambd):
    return lambd


# LabWork3
def simulate_normal(n, m, s2, N):
    samples = np.random.normal(m, np.sqrt(s2), size=(n, N))
    means = np.mean(samples, axis=1)
    variances = np.var(samples, axis=1, ddof=1)
    return means, variances


def simulate_lognormal(n, m, s2):
    samples = np.random.lognormal(m, np.sqrt(s2), size=n)
    return samples


def simulate_logistic(n, a, b):
    samples = np.random.logistic(a, b, size=n)
    return samples


def simulate_laplace(n, a):
    samples = np.random.laplace(0, a, size=n)
    return samples


def simulate_exponential(n, a):
    samples = np.random.exponential(1 / a, size=n)
    return samples


def calculate_unbiased_mean(samples):
    return np.mean(samples)


def calculate_unbiased_variance(samples):
    return np.var(samples, ddof=1)


def calculate_true_mean_lognormal(m, s2):
    return np.exp(m + (s2 / 2))


def calculate_true_variance_lognormal(m, s2):
    return (np.exp(s2) - 1) * np.exp(2 * m + s2)


def calculate_true_mean_logistic(a, b):
    return a


def calculate_true_variance_logistic(a, b):
    return (np.pi ** 2) * (b ** 2) / 3


def calculate_true_mean_laplace(a):
    return 0


def calculate_true_variance_laplace(a):
    return 2 * (a ** 2)


def calculate_true_mean_exponential(a):
    return 1 / a


def calculate_true_variance_exponential(a):
    return 1 / (a ** 2)
