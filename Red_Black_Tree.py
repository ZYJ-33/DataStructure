from basic_structure.bintreenode import BinTreeNode
from basic_structure.bin_search_tree import (
    BinSearchTree,
    travlevel,
)

class RedBlackTree(BinSearchTree):
    def __init__(self, ele):
        if isinstance(ele, list):
            self.root = BinTreeNode(ele[0], color="B")
            for e in ele[1:]:
                self.insert(e)
        else:
            self.root = BinTreeNode(ele, color="B")

    def insert(self, ele):
        node = self.find(ele)
        if node.data == ele:
            return
        if ele < node.data:
            newnode = node.insert_as_lchild(ele)
        else:
            newnode = node.insert_as_rchild(ele)
        self.solve_double_red(newnode)

    def delete(self, ele):
        succ, old = super(RedBlackTree, self).delete(ele)
        if old.color == "R":
            return old
        else:
            if succ:
                if succ.color == "R":
                    succ.color = "B"
                    return old
                else:
                    self.solve_double_black(succ, old.parent)
                    return old
            else:
                self.solve_double_black(succ, old.parent)


    def from_parent_to_child(self, node, child):       #重写父类同命方法  返回删除节点的替代和删除节点
        if node.islchild():
            node.parent.lchild = child
        else:
            node.parent.rchild = child
        if child is not None:
            child.parent = node.parent
        return child, node

    def solve_BB_1(self, brother):
        parent = brother.parent
        redchild = brother.get_red_child()
        g = parent.parent
        if g:
            if parent.islchild():
                L = True
            else:
                L = False

        if brother.islchild():
            if redchild.islchild():
                brother.color = parent.color
                parent.color = "B"
                redchild.color = "B"
                tmp = self.right_rotate(parent)
            else:
                redchild.color = parent.color
                parent.color = "B"
                tmp = self.reconnect34(brother.lchild, brother, redchild.lchild, redchild, redchild.rchild,
                                       parent, parent.rchild)
        else:
            if redchild.isrchild():
                brother.color = parent.color
                parent.color = "B"
                tmp = self.left_rotate(parent)

            else:
                redchild.color = parent.color
                parent.color = "B"
                tmp = self.reconnect34(parent.lchild, parent, redchild.lchild, redchild, redchild.rchild,
                                       brother, brother.rchild)
            tmp.parent = g
            if g:
                if L:
                    g.lchild = tmp
                else:
                    g.rchild = tmp
            else:
                self.root = tmp
                self.root.parent = None

    def solove_BB_3(self, brother, succ):
        parent = brother.parent
        g = parent.parent
        if g:
            if parent.islchild():
                L = True
            else:
                L = False
        brother.color = "B"
        parent.color = "R"
        if brother.islchild():
            tmp = self.right_rotate(parent)
        else:
            tmp = self.left_rotate(parent)
        tmp.parent = g
        if g:
            if L:
                g.lchild = tmp
            else:
                g.rchild = tmp
        else:
            self.root = tmp
            self.root.parent = None
        self.solve_double_black(succ, parent)

    def solve_BB_2R(self, brother):
        parent = brother.parent
        parent.color = "B"
        brother.color = "R"
        return

    def solve_BB_2B(self, brother):
        brother.color = "R"
        if brother.parent is self.root:
            return
        self.solve_double_black(brother.parent, brother.parent.parent)

    def get_brother(self, parent, node):
        if parent.lchild is node:
            return parent.rchild
        else:
            return parent.lchild

    def solve_double_black(self, succ, parent):
        brother = self.get_brother(parent, succ)
        if brother.color == "B":
            if brother.get_red_child() is not None:
                self.solve_BB_1(brother)
            else:
                if parent.color == "R":
                    self.solve_BB_2R(brother)
                else:
                    self.solve_BB_2B(brother)
        else:
            self.solove_BB_3(brother, succ)

    def get_uncle(self, node):
        p = node.parent
        g = p.parent
        if p.isrchild():
            u = g.lchild
        else:
            u = g.rchild
        return u

    def solve_double_red(self, node):
        p = node.parent
        if p.color == "B":
            return
        g = p.parent
        u = self.get_uncle(node)
        if self.uncle_is_black(node):         # when uncle of node is black
            gg = g.parent
            if gg:
                if g.islchild():
                    L = True
                else:
                    L = False
            g.color = "R"
            if p.islchild():
                if node.islchild():      #LL
                    p.color = "B"
                    tmp = self.reconnect34(node.lchild, node, node.rchild, p, p.rchild, g, g.rchild)
                else:                     #LR
                    node.color = "B"
                    tmp = self.reconnect34(p.lchild, p, node.lchild, node, node.rchild, g, g.rchild)
            else:
                if node.isrchild():     #RR
                    p.color = "B"
                    tmp = self.reconnect34(g.lchild, g, p.lchild, p, node.lchild, node, node.rchild)
                else:                   #RL
                    node.color = "B"
                    tmp = self.reconnect34(g.lchild, g, node.lchild, node, node.rchild, p, p.rchild)
            tmp.parent = gg
            if gg:
                if L:
                    gg.lchild = tmp
                else:
                    gg.rchild = tmp
            else:
                self.root = tmp
        else:                                                 # when node of uncle is red
            if g is self.root:
                g.color = "B"
            else:
                g.color = "R"
            p.color = "B"
            if u:
                u.color = "B"
            if g.color == "R":
                self.solve_double_red(g)

    def uncle_is_black(self, node):
        p = node.parent
        g = p.parent
        if p.isrchild():
            u = g.lchild
        else:
            u = g.rchild
        if u is None or u.color == "B":
            return True
        else:
            return False

    def height(self, node):
        if node is None:
            return -1
        h = max(self.height(node.lchild), self.height(node.rchild))
        if node.color == "B":
            return h + 1
        else:
            return h


def log(node):
    print(node.color + ":" + str(node.data))

if __name__ == "__main__":
    t = RedBlackTree([i for i in range(10)])
    travlevel(t.root, log)
    print("**********")
    t.delete(8)
    travlevel(t.root, log)
    print("**********")
    t.delete(9)
    travlevel(t.root, log)
    print("**********")
    t.delete(4)
    travlevel(t.root, log)
    print("**********")
    t.delete(7)
    travlevel(t.root, log)
    print("**********")
    t.delete(6)
    travlevel(t.root, log)
    print("**********")
    t.delete(5)
    travlevel(t.root, log)

