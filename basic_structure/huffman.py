from random import random
from basic_structure.mylist import mylist

class node(object):

    def __init__(self, value=None, leftc=None, rightc=None):
        self.leftchild = leftc
        self.rightchild = rightc
        self.sum = value

    def __lt__(self, other):
        return self.sum < other.sum

    def __le__(self, other):
        return self.sum <= other.sum

    def __str__(self):
        return str(self.sum)

    def __repr__(self):
        return str(self)

pl = []
ml = []


def pre_traverse(node):
    if not node:
        return
    pl.append(node)
    pre_traverse(node.leftchild)
    pre_traverse(node.rightchild)

def isleaf(node):
    return not node.leftchild and not node.rightchild


def mid_traverse(node):
    if not node:
        return
    mid_traverse(node.leftchild)
    if isleaf(node):
        ml.append(node)
    mid_traverse(node.rightchild)


def order_traverse(node):
    queue = []
    queue.append(node)
    while len(queue) > 0:
        head = queue.pop(0)
        if head.rightchild:
            queue.append(head.rightchild)
        if head.leftchild:
            queue.append(head.leftchild)
        if isleaf(head):
            ml.append(head)


def huffman(list):
    while len(list)>1:
        left, right = l.pop(0), l.pop(0)
        new = node(left.sum+right.sum, left, right)
        list.insert(list.bin_search(new, 0, len(list)) + 1, new)
    return list[0]



if __name__ == "__main__":
    sum = 0
    r = [node(round(random(), 2)) for i in range(10)]
    for i in r:
        sum += i.sum
    l = mylist(r)
    l.quicksort(0, len(l))
    print(l)
    node = huffman(l)
    order_traverse(node)
    print(ml)



