def binary(num , precision=8):
    binary_integer=bin(int(num))[2:]
    fraction=num-int(num)
    binary_fra=""

    for _ in range(precision):
        fraction *= 2
        bit =int(fraction)
        binary_fra +=str(bit)
        fraction -=bit

    result=binary_integer +"."+binary_fra
    return result

num=10.625
result=binary(num)
print(result)