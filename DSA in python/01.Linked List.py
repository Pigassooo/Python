class Node():
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

class LinkedList():
    def __init__(self):
        self.head = None

    def insertatfront(self, value):
        node = Node(value, self.head)
        self.head = node

    def print(self):
        if self.head is None:
            print("LInked List is Empty")
            return

        itr = self.head
        listr = ''
        while itr:
            listr += str(itr.value) + "-->"
            itr = itr.next
        print(listr[:-len("-->")])

    def insertatend(self, value):
        if self.head is None:
            self.head = Node(value)
            return

        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(value)

    def insert_values(self, data_list):
        self.head = None
        for value in data_list:
            self.insertatend(value)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next

        return count

    def remove(self, index):
        if index < 0 or index>=self.get_length():
            raise Exception("Invalid index")

        if index == 0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if count == index-1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1

    def insert_at(self, index, value):
        if index < 0 or index>=self.get_length():
            raise Exception("Invalid index")

        if index == 0:
            self.insertatfront(value)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(value, itr.next)
                itr.next = node
                break
            itr = itr.next
            count += 1


if __name__ == '__main__':
    ll = LinkedList()
    ll.insertatfront(5)
    ll.insertatfront(100)
    ll.insertatend(98)
    ll.insert_values(['China', 'US', 'Australia'])
    ll.remove(1)
    ll.print()
    print('Length:', ll.get_length())
    ll.insert_at(0, 'fig')
    ll.print()




