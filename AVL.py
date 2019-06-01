from basic_structure.bin_search_tree import (
    BinSearchTree,
    BinTreeNode,
    height,
    log,
)
from basic_structure.bintreenode import travlevel


def factor(node):
    return height(node.lchild) - height(node.rchild)


class AVL(BinSearchTree):
    def insert(self, ele):
        node = super(AVL, self).insert(ele)
        self.ensure_balance_for_insert(node.parent)

    def delete(self, ele):
        node = super(AVL, self).delete(ele)
        if node is not None:
            node = node.parent
            while node:
                f = factor(node)
                if f <= -2 or f >= 2:
                    self.rotate(node)
                node = node.parent

    def find_greater_child(self, node):
        if height(node.lchild) > height(node.rchild):
            return node.lchild
        else:
            return node.rchild

    def ensure_balance_for_insert(self, node):
        while node:
            f = factor(node)
            if f <= -2 or f >= 2:
                self.rotate(node)
                break
            node = node.parent

    def rotate(self, node):
        if node.parent:
            if node.islchild():
                L = True
            else:
                L = False
        p = node.parent         #如果node是根节点 则p为None
        new_tree = self.rotate_at(self.find_greater_child(self.find_greater_child(node)))
        new_tree.parent = p
        if p is not None:
            if L:
                p.lchild = new_tree
            else:
                p.rchild = new_tree
        else:
            self.root = new_tree

    def rotate_at(self, v):
        p = v.parent
        g = p.parent
        if p.islchild():
            if v.islchild():
                return self.reconnect34(v.lchild, v, v.rchild, p, p.rchild, g, g.rchild)
            else:
                return self.reconnect34(p.lchild, p, v.lchild, v, v.rchild, g, g.rchild)
        else:
            if v.isrchild():
                return self.reconnect34(g.lchild, g, p.lchild, p, v.lchild, v, v.rchild)
            else:
                return self.reconnect34(g.lchild, g, v.lchild, v, v.rchild, p, p.rchild)

    def reconnect34(self, t1, a, t2, b, t3, c, t4):
        a.lchild = t1
        a.rchild = t2
        c.lchild = t3
        c.rchild = t4
        b.lchild = a
        b.rchild = c
        a.parent = b
        c.parent = b
        if t1:
            t1.parent = a
        if t2:
            t2.parent = a
        if t3:
            t3.parent = c
        if t4:
            t4.parent = c
        return b






if __name__ == "__main__":
    t = AVL([20, 16, 22, 21, 25, 23])
    travlevel(t.root, log)
    print("*************")
    #t.delete(22)
    #travlevel(t.root, log)






