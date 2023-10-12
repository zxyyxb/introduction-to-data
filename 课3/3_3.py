import re

def validate(id_card):
    # 定义中国大陆身份证号的正则表达式模式
    pattern = "(^\d{15}$)|(^\d{18}$)|(^\d{17})(\d|X|x)$"
    
    # 使用正则表达式进行匹配
    if re.match(pattern, id_card):
        return True
    else:
        return False

# 测试函数
id_card_number = "123456789012345671"
if validate(id_card_number):
    print(f"{id_card_number} 是合法的身份证号")
else:
    print(f"{id_card_number} 不是合法的身份证号")
