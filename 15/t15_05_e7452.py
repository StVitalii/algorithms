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

    def _fill_output(func):
        def wrapper(self):
            self.output = []
            self._last = self.head
            while self._last:
                func(self)
                self._last = self._last.next
            return self.output
        return wrapper
    
    @_fill_output
    def print(self):
        self.output.append(self._last.data)
    
    @_fill_output
    def print_reverse(self):
        self.output.insert(0, self._last.data)


n, *array = map(int, open('input.txt').read().split())

l = List()
for el in array:
    l.add_to_tail(el)

with open('output.txt', 'w') as file:
    print(*l.print(), file=file)
    print(*l.print_reverse(), file=file)



