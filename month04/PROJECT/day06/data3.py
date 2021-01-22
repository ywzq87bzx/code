class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Solution:
    def reverse_link_list(self, head):
        # 1、空链表情况
        if head == None:
            return
        # 2、非空链表情况
        pre = None
        cur = head
        while cur:
            # 记录下一个要操作反转的节点
            next_node = cur.next
            # 反转节点cur,并移动两个游标
            cur.next = pre
            pre = cur
            cur = next_node



        return pre.value

if __name__ == '__main__':
    s = Solution()
    # 1、空链表情况
    head = None
    print(s.reverse_link_list(head))
    # 2、只有1个节点情况
    head = Node(100)
    print(s.reverse_link_list(head))
    # 3、有多个节点情况
    head = Node(100)
    head.next = Node(200)
    head.next.next = Node(300)
    print(s.reverse_link_list(head))