import random
import math
import time
from decimal import Decimal, getcontext


#蒙特卡洛方法
def monte_carlo(all_num):
    inside = 0
    for _ in range(all_num):
        x = random.random()
        y = random.random()
        if x**2 + y**2 <= 1:
            inside += 1
    return 4 * inside / all_num


#Leibniz公式
def leibniz_pi(all_num):
    pi = 0
    for i in range(all_num):
        pi += ((-1)**i) / (2*i + 1)
    return 4 * pi

def chudnovsky_pi(all_num):
    getcontext().prec = 1000  # 设置精度为1000位，根据需要调整

    k = 0
    pi = Decimal(0)
    while k < all_num:
        numerator = Decimal(math.factorial(6*k)) * (545140134*k + 13591409)
        denominator = Decimal(math.factorial(3*k)) * (Decimal(math.factorial(k))**3) * Decimal(640320**(3*k + 3/2))
        term = numerator / denominator
        pi += term
        k += 1

    return 1 / (12 * pi)

# 设置迭代次数
all_num = 15

start_time = time.time()
monte_carlo_result = monte_carlo(all_num)
monte_carlo_time = time.time() - start_time

start_time = time.time()
leibniz_result = leibniz_pi(all_num)
leibniz_time = time.time() - start_time

start_time = time.time()
chudnovsky_result = chudnovsky_pi(all_num)
chudnovsky_time = time.time() - start_time

# 输出结果和计算时间
print(f"蒙特卡洛方法计算π的结果: {monte_carlo_result:.10f}, 耗时 {monte_carlo_time:.6f}秒")
print(f"Leibniz公式计算π的结果: {leibniz_result:.10f}, 耗时 {leibniz_time:.6f}秒")
print(f"Chudnovsky公式计算π的结果: {chudnovsky_result:.10f}, 耗时 {chudnovsky_time:.6f}秒")
