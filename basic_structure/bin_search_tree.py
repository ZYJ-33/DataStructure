from basic_structure.bintreenode import (
    BinTreeNode,
    travelin,
    travelpre,
    travlevel,
    size,
    height,
)
from basic_structure.mylist import mylist
from random import randint

class BinSearchTree():
    def __init__(self, ele=None):
        if isinstance(ele, list):
            self.root = BinTreeNode(ele[0])
            for e in ele[1:]:
                self.insert(e)
        else:
            self.root = BinTreeNode(ele)
        self.hot = None

    @classmethod
    def set_as_rchild(cls, parent, child):
        parent.rchild = child
        if child:
            child.parent = parent

    @classmethod
    def set_as_lchild(cls, parent, child):
        parent.lchild = child
        if child:
            child.parent = parent

    @classmethod
    def set_as_child(cls, parent, lchild, rchild):
        cls.set_as_lchild(parent, lchild)
        cls.set_as_rchild(parent, rchild)

    @classmethod
    def reconnect34(cls, t1, a, t2, b, t3, c, t4):
        cls.set_as_child(a, t1, t2)
        cls.set_as_child(c, t3, t4)
        cls.set_as_child(b, a, c)
        return b

    def insert(self, ele):
        node = self.find(ele)
        if node.data == ele:
            return node
        elif ele < node.data:
            return node.insert_as_lchild(ele)
        else:
            return node.insert_as_rchild(ele)

    def delete(self, ele):
        node = self.find(ele)
        if node.data == ele:
            return self._delete(node)
        else:
            return None

    def from_parent_to_child(self, node, child):
        if node.islchild():
            node.parent.lchild = child
        else:
            node.parent.rchild = child
        if child is not None:
            child.parent = node.parent
        return node

    def _delete(self, node):
        if node.haslchild() and node.hasrchild():
            closest = self._find_closest(node)
            node.data, closest.data = closest.data, node.data
            return self._delete(closest)
        elif node.haslchild():
            return self.from_parent_to_child(node, node.lchild)
        elif node.hasrchild():
            return self.from_parent_to_child(node, node.rchild)
        else:
            return self.from_parent_to_child(node, None)

    @staticmethod
    def _find_closest(node):
        point = node.rchild
        while point.haslchild():
            point = point.lchild
        return point

    def find(self, value):
        "find the node which data same as value, if can't find the node , return last node been found"
        hot = point = self.root
        while point is not None:
            if value == point.data:
                return point
            elif value > point.data:
                hot = point
                point = point.rchild
            else:
                hot = point
                point = point.lchild
        return hot

    @classmethod
    def left_rotate(cls, point):
        rchild = point.rchild
        cls.set_as_rchild(point, rchild.lchild)
        cls.set_as_lchild(rchild, point)
        return rchild

    @classmethod
    def right_rotate(cls, point):
        lchild = point.lchild
        cls.set_as_lchild(point, lchild.rchild)
        cls.set_as_rchild(lchild, point)
        return lchild

    @classmethod
    def reconnect34(cls, t1, a, t2, b, t3, c, t4):
        cls.set_as_child(a, t1, t2)
        cls.set_as_child(c, t3, t4)
        cls.set_as_child(b, a, c)
        return b



def log(node):
    print(node.data)

if __name__ == "__main__":
     tree = BinSearchTree([20, 16, 22, 21, 25, 23])
     node = tree.delete(22)
     print(node.data)
     travlevel(tree.root, log)