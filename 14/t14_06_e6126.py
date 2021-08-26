class Queue(list):
    def push(self, x):
        self.insert(0, x)
        return 'ok'
    
    def _err_handler(func):
        def wrapper(self):
            try: return func(self)
            except IndexError: return 'error'
        return wrapper
    
    @_err_handler
    def pop(self):
        return super().pop()
    
    @_err_handler
    def front(self):
        return self[-1]
    
    def size(self):
        return len(self)
    
    def clear(self):
        self.clear()
        return 'ok'
    
    def exit(self):
        return 'bye'


operations = [line.split() for line in open('input.txt').readlines()]

q = Queue()
op = {'push': q.push,
      'pop': q.pop,
      'front': q.front,
      'size': q.size,
      'clear': q.clear,
      'exit': q.exit}

with open('output.txt', 'w') as file:
    for operation, *args in operations:
        res = op[operation](*args)
        print(res, file=file)
        if res == 'bye': break