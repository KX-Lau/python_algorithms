"""
在一个二维数组中（每个一维数组的长度相同），
每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
"""


# array = [[1, 2, 3], [4, 5, 6]]

class Solution:

    def Find(self, target, array):
        if not array:
            return False
        for row in array:
            for item in row:
                if item == target:
                    return True
        else:
            return False

    # def Find(self, target, array):
    #     # 二维数组的行数
    #     row = len(array)
    #     # 二维数组的列数
    #     col = len(array[0])
    #     for i in range(row):
    #         for j in range(col):
    #             if array[i][j] == target:
    #                 return True
    #     else:
    #         return False
