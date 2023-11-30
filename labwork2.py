from matplotlib import pyplot as plt
from distributions import *


def LabWork2():
    n = 1000
    p_bernoulli = 0.2
    m_binomial = 6
    p_binomial = 0.75
    p_geometric = 0.9
    lambda_poisson = 0.7

    bernoulli_numbers = bernoulli(n, p_bernoulli)
    binomial_numbers = binomial(n, m_binomial, p_binomial)
    geometric_numbers = generate_geometric(n, p_geometric)
    poisson_numbers = generate_poisson(n, lambda_poisson)

    # Доп задание: график эмпирической функции распределения (ECDF)
    def ecdf_bernulli(data):
        x_bernoulli = np.sort(data)
        y_bernoulli = np.arange(1, len(data) + 1) / len(data)

        plt.plot(x_bernoulli, y_bernoulli, label='Empirical')

        x_theoretical_bernoulli = [0, 1]
        y_theoretical_bernoulli = [1 - p_bernoulli, 1]

        plt.plot(x_theoretical_bernoulli, y_theoretical_bernoulli, label='Theoretical')
        plt.xlabel('Value')
        plt.ylabel('Probability')
        plt.title('График эмпирической функции распределения (Бернулли)')
        plt.legend()
        plt.show()

    ecdf_bernulli(bernoulli_numbers)

    bernoulli_mean = unbiased_mean(bernoulli_numbers)
    bernoulli_variance = unbiased_variance(bernoulli_numbers)
    binomial_mean = unbiased_mean(binomial_numbers)
    binomial_variance = unbiased_variance(binomial_numbers)

    geometric_mean = calculate_unbiased_mean(geometric_numbers)
    geometric_variance = calculate_unbiased_variance(geometric_numbers)
    poisson_mean = calculate_unbiased_mean(poisson_numbers)
    poisson_variance = calculate_unbiased_variance(poisson_numbers)

    true_mean_bernoulli1 = true_mean_bernoulli(p_bernoulli)
    true_variance_bernoulli1 = true_variance_bernoulli(p_bernoulli)
    true_mean_binomial1 = true_mean_binomial(m_binomial, p_binomial)
    true_variance_binomial1 = true_variance_binomial(m_binomial, p_binomial)

    true_mean_geometric = calculate_true_mean_geometric(p_geometric)
    true_variance_geometric = calculate_true_variance_geometric(p_geometric)
    true_mean_poisson = calculate_true_mean_poisson(lambda_poisson)
    true_variance_poisson = calculate_true_variance_poisson(lambda_poisson)

    print_distribution_stats("Bernoulli", bernoulli_mean, true_mean_bernoulli1, bernoulli_variance,
                             true_variance_bernoulli1)
    print_distribution_stats("Binomial", binomial_mean, true_mean_binomial1, binomial_variance, true_variance_binomial1)
    print_distribution_stats("Geometric", geometric_mean, true_mean_geometric, geometric_variance,
                             true_variance_geometric)
    print_distribution_stats("Poisson", poisson_mean, true_mean_poisson, poisson_variance, true_variance_poisson)
