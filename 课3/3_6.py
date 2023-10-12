def mark(num):
    if num<60:
        print("不合格")
    elif num>=60&num<=74:
        print("合格")
    elif num>=75&num<=89:
        print("良好")
    else:
        print("优秀")

num=67
mark(num)