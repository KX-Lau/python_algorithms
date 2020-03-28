class Solution:
    """两个栈实现一个队列"""

    def __init__(self):
        # 接收栈
        self.accept_stack = []
        # 输出栈
        self.output_stack = []

    def push(self, item):
        """进队列"""
        self.accept_stack.append(item)

    def pop(self):
        """出队列"""

        if not self.output_stack:
            # 输出栈为空, 接收栈不为空
            while self.accept_stack:
                self.output_stack.append(self.accept_stack.pop())

        return self.output_stack.pop()


