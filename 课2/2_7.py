def cubic_root(c, g, tolerance=1e-6, max_iterations=100):
    x = g
    for i in range(max_iterations):
        x_next = (2 * x + c / (x ** 2)) / 3
        if abs(x_next - x) < tolerance:
            return x_next
        x = x_next
    return x

c = 10
g = 1.0 
cubic_root = cubic_root(c, g)
print(f"{c}的立方根是：{cubic_root}")
