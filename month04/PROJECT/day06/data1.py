class Node:
    """节点类"""

    def __init__(self, value):
        self.value = value
        self.next = None


class SingleLinkList:
    """单链表类"""

    def __init__(self, node=None):
        """创建链表时: s=SingleLinkList()表示空链表,s=SingleLinkList(Node(100)) 表示有1个节点的单链表"""
        self.head = node

    def is_empty(self):
        """判断链表是否为空"""
        return self.head == None

    def lengh(self):
        """获取链表长度"""
        # 游标：从头节点开始,一直往后移动,移动一次,+1
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.next

        return count

    def travel(self):
        """遍历整个链表"""
        current = self.head
        while current is not None:
            print(current.value, end=" ")
            current = current.next
        # 因为上面是end=" ",所以此处打印一个换行
        print()

    def add(self, item):
        """链表头部添加1个节点"""
        node = Node(item)
        # 1、把新添加的节点指针指向原来头节点
        node.next = self.head
        # 2、添加的节点设置为新的头
        self.head = node

    def append(self, item):
        """链表尾部添加1个节点,考虑空链表特殊情况"""
        node = Node(item)
        if self.is_empty():
            self.head = node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            # 循环结束后,current指向尾节点
            current.next = node
            node.next = None

    def remove(self, item):
        pre = None
        cur = self.head
        while cur:
            if cur.value != item:
                pre = cur
                cur = cur.next
            else:
                pre.next = cur.next
                return


if __name__ == '__main__':
    s = SingleLinkList()
    # 终端1：True
    print(s.is_empty())
    # 链表：Node(100) -> Node(200) -> Node(300)
    s.add(200)
    s.add(100)
    s.append(300)

    # 终端3：100 200 300
    s.travel()
    s.remove(300)
    s.travel()
