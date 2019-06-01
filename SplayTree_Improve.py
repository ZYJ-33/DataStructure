from basic_structure.bin_search_tree import (
    BinSearchTree,
    BinTreeNode,
    travlevel,
    log,
)

class SplayTree(BinSearchTree):
    def forming_newnode(self, be_replace, ele):
        newnode = BinTreeNode(ele, parent=self.root)
        if be_replace is not None:
            if newnode < be_replace:
                newnode.rchild = be_replace
            else:
                newnode.lchild = be_replace
            be_replace.parent = newnode
        return newnode

    def find(self, ele):
        node = super(SplayTree, self).find(ele)
        self.splay(node)

    def insert(self, ele):
        self.find(ele)
        if self.root.data == ele:
            return self.root
        elif self.root.data < ele:
           self.root.rchild = self.forming_newnode(self.root.rchild, ele)
        elif ele < self.root.data:
           self.root.lchild = self.forming_newnode(self.root.lchild, ele)


    def delete(self, ele):
        self.find(ele)
        if self.root.data == ele:
            return super(SplayTree, self)._delete(self.root)
        else:
            return None

    def update_g_p_gp(self, node):
        p = node.parent
        L = None
        if p is not None:
            g = p.parent
            if g is not None:
                gp = g.parent
            else:
                gp = None
        else:
            g = gp = None
        if gp is not None:
            if g.islchild():
                L = True
            else:
                L = False
        return p, g, gp, L

    def splay(self, node):
        p, g, gp, L= self.update_g_p_gp(node)
        while g and p:      #当node有父节点和祖父节点的时候  对应双旋操作

            if p.islchild():
                if node.islchild():
                    node = self.left_left_34(node.lchild, node, node.rchild, p, p.rchild, g, g.rchild)
                else:
                    node = self.left_right_or_right_left_34(p.lchild, p, node.lchild, node, node.rchild, g, g.rchild)
            else:
                if node.isrchild():
                    node = self.right_right_34(g.lchild, g, p.lchild, p, node.lchild, node, node.rchild)
                else:
                    node = self.left_right_or_right_left_34(g.lchild, g, node.lchild, node, node.rchild, p, p.rchild)

            node.parent = gp
            if gp:
                if L:
                    self.set_as_lchild(gp, node)
                else:
                    self.set_as_rchild(gp, node)
            p, g, gp, L = self.update_g_p_gp(node)   # 可能返回p,g,None,None  p,None,None,None  p,g,gp,L

        if p:               #当node只有父节点的时候对应一次单旋操作
            if node.islchild():
                node = self.right_reconnect23(node.lchild, node, node.rchild, p, p.rchild)
            else:
                node = self.left_reconnect23(p.lchild, p, node.lchild, node, node.rchild)
        node.parent = None
        self.root = node

            #更新根节点的值

    def left_left_34(self, t1, a, t2, b, t3, c, t4):
        self.set_as_child(c, t3, t4)
        self.set_as_child(b, t2, c)
        self.set_as_child(a, t1, b)
        return a

    def right_right_34(self, t1, a, t2, b, t3, c, t4):
        self.set_as_child(a, t1, t2)
        self.set_as_child(b, a, t3)
        self.set_as_child(c, b, t4)
        return c

    def left_right_or_right_left_34(self, t1, a, t2, b, t3, c, t4):
        self.set_as_child(a, t1, t2)
        self.set_as_child(c, t3, t4)
        self.set_as_child(b, a, c)
        return b

    def right_reconnect23(self, t1, a, t2, b, t3):
        '''
        return the tree like  a
                            t1  b
                               t2  t3
        '''
        b.lchild = t2
        b.rchild = t3
        a.lchild = t1
        a.rchild = b
        b.parent = a
        if t1:
            t1.parent = a
        if t2:
            t2.parent = b
        if t3:
            t3.parent = b
        return a

    def left_reconnect23(self, t1, a, t2, b, t3):
        '''
        return the tree like    b
                              a   t3
                            t1 t2
        '''
        a.lchild = t1
        a.rchild = t2
        b.rchild = t3
        b.lchild = a
        a.parent = b
        if t1:
            t1.parent = a
        if t2:
            t2.parent = a
        if t3:
            t3.parent = b
        return b


if __name__ == "__main__":
    t = SplayTree([20, 16, 22, 21, 25, 23])
    travlevel(t.root, log)
    print("****************")
    t.find(16)
    t.find(22)
    t.find(20)
    travlevel(t.root, log)
