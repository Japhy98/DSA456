
class Node:
    def __init__(self, data, next=None, prev=None) -> None:
        self.data = data
        self.next = next
        self.prev = prev

    def get_data(self):
        return self.data


class LinkedList:
    def __init__(self, front=None, back=None) -> None:
        self.sentinel = Node(None)
        self.sentinel.next = self.sentinel
        self.sentinel.prev = self.sentinel
        self.count = 0

    def show(self):
        current = self.sentinel.next
        while current != self.sentinel:
            print(current.data, end=" ")
            current = current.next
        print()

    def get_front(self):
        if self.count == 0:
            return None
        return self.sentinel.next

    def get_back(self):
        if self.count == 0:
            return None
        return self.sentinel.prev

    def insert_front(self, data):
        new_node = Node(data, self.sentinel.next, self.sentinel)
        self.sentinel.next.prev = new_node
        self.sentinel.next = new_node
        self.count += 1

    def insert_back(self, data):
        new_node = Node(data, self.sentinel, self.sentinel.prev)
        self.sentinel.prev.next = new_node
        self.sentinel.prev = new_node
        self.count += 1

    def insert(self, data):
        current = self.sentinel.next

        while current != self.sentinel and current.data < data:
            current = current.next

        new_node = Node(data, current, current.prev)
        current.prev.next = new_node
        current.prev = new_node
        self.count += 1

    def remove(self, data):
        current = self.sentinel.next

        while current != self.sentinel:
            if current.data == data:
                current.prev.next = current.next
                current.next.prev = current.prev
                self.count -= 1
                return True

            if current.data > data:
                return False

            current = current.next

        return False

    def is_present(self, data):
        current = self.sentinel.next

        while current != self.sentinel:
            if current.data == data:
                return True

            if current.data > data:
                return False

            current = current.next

        return False

    def __len__(self):
        return self.count


# Testing
if __name__ == "__main__":
    lst = LinkedList()

    lst.insert(30)
    lst.insert(10)
    lst.insert(20)
    lst.insert(40)
    lst.insert(25)

    print("List after insertions:")
    lst.show()

    print("25 present?", lst.is_present(25))
    print("15 present?", lst.is_present(15))

    print("Remove 20:", lst.remove(20))
    lst.show()

    print("Remove 99:", lst.remove(99))
    print("Length:", len(lst))