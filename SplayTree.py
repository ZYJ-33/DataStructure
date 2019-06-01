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

    def find(self, ele):
        point = super(SplayTree, self).find(ele)
        while point.parent:
            point = self.rotate(point)
        self.root = point
        return self.root


    def rotate(self, node):
        p = node.parent
        g = p.parent        #may be None
        if g is not None:
            if p.islchild():
                L = True
            else:
                L = False

        if node.islchild():
            new_tree = self.right_reconnect23(node.lchild, node, node.rchild, p, p.rchild)
        else:
            #node.lchild, node, node.rchild, p, p.rchild
            new_tree = self.left_reconnect23(p.lchild, p, node.lchild, node, node.rchild)
        new_tree.parent = g

        if g is not None:
            if L:
                g.lchild = new_tree
            else:
                g.rchild = new_tree

        return new_tree

    #node.lchild, node, node.rchild, p, p.rchild
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
    #p.lchild, p, node.lchild, node, node.rchild
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
    t.delete(22)
    travlevel(t.root, log)

