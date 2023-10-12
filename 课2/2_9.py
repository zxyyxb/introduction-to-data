import random

def monte_carlo(func, a, b, num_samples):
    total = 0
    for _ in range(num_samples):
        x = random.uniform(a, b)
        total += func(x)
    average = total / num_samples
    integral_estimate = average * (b - a)
    return integral_estimate

def f(x):
    return x**2 + 4 * x * math.sin(x)


num_samples = 100000 

import math
estimated_integral = monte_carlo(f, 2, 3, num_samples)
print("定积分值为:", estimated_integral)
