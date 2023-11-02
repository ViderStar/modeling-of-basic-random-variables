from matplotlib import pyplot as plt
from generators import mkm_generator, macLarenMarsaglia
from distributions import *
from scipy.stats import lognorm, logistic, laplace, expon


def print_distribution_stats(distribution_name, unbiased_mean, true_mean, unbiased_variance, true_variance):
    print(f"\n{distribution_name} Distribution:")
    print("Unbiased mean:", unbiased_mean)
    print("True mean:", true_mean)
    print("Unbiased variance:", unbiased_variance)
    print("True variance:", true_variance)


def LabWork1():
    n = 1000
    a01 = 24149775
    c1 = 19581355
    m = 2 ** 31

    a02 = 179029053
    c2 = 457816087
    k = 128

    # Output sequence values to be tested
    #
    # MKM - 1st element:        0.614329
    # MKM - 15th element:       0.792078
    # MKM - 1000th element:     0.027633
    #
    # MacLaren-Marsaglia - 1st element:     0.008959
    # MacLaren-Marsaglia - 15th element:    0.614329
    # MacLaren-Marsaglia - 1000th element:  0.496629

    mkm1 = mkm_generator(a01, c1, m, n)
    print()
    print("MKM - 1st element:", mkm1[0])
    print("MKM - 14th element:", mkm1[14])
    print("MKM - 1000th element:", mkm1[999])
    print()

    mkm2 = mkm_generator(a02, c2, m, n)
    macLaren_Marsaglia = macLarenMarsaglia(mkm1, mkm2, k, n)
    print("MacLaren-Marsaglia - 1st element:", macLaren_Marsaglia[0])
    print("MacLaren-Marsaglia - 14th element:", macLaren_Marsaglia[14])
    print("MacLaren-Marsaglia - 1000th element:", macLaren_Marsaglia[999])


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

def LabWork3():
    n = 10000
    N = 48  # Number of terms in the Central Limit Theorem approximation

    # Task 1
    m_task1 = 0
    s2_task1 = 16
    means_task1, variances_task1 = simulate_normal(n, m_task1, s2_task1, N)
    true_mean_task1 = m_task1
    true_variance_task1 = s2_task1
    unbiased_mean_task1 = calculate_unbiased_mean(means_task1)
    unbiased_variance_task1 = calculate_unbiased_variance(means_task1)
    print_distribution_stats("Normal", unbiased_mean_task1, true_mean_task1, unbiased_variance_task1,
                             true_variance_task1)

    # Task 2
    m_lognormal = 1
    s2_lognormal = 1
    a_logistic = 0
    b_logistic = 1
    a_laplace = 1
    a_exponential = 1

    lognormal_samples = simulate_lognormal(n, m_lognormal, s2_lognormal)
    logistic_samples = simulate_logistic(n, a_logistic, b_logistic)
    laplace_samples = simulate_laplace(n, a_laplace)
    exponential_samples = simulate_exponential(n, a_exponential)

    true_mean_lognormal = calculate_true_mean_lognormal(m_lognormal, s2_lognormal)
    true_variance_lognormal = calculate_true_variance_lognormal(m_lognormal, s2_lognormal)
    true_mean_logistic = calculate_true_mean_logistic(a_logistic, b_logistic)
    true_variance_logistic = calculate_true_variance_logistic(a_logistic, b_logistic)
    true_mean_laplace = calculate_true_mean_laplace(a_laplace)
    true_variance_laplace = calculate_true_variance_laplace(a_laplace)
    true_mean_exponential = calculate_true_mean_exponential(a_exponential)
    true_variance_exponential = calculate_true_variance_exponential(a_exponential)

    unbiased_mean_lognormal = calculate_unbiased_mean(lognormal_samples)
    unbiased_variance_lognormal = calculate_unbiased_variance(lognormal_samples)
    unbiased_mean_logistic = calculate_unbiased_mean(logistic_samples)
    unbiased_variance_logistic = calculate_unbiased_variance(logistic_samples)
    unbiased_mean_laplace = calculate_unbiased_mean(laplace_samples)
    unbiased_variance_laplace = calculate_unbiased_variance(laplace_samples)
    unbiased_mean_exponential = calculate_unbiased_mean(exponential_samples)
    unbiased_variance_exponential = calculate_unbiased_variance(exponential_samples)

    print_distribution_stats("Lognormal", unbiased_mean_lognormal, true_mean_lognormal, unbiased_variance_lognormal,
                             true_variance_lognormal)
    print_distribution_stats("Logistic", unbiased_mean_logistic, true_mean_logistic, unbiased_variance_logistic,
                             true_variance_logistic)
    print_distribution_stats("Laplace", unbiased_mean_laplace, true_mean_laplace, unbiased_variance_laplace,
                             true_variance_laplace)
    print_distribution_stats("Exponential", unbiased_mean_exponential, true_mean_exponential,
                             unbiased_variance_exponential, true_variance_exponential)

    # Task 3
    fig, axs = plt.subplots(2, 2, figsize=(12, 8))

    axs[0, 0].hist(lognormal_samples, bins=50, density=True, alpha=0.7)
    axs[0, 0].set_title('Lognormal Distribution')
    x_lognormal = np.linspace(0, 10, 1000)
    axs[0, 0].plot(x_lognormal, lognorm.pdf(x_lognormal, s=np.sqrt(s2_lognormal), scale=np.exp(m_lognormal)), 'r-',
                   lw=2)

    axs[0, 1].hist(logistic_samples, bins=50, density=True, alpha=0.7)
    axs[0, 1].set_title('Logistic Distribution')
    x_logistic = np.linspace(-10, 10, 1000)
    axs[0, 1].plot(x_logistic, logistic.pdf(x_logistic, loc=a_logistic, scale=b_logistic), 'r-', lw=2)

    axs[1, 0].hist(laplace_samples, bins=50, density=True, alpha=0.7)
    axs[1, 0].set_title('Laplace Distribution')
    x_laplace = np.linspace(-10, 10, 1000)
    axs[1, 0].plot(x_laplace, laplace.pdf(x_laplace, loc=0, scale=a_laplace), 'r-', lw=2)

    axs[1, 1].hist(exponential_samples, bins=50, density=True, alpha=0.7)
    axs[1, 1].set_title('Exponential Distribution')
    x_exponential = np.linspace(0, 10, 1000)
    axs[1, 1].plot(x_exponential, expon.pdf(x_exponential, scale=1 / a_exponential), 'r-', lw=2)

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    # LabWork1()
    LabWork2()
    # LabWork3()
