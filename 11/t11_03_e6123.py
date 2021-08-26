class Stack(list):
    def push(self, n):
        self.append(int(n))
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
    def back(self):
        return self[-1]

    def size(self):
        return len(self)
    
    def clear(self):
        self.clear()
        return 'ok'
    
    def exit(self):
        return 'bye'


operations = [line.split() for line in open('input.txt').readlines()]

s = Stack()
op = {'push': s.push,
      'pop': s.pop,
      'back': s.back,
      'size': s.size,
      'clear': s.clear,
      'exit': s.exit}

with open('output.txt', 'w') as file:
    for operation, *args in operations:
        res = op[operation](*args)
        print(res, file=file)
        if res == 'bye': break