"""
十进制转换成n进制

例子: 100转换成8进制-----144
      256除8  商32 余0
      32除8   商4  余0
      4除8    商0  余4
      每次结果的余数进栈, 最后出栈
"""


def decimal_conversion(num, base):
    if base <= 0:
        print("base error")
        return

    if not num:
        print(0)
        return
    if num < base:
        print(num)
        return

    # 商
    quotient = num // base
    # 余数
    remainder = num % base

    # 存放结果的栈
    conver_stack = [remainder]

    while quotient >= base:
        remainder = quotient % base
        quotient = quotient // base
        conver_stack.append(remainder)

    conver_stack.append(quotient)

    for i in range(len(conver_stack)):
        print(conver_stack.pop(), end="")
    print()


decimal_conversion(8644197605847452079, 2)
decimal_conversion(1025, 2)
decimal_conversion(3, 2)
decimal_conversion(1, 2)
decimal_conversion(0, 2)
decimal_conversion(100, 8)
