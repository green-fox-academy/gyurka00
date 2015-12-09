class Node:
    def __init__(self,value,left = None,right = None):
        self.value = value
        self.left = left
        self.rigth = right


root =Node(
    1,          #value
    Node(2),    #left
    Node(3)     #right
)

class LeftIterator():
    def __init__(self,root):
        self.curr = root

    def next(self):
        return self.curr is not None

    def current(self):
        tmp = self.curr
        self.curr = self.curr.left
        return tmp

iter = LeftIterator(root)
while iter.next():
    print(iter.current().value)
