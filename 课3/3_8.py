import random

# 生成随机数列
def generate_random_sequence(length):
    return [random.randint(1, 1000) for _ in range(length)]

# 选择排序算法
def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr 

# 归并排序算法
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
    return arr  

num_lists = 5  # 生成5组随机数列
list_length = 100  # 每组数列的长度

for i in range(num_lists):
    random_list = generate_random_sequence(list_length)
    print(f"随机数列 {i + 1} 原始数据：{random_list}")
    
    # 选择排序
    sorted_list_selection = selection_sort(random_list.copy())
    print(f"选择排序后：{sorted_list_selection}")
    
    # 归并排序
    sorted_list_merge = merge_sort(random_list.copy())
    print(f"归并排序后：{sorted_list_merge}")
    print()
