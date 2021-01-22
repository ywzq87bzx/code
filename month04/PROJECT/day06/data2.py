class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Solution:
    def get_array_list(self, head):
        array_list = []
        cur = head
        while cur:
            array_list.append(cur.value)
            cur = cur.next
        return array_list[::-1]


if __name__ == '__main__':
    s = Solution()
    head = Node(100)
    head.next = Node(200)
    head.next.next = Node(300)
    print(s.get_array_list(head))
