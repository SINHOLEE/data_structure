'''
양방향 링크드 리스트

'''
class Node(object):
    def __init__(self, item):
        self.data = item
        self.prev = None
        self.next = None

    def get_next(self):
        return self.next

    def set_next(self, next):
        self.next = next

    def get_prev(self):
        return self.prev

    def set_prev(self, prev):
        self.prev = prev

    def get_data(self):
        return self.data


class DoublyLinkedList(object):
    def __init__(self):
        self.size = 0
        self.head = Node(None)
        self.tail = Node(None)
        self.head.set_prev(None)
        self.head.set_next(self.tail)
        self.tail.set_prev(self.head)
        self.tail.set_next(None)

    def get_head(self):
        return self.head

    def get_tail(self):
        return self.tail

    def __repr__(self):
        if self.is_empty():
            return 'LinkedList: empty'

        s = ''
        curr = self.head
        while curr.next.next:
            curr = curr.next
            s += repr(curr.data)
            if curr.next.next is not None:
                s += ' '
        return s

    def _add_size(self):
        self.size += 1

    def _minus_size(self):
        self.size -= 1

    def is_empty(self):
        return self.size == 0

    def get_size(self):
        return self.size

    def traverse(self, reverse=False):
        result = []
        if not reverse:
            curr = self.get_tail()
            while curr.get_prev().get_prev():
                curr = curr.get_prev()
                result.append(curr.get_data())
        else:
            curr = self.get_head()
            while curr.get_next().get_next():
                curr = curr.get_next()
                result.append(curr.get_data())

        return result

    def _get_at(self, pos):
        if pos < 0 or pos > self.get_size():
            return None

        if pos > self.get_size() // 2:
            i = 0
            curr = self.get_tail()
            while i < self.get_size() - pos + 1:
                curr = curr.get_prev()
                i += 1
        else:
            i = 0
            curr = self.get_head()
            while i < pos:
                curr = curr.get_next()
                i += 1
        return curr

    def _insert_after(self, prev, new_node):
        next = prev.get_next()
        new_node.set_prev(prev)
        new_node.set_next(next)
        prev.set_next(new_node)
        next.set_prev(new_node)
        self.size += 1
        return True

    def insert_at(self, pos, item):
        if pos < 0 or pos > self.get_size():
            raise Exception ("out of range")
        prev = self._get_at(pos)
        return self._insert_after(prev, Node(item))

    def my_append(self, item):
        new_node = Node(item)
        tail_prev = self.tail.get_prev()

        self.tail.set_prev(new_node)
        tail_prev.set_next(new_node)
        new_node.set_prev(tail_prev)
        new_node.set_next(self.tail)
        self._add_size()

    def insert_front(self, item):
        new_node = Node(item)
        head_next = self.head.get_next()

        self.head.set_next(new_node)
        new_node.set_next(head_next)
        head_next.set_prev(new_node)
        new_node.set_prev(self.head)
        self._add_size()

    def pop(self):
        target = self.tail.get_prev()
        target_prev = target.get_prev()

        target_prev.set_next(self.tail)
        self.tail.set_prev(target_prev)
        self._minus_size()
        return target.get_data()

    def pop_zero(self):
        target = self.head.get_next()
        target_next = target.get_next()

        self.head.set_next(target_next)
        target_next.set_prev(self.head)
        self._minus_size()
        return target.get_data()


if __name__ == "__main__":
    linked_list = DoublyLinkedList()
    linked_list.my_append(2)
    linked_list.my_append("asd")
    linked_list.my_append(4)
    linked_list.my_append(3)
    linked_list.insert_front(976)
    print(linked_list.size)
    linked_list.insert_at(4, 12312312312312)
    print(linked_list.traverse())
    print(linked_list.pop())
    print(linked_list.traverse())
    print(linked_list.pop_zero())
    print(linked_list.traverse())
    print(linked_list.get_size())
    print(linked_list)
    print(linked_list.traverse())
    print(linked_list.traverse(reverse=True))
