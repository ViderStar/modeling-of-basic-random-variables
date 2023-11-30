from scipy import integrate
import numpy as np
import matplotlib.pyplot as plt

inf = 10e10


def function1(x):
    return x * np.log(x)


def function2(x, y):
    return np.exp(-(x ** 2 + y ** 2) / 2) * np.log(1 + (2 * x - 3 * y) ** 2 + 1e-10)


def monte_carlo_integration1(func, xmin, xmax, num_points):
    x = np.random.uniform(xmin, xmax, num_points)
    integral_sum = np.sum(func(x))
    area = (xmax - xmin)
    integral_value = area * (integral_sum / num_points)
    return integral_value


def monte_carlo_integration2(func, xmin, xmax, ymin, ymax, num_points):
    x = np.random.uniform(xmin, xmax, num_points)
    y = np.random.uniform(ymin, ymax, num_points)
    integral_sum = np.sum(func(x, y), axis=None)
    area = (xmax - xmin) * (ymax - ymin)
    integral_value = area * (integral_sum / num_points)
    return integral_value


# Вычисление первого интеграла
integral1_exact, _ = integrate.quad(function1, 1, 3)
num_iterations = np.arange(100, 10000, 100)
error1 = []

for num_points in num_iterations:
    integral1 = monte_carlo_integration1(function1, 1, 3, num_points)
    error1.append(np.abs(integral1 - integral1_exact))

# Вычисление второго интеграла
integral2_exact, _ = integrate.dblquad(function2, -np.inf, np.inf, -np.inf, np.inf)
print(integral2_exact)
error2 = []

for num_points in num_iterations:
    integral2 = monte_carlo_integration2(function2, -inf, inf, -inf, inf, num_points)
    error2.append(np.abs(integral2 - integral2_exact))

# Построение графика зависимости точности от числа итераций
plt.figure(figsize=(10, 5))
plt.subplot(121)
plt.plot(num_iterations, error1)
plt.xlabel('Number of Iterations')
plt.ylabel('Error')
plt.title('First Integral')

plt.subplot(122)
plt.plot(num_iterations, error2)
plt.xlabel('Number of Iterations')
plt.ylabel('Error')
plt.title('Second Integral')

plt.tight_layout()
plt.show()