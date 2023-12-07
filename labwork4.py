import numpy as np
import matplotlib.pyplot as plt


def LabWork4():
    def function1(x):
        return x * np.log(x)

    def function2(x, y):
        return np.exp(-(x ** 2 + y ** 2) / 2) * np.log(1 + (2 * x - 3 * y) ** 2)

    def monte_carlo_integration(func, bounds, num_samples=1000):
        dim = len(bounds)
        samples = np.random.rand(num_samples, dim)
        for i in range(dim):
            samples[:, i] = samples[:, i] * (bounds[i][1] - bounds[i][0]) + bounds[i][0]
        sample_evaluations = func(*samples.T)
        integral = np.mean(sample_evaluations) * np.prod([bound[1] - bound[0] for bound in bounds])
        return integral, np.std(sample_evaluations) / np.sqrt(num_samples)

    bounds1 = [(1, 3)]
    bounds2 = [(-100, 100), (-100, 100)]

    num_samples = np.logspace(1, 5, 10).astype(int)
    errors1 = []
    errors2 = []

    for n in num_samples:
        integral1, error1 = monte_carlo_integration(function1, bounds1, n)
        integral2, error2 = monte_carlo_integration(function2, bounds2, n)
        errors1.append(error1)
        errors2.append(error2)

    print(f"Integral of function1: {integral1}")
    print(f"Integral of function2: {integral2}")

    plt.figure(figsize=(10, 5))

    plt.subplot(121)
    plt.loglog(num_samples, errors1, 'o-')
    plt.xlabel('Number of Iterations')
    plt.ylabel('Error')
    plt.title('First Integral')

    plt.subplot(122)
    plt.loglog(num_samples, errors2[::-1], 'o-')
    plt.xlabel('Number of Iterations')
    plt.ylabel('Error')
    plt.title('Second Integral')

    plt.tight_layout()
    plt.show()
