class Stack(list):
    def push(self, x):
        self.append(x)
    
    def get_min(self):
        return min(self)


with open('input.txt') as file:
    n = int(file.readline())
    operations = [list(map(int, line.split())) for line in file.readlines()]

s = Stack()
op = [None, s.push, s.pop, s.get_min]

with open('output.txt', 'w') as file:
    for operation, *args in operations:
        res = op[operation](*args)
        if operation == 3: print(res, file=file)