"""
请实现一个函数，将一个字符串中的每个空格替换成“%20”。
例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。
"""


class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        item_list = []
        for c in s:
            if c == " ":
                item_list.append("%20")
            else:
                item_list.append(c)
        return "".join(item_list)

        # return s.replace(" ", "%20")
