class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node


class SinglyLinkedList:
    def __init__(self):
        self.head = None


    def is_empty(self):
        return self.head is None


    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node


    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next

        current.next = new_node


    def insert_after(self, target, data):
        current = self.head

        while current:
            if current.data == target:
                new_node = Node(data, current.next)
                current.next = new_node
                return
            current = current.next


    def delete(self, target):
        if self.head is None:
            return

        if self.head.data == target:
            self.head = self.head.next
            return

        current = self.head

        while current.next:
            if current.next.data == target:
                current.next = current.next.next
                return
            current = current.next


    def search(self, data):
        current = self.head

        while current:
            if current.data == data:
                return True
            current = current.next

        return False


    def size(self):
        count = 0
        current = self.head

        while current:
            count += 1
            current = current.next

        return count


    def to_list(self):
        result = []
        current = self.head

        while current:
            result.append(current.data)
            current = current.next

        return result


    def print(self):
        current = self.head

        while current:
            print(current.data, end=" -> ")
            current = current.next

        print("None")


# TEST CODE AT THE BOTTOM
if __name__ == "__main__":
    ll = SinglyLinkedList()

    ll.append(10)
    ll.append(20)
    ll.prepend(5)
    ll.insert_after(10, 15)

    ll.print()

    print("Size:", ll.size())
    print("Search 20:", ll.search(20))
    print("List:", ll.to_list())