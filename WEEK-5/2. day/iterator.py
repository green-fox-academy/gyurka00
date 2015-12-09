class FibonacciIterator:
    def __init__(self, count):
        self.count = count
        self.i = 0
        self.a = 0
        self.b = 1
        self.curr = 0

    def next(self):
        if self.count <= self.i:
            return False

        self.i += 1
        self.curr = self.a
        self.a, self.b = self.a + self.b,self.a
        return True

    def current(self):
        return self.curr


fibo = FibonacciIterator(10)
while fibo.next():
    print(fibo.current())

class Iterator:
    def __init__(self,list):
        self.list = list
        self.i = 0

    def next(self):
        self.i += 1
        return len(self.list) >= self.i

    def current(self):
        return self.list[self.i-1]

class IteratorPow:
    def __init__(self,list):
        self.list = list
        self.i = 0

    def next(self):
        self.i += 1
        return len(self.list) >= self.i

    def current(self):
        return self.list[self.i-1]**2


print('************')
l = [1,2,3,4,5]
iter = Iterator(l)
while iter.next():
    print(iter.current())

print('************')
iter_pow = IteratorPow(l)
while iter_pow.next():
    print(iter_pow.current())
