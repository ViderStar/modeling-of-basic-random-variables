import numpy as np
from matplotlib import pyplot as plt

from generators import mkm_generator, macLarenMarsaglia
from distributions import bernoulli, binomial, unbiased_mean, unbiased_variance, true_mean_bernoulli, \
    true_variance_bernoulli, true_mean_binomial, true_variance_binomial


def LabRabota1():
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


def LabRabota2():
    n = 1000
    p_bernoulli = 0.2
    m_binomial = 6
    p_binomial = 0.75

    bernoulli_numbers = bernoulli(n, p_bernoulli)
    binomial_numbers = binomial(n, m_binomial, p_binomial)

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

    true_mean_bernoulli_var = true_mean_bernoulli(p_bernoulli)
    true_variance_bernoulli_var = true_variance_bernoulli(p_bernoulli)
    true_mean_binomial_var = true_mean_binomial(m_binomial, p_binomial)
    true_variance_binomial_var = true_variance_binomial(m_binomial, p_binomial)

    print("\nBernoulli:")
    print("Unbiased mean:", bernoulli_mean)
    print("True mean:", true_mean_bernoulli_var)
    print("Unbiased variance:", bernoulli_variance)
    print("True variance:", true_variance_bernoulli_var)

    print("\nBinomial:")
    print("Unbiased mean:", binomial_mean)
    print("True mean:", true_mean_binomial_var)
    print("Unbiased variance:", binomial_variance)
    print("True variance:", true_variance_binomial_var)


if __name__ == "__main__":
    LabRabota1()
    LabRabota2()
