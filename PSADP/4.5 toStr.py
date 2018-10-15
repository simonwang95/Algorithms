def to_str1(n, base):

    convert_string = "0123456789ABCDEF"
    if n < base:
        return convert_string[n]
    else:
        return to_str1(n // base, base) + convert_string[n % base]
        # 最早生成的余数-->排到最后

print(to_str1(10, 2))

# 栈帧：实现递归
