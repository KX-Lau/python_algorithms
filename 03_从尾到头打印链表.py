class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # 用栈来存放链表的结点
        val_list = []
        cur_node = listNode
        while cur_node is not None:
            val_list.insert(0, cur_node.val)
            cur_node = cur_node.next
        return val_list
