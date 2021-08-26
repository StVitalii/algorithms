class PriorityQueue(dict):    
    def add(self, id, priority):
        self[id] = priority
    
    def pop(self):
        id, priority = max(self.items(), key=lambda x: x[1])
        return id, super().pop(id)


operations = [line.split() for line in open('input.txt').readlines()]

pq = PriorityQueue()
op = {'ADD': pq.add,
      'POP': pq.pop,
      'CHANGE': pq.add}

with open('output.txt', 'w') as file:
    for operation, *args in operations:
        res = op[operation](*args)
        if res: print(*res, file=file)
