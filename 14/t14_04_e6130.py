def _err_handler(func):
        def wrapper(self):
            try: return func(self)
            except IndexError: return 'error'
        return wrapper


class Deque(list):
    def push_front(self, x):
        self.insert(0, x)
        return 'ok'
    
    def push_back(self, x):
        self.append(int(x))
        return 'ok'
    
    @_err_handler
    def pop_front(self):
        return self.pop(0)
    
    @_err_handler
    def pop_back(self):
        return self.pop()
    
    @_err_handler
    def front(self):
        return self[0]
    
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

d = Deque()
op = {'push_front': d.push_front,
      'push_back': d.push_back,
      'pop_front': d.pop_front,
      'pop_back': d.pop_back,
      'front': d.front,
      'back': d.back,
      'size': d.size,
      'clear': d.clear,
      'exit': d.exit}

with open('output.txt', 'w') as file:
    for operation, *args in operations:
        res = op[operation](*args)
        print(res, file=file)
        if res == 'bye': break