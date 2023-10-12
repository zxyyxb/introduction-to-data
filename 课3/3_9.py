def except_self(nums):
    n = len(nums)
    B = [1] * n
    
    # 计算左侧元素的乘积
    for i in range(n):
        for j in range(0,i,1):
            B[i] *= nums[j]
           
        for k in range(i+1,n, 1):
            B[i] *= nums[k]
    
    return B

# 示例输入
str=input(" 输入数组:")
A=[int(item) for item in str.split(",")]
B = except_self(A)
print(B)