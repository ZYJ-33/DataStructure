class BinTreeNode(object):
    def __init__(self, data, parent=None, lchild=None, rchild=None, color=None):
        self.data = data
        self.parent = parent
        self.lchild = lchild
        self.rchild = rchild
        self.color = color

    def insert_as_lchild(self, data):
        self.lchild = BinTreeNode(data, parent=self, color="R")
        return self.lchild

    def insert_as_rchild(self, data):
        self.rchild = BinTreeNode(data, parent=self, color="R")
        return self.rchild

    def haslchild(self):
        return not self.lchild is None

    def hasrchild(self):
        return not self.rchild is None

    def islchild(self):
            if self.parent.lchild is self:
                return True
            return False

    def isrchild(self):
            if self.parent.rchild is self:
                return True
            return False

    def __ge__(self, other):
        return self.data >= other.data

    def __gt__(self, other):
        return self.data > other.data

    def __eq__(self, other):
        return self.data == other.data

    def __lt__(self, other):
        return self.data < other.data

    def get_red_child(self):
        if self.lchild:
            if self.lchild.color == "R":
                return self.lchild
        elif self.rchild:
            if self.rchild.color == "R":
                return self.rchild
        else:
            return None


def size(node):
    if node is None:
        return 0
    return size(node.lchild)+size(node.rchild)+1


def height(node):
    if node is None:
        return -1
    return max(height(node.lchild), height(node.rchild))+1


def travlevel(node, func):
    order = []
    order.append(node)
    while len(order) > 0:
        hotpoint = order.pop(0)
        func(hotpoint)
        if hotpoint.haslchild():
            order.append(hotpoint.lchild)
        if hotpoint.hasrchild():
            order.append(hotpoint.rchild)



def travelpre(node, func):
    if node is None:
        return
    func(node)
    travelpre(node.lchild, func)
    travelpre(node.rchild, func)


def travelin(node, func):
    if node is None:
        return
    travelin(node.lchild, func)
    func(node)
    travelin(node.rchild, func)


def travelpost(node, func):
    if node is None:
        return
    travelpost(node.lchild, func)
    travelpost(node.rchild, func)
    func(node)

