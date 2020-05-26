class Node(object):

    def __init__(self, item=None, nxt = None):
        self.item = item
        self.nxt = nxt

    def get_item(self):
        return self.item

    def get_nxt(self):
        return self.nxt

    def set_nxt(self, nxt):
        self.nxt = nxt

    def __repr__(self):
        return str(self.item) + " , " + str(self.nxt)


class Linked_list(object):
    def __init__(self, head =None, size=0):
        self.head = head
        self.size = size

    def __str__(self):
        return str(self.head)

    def _get_size(self):
        return self.size

    def _is_empty(self):
        return self.size == 0

    def _add_size(self):
        self.size += 1

    def _minus_size(self):
        self.size -= 1

    def insert_front(self, item):
        if self._is_empty():
            self.head = Node(item)
        else:
            self.head = Node(item, self.head)
        self._add_size()

    def insert_after(self, item, p):
        if type(p) != int:
            raise Exception ("p가 정수형이 아닙니다.")
        if self._get_size() <= p or p < 0:
            raise Exception ("p가 index 범위를 초과합니다.")
        node = self.head
        for i in range(p):
            node = node.nxt
        node.nxt = Node(item, node.nxt)

        self._add_size()

    def print_reverse(self):
        if self._is_empty():
            print("비어있습니다.")
            return
        self._post_order(self.head)
        print()

    def _post_order(self, node):
        if node is None:
            return
        self._post_order(node.nxt)
        print(node.item, end=" ")

    def print_out(self):
        if self._is_empty():
            print("비어있습니다.")
            return
        self._pre_order(self.head)
        print()

    def _pre_order(self, node):
        if node is None:
            return
        print(node.item, end=" ")
        self._pre_order(node.nxt)

    def delete_front(self):
        if self._is_empty():
            raise Exception ("지울게 없어요")
        self.head = self.head.nxt
        self._minus_size()



linked_list = Linked_list()
linked_list.insert_front(3)
linked_list.insert_front(4)
linked_list.insert_front(5)
linked_list.insert_front(5)
linked_list.insert_front(5)
linked_list.delete_front()

linked_list.print_reverse()
linked_list.print_out()




