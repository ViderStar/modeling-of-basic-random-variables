from matplotlib import pyplot as plt
from distributions import *
from scipy.stats import lognorm, logistic, laplace, expon


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
