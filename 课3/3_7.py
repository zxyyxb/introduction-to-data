def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# 例子
num1 = 48
num2 = 18
result = gcd(num1, num2)
print(f"{num1} 和 {num2} 的最大公约数是 {result}")
