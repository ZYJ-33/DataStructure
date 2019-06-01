from basic_structure.mylist import mylist
from random import randint

class heapnode():
    ...

class heap(mylist):
    @staticmethod
    def parentof(rank):
        return int((rank - 1) / 2)

    @staticmethod
    def rightchild(rank):
        return (rank+1)*2

    @staticmethod
    def leftchild(rank):
        return rank*2+1

    def lastofinterval(self):
        if len(self) > 1:
            return int((len(self)-2)/2)
        return 0

    def have_rightchild(self, rank, n):
        return (rank+1)*2 < n

    def have_leftchild(self, rank, n):
        return rank*2+1 < n

    def greater(self, left, right):
        if self[left] > self[right]:
            return left
        else:
            return right

    def insert(self, value):
        self.append(value)
        self.percolateup(len(self)-1)

    def percolateup(self, rank):
        upper = self[rank]
        pr = self.parentof(rank)
        while self[pr] < upper and rank > 0:
            self[rank] = self[pr]
            rank = pr
            pr = self.parentof(rank)
        self[rank] = upper

    def heaplify_up_version(self, other):
        self.clear()
        for item in other:
            self.insert(item)
        del other

    def heaplify_down_version(self):
        rank = self.lastofinterval()
        while rank >= 0:
            self.percolatedown(rank, len(self))
            rank -= 1


    def heaplify_self(self):
        lo = 1
        hi = len(self)
        while lo < hi:
            self.percolateup(lo)
            lo += 1


    def heap_sort(self):
        self.heaplify_down_version()
        last = len(self)-1
        while last > 0:
            self.swap(0, last)
            self.percolatedown(0, last)
            last -= 1




    def percolatedown(self, rank, n):
        downer = self[rank]
        posible = self.proper_parent(rank, downer, n)
        while posible is not None:
            self[rank] = self[posible]
            rank = posible
            posible = self.proper_parent(rank, downer, n)
        self[rank] = downer


    def proper_parent(self, rank, downer, n):
        haverc = self.have_rightchild(rank, n)
        havelc = self.have_leftchild(rank, n)
        if havelc and haverc:
            posible = self.greater(self.leftchild(rank), self.rightchild(rank))
            if downer > self[posible]:
                return None
            return posible
        elif havelc:
            posible = self.leftchild(rank)
            if downer > self[posible]:
                return None
            return posible
        elif haverc:
            posible = self.rightchild(rank)
            if downer > self[posible]:
                return None
            return posible
        else:
            return None


    def get_max(self):
        return self[0]

    def set_max(self, index):
        self[0] = self[index]

    def del_max(self):
        max = self.get_max()
        self.set_max(len(self)-1)
        self.percolatedown(0)
        return max



if __name__ == "__main__":
    h = heap([randint(0, 100)for i in range(10)])
    h.heap_sort()
    print(h)
