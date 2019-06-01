from basic_structure.mylist import mylist

class BTreeNode(object):
    def __init__(self, ele=None, lchild=None, rchild=None, parent=None):
        self.parent = parent
        self.keys = mylist()
        self.childs = list()
        if ele is not None:
            self.keys.append(ele)
            self.childs.append(lchild)
            self.childs.append(rchild)
            if lchild is not None:
                lchild.parent = self
            if rchild is not None:
                rchild.parent = self
        else:
            self.childs.append(None)


class BTree(object):
    def __init__(self, order=4):
        self.__root = BTreeNode()
        self.__size = 0
        self.__order = order
        self.__hot = None

    def getroot(self):
        return self.__root

    def split_node(self, oldnode):
        start = len(oldnode.keys)//2
        time = self.__order - start
        newnode = BTreeNode()
        newnode.childs.pop(0)
        while time > 0:
            newnode.keys.append(oldnode.keys.pop(start))
            newnode.childs.append(oldnode.childs.pop(start+1))
            time -= 1
        newnode.parent = oldnode.parent
        return oldnode, newnode


    def __solve_overflow(self, node):
        parent = node.parent
        if len(node.childs) <= self.__order:
            return
        node, newnode = self.split_node(node)
        upper = newnode.keys.pop(0)
        if parent is not None:
            index = parent.keys.sorted_liner_find(upper)
            parent.keys.insert(index+1, upper)
            parent.childs.insert(index+2, newnode)
            self.__solve_overflow(parent)
        else:
            self.__root = BTreeNode(ele=upper, lchild=node, rchild=newnode)

    def findbrothers(self, node):
        parent = node.parent
        index = parent.childs.index(node)
        if index == 0 or index == len(parent.childs)-1:
            if index == 0:
                return None, parent.childs[index+1]
            else:
                return parent.childs[index-1], None
        return parent.childs[index-1], parent.childs[index+1]

    def borrow_key_from_brother(self, node, rightbro=None, leftbro=None):
        if (rightbro and leftbro) or not (rightbro or leftbro):
            raise Exception
        parent = node.parent
        key = node.keys[len(node.keys) - 1] if rightbro else leftbro.keys[len(leftbro.keys) - 1]
        index = parent.keys.sorted_liner_find(key) + 1
        if rightbro:
            node.keys.append(parent.keys[index])
            parent.keys[index] = rightbro.keys.pop(0)
            node.childs.append(rightbro.childs.pop(0))
        else:
            node.keys.insert(0, parent.keys[index])
            parent.keys[index] = leftbro.keys.pop(len(leftbro.keys)-1)
            node.childs.insert(0, leftbro.childs.pop(len(leftbro.childs)-1))

    def emerge_right_to_left(self, left, right, parent, index):
        left.keys.append(parent.keys.pop(index))
        left.childs.append(right.childs.pop(0))
        parent.childs.pop(index + 1)
        time = len(right.keys)
        while time > 0:
            left.keys.append(right.keys.pop(0))
            left.childs.append(right.childs.pop(0))
            time -= 1
        if parent is self.__root and len(parent.keys) == 0:
            self.__root = left
            self.__root.parent = None
        return left

    def emerge(self, node, leftbro=None, rightbro=None):
        if (rightbro and leftbro) or not (rightbro or leftbro):
            raise Exception
        parent = node.parent
        key = node.keys[len(node.keys) - 1] if rightbro else leftbro.keys[len(leftbro.keys) - 1]
        index = parent.keys.sorted_liner_find(key) + 1

        if rightbro:
            return self.emerge_right_to_left(node, rightbro, parent, index)
        else:
            return self.emerge_right_to_left(leftbro, node, parent, index)




    def __solve_underflow(self, node):
        if len(node.childs) >= self.__order//2 or node is self.__root:
            return
        leftbro, rightbro = self.findbrothers(node)
        if rightbro and len(rightbro.keys) >= self.__order//2:
            self.borrow_key_from_brother(node, rightbro=rightbro)
            return
        elif leftbro and len(leftbro.keys) >= self.__order//2:
            self.borrow_key_from_brother(node, leftbro=leftbro)
            return
        else:
            if leftbro:
                node = self.emerge(node, leftbro=leftbro)
            elif rightbro:
                node = self.emerge(node, rightbro=rightbro)
            else:
                raise Exception
            if node.parent:
                self.__solve_underflow(node.parent)



    def find(self, ele):
        hot = node = self.__root
        while node:
            index = node.keys.sorted_liner_find(ele)
            if (index >= 0 and node.keys[index] == ele):
                return node
            else:
                hot = node
                try:
                    node = node.childs[index+1]
                except IndexError:
                    node = None

        self.__hot = hot
        return node



    def insert(self, ele):
        node = self.find(ele)
        if node is not None:
            return
        else:
            node = self.__hot
            index = node.keys.sorted_liner_find(ele)
            node.keys.insert(index+1, ele)
            node.childs.insert(index+2, None)
            self.__size += 1
            self.__solve_overflow(node)





    def delete(self, ele):
        node = self.find(ele)
        if node is None:
            return
        index = node.keys.sorted_liner_find(ele)
        if node.childs[0] is not None:
            tmp = node.childs[index+1]
            if tmp:
                while tmp.childs[0]:
                    tmp = tmp.childs[0]
                node.keys[index] = tmp.keys[0]
                node = tmp
                index = 0
        node.keys.pop(index)
        node.childs.pop(index+1)
        self.__size -= 1
        self.__solve_underflow(node)




def BTree_travel(node):
    if node is None:
        return
    tmp = []
    for i in node.keys:
        tmp.append(i)
    print(tmp)
    for child in node.childs:
        BTree_travel(child)


if __name__ == "__main__":
    b = BTree()
    for i in range(1, 11):
        b.insert(i)
    BTree_travel(b.getroot())
    b.delete(10)
    print("*******************************")
    BTree_travel(b.getroot())
    b.delete(9)
    print("*******************************")
    BTree_travel(b.getroot())
    b.delete(7)
    print("*******************************")
    BTree_travel(b.getroot())
    b.delete(8)
    print("*******************************")
    BTree_travel(b.getroot())
    b.delete(6)
    print("*******************************")
    BTree_travel(b.getroot())
    b.delete(4)
    print("*******************************")
    BTree_travel(b.getroot())
    b.delete(5)
    print("*******************************")
    BTree_travel(b.getroot())
    b.delete(3)
    print("*******************************")
    BTree_travel(b.getroot())

