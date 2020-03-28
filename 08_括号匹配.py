"""
括号匹配

输入: "()[]{}" 输出true
输入："([)]" 输出false
输入：")(()))" 输出false
输入："()" 输出true
输入："((([])))" 输出true
输入："]][[" 输出false
输入：([)] 输出false
"""


def bracket_match_v1(brackets_str):
    brackets_dict = {'(': ')', '[': ']', '{': '}'}

    # 右括号开头
    if brackets_str[0] in brackets_dict.values():
        return False

    # 左括号开头
    brackets_stack = []
    for bracket in brackets_str:
        # 左括号进栈
        if bracket in brackets_dict.keys():
            brackets_stack.append(bracket)

        # 右括号 去匹配栈顶元素是否对应
        elif bracket in brackets_dict.values():
            if brackets_dict[brackets_stack.pop()] != bracket:
                return False

    if not brackets_stack:
        return True

    return False


def bracket_match_v2(brackets_str):
    """简化版"""
    brackets_dict = {')': '(', ']': '[', '}': '{'}
    brackets_stack = []
    for bracket in brackets_str:
        # 左括号
        if bracket in brackets_dict.values():
            brackets_stack.append(bracket)
        # 右括号, 包含右括号开头
        elif not brackets_stack or brackets_dict[bracket] != brackets_stack.pop():
            return False

    return not brackets_stack


print(bracket_match_v1("()[]{}"))
print(bracket_match_v1("([)]"))
print(bracket_match_v1(")(()))"))
print(bracket_match_v1("()"))
print(bracket_match_v1("((([])))"))
print(bracket_match_v1("]][["))
print(bracket_match_v1("([)]"))

print('-' * 66)

print(bracket_match_v2("()[]{}"))
print(bracket_match_v2("([)]"))
print(bracket_match_v2(")(()))"))
print(bracket_match_v2("()"))
print(bracket_match_v2("((([])))"))
print(bracket_match_v2("]][["))
print(bracket_match_v2("([)]"))
