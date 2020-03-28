class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    """反转链表, 输出表头"""

    def ReverseList(self, pHead):
        # 空链表或链表只有一个结点
        if pHead is None or pHead.next is None:
            return pHead

        cur_node = pHead
        pre = None

        while cur_node is not None:
            p_next = cur_node.next
            cur_node.next = pre
            pre = cur_node
            cur_node = p_next
        return pre



