class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class List:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def add_to_tail(self, val):
        node = Node(val)
        if self.head and self.tail:
            last = self.tail
            while last.next:
                last = last.next
            last.next = node
        elif self.head:
            self.head.next = self.tail = node
        else:
            self.head = node
    
    def print(self):
        last = self.head
        output = []
        while last:
            output.append(last.data)
            last = last.next
        return output
    
    def rotate_right(self, k):
        for _ in range(k):
            last = self.head
            prev = None
            while last.next:
                prev = last
                last = last.next
            if prev:
                prev.next = None
                self.tail = self.head
            last.next = self.head
            self.head = last


with open('input.txt') as file:
    file.readline()
    array = map(int, file.readline().split())
    rotations = map(int, file.readlines())

l = List()
for el in array:
    l.add_to_tail(el)

with open('output.txt', 'w') as file:
    for k in rotations:
        l.rotate_right(k)
        print(*l.print(), file=file)



