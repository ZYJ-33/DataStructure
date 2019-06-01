class listnode(object):
    def __init__(self, value = None):
        self.value = value
        self.before = None
        self.after = None

    def insertasbefore(self, value):
        beforenode = self.before
        if beforenode is None:
            return
        node = listnode(value)
        beforenode.after = node
        self.before = node
        node.after = self
        node.before = beforenode

    def insertasafter(self, value):
        afternode = self.after
        if afternode is None:
            return
        node = listnode(value)
        afternode.before = node
        self.after = node
        node.before = self
        node.after = afternode

class linklist(object):
    def __init__(self):
        self.header = listnode()
        self.trail = listnode()
        self.trail.before = self.header
        self.header.after = self.trail
        self.size = 0

    def __repr__(self):
        string = ''
        for item in self:
            string = string + ' ' + str(item)

    def insertaslast(self, value):
        self.trail.insertasbefore(value)
        self.size += 1

    def insertasfirst(self, value):
        self.header.insertasafter(value)
        self.size += 1

    def find(self, value):
        for node in self:
            if node.value == value:
                return node

    def drop(self, node):
        before = node.before
        after = node.after
        before.after = after
        after.before = before
        node.before = None
        node.after = None
        value = node.value
        self.size -= 1
        del node
        return value

    def remove(self, value):
        return self.drop(self.find(value))

    def delete(self, index):
        p = self.header.after
        while index > 0:
            p = p.after
            index -= 1
        return self.drop(p)

    def __iter__(self):
        p = self.header.after
        while p is not self.trail:
            yield p
            p = p.after
        raise StopIteration

    def select_sort(self):
        count = self.size
        last = self.trail
        while count > 0:
            max = self.select_max(count)
            last.insertasbefore(self.drop(max))
            count -= 1
            last = last.before

    def select_max(self, count):
        max = self.header.after
        for index, node in enumerate(self):
            if index < count:
                if node.value > max.value:
                    max = node
            else:
                break
        return max

    def find_suitable(self, node):
        ordered = node.before
        while ordered is not self.header:
            if node.value >= ordered.value:
                return ordered
            ordered = ordered.before
        return ordered

    def insert_sort(self):
        start = self.header.after
        while start is not self.trail:
            point = self.find_suitable(start)
            tmp = start.after
            point.insertasafter(self.drop(start))
            start = tmp

    def merge_sort(self, node, length):
        if length <= 1:
            return
        count = mid = int(length/2)
        mi = node
        while count > 0:
            mi = mi.after
            count -= 1
        self.merge_sort(node, mid)
        self.merge_sort(mi, length-mid)
        self.merge(node, mid, mi, length-mid)

    def merge(self, lo, n, mi, m):
        pp = lo.before
        while m > 0:
            if n > 0 and lo.value <= mi.value:
                lo = lo.after
                n -= 1
            elif mi.value < lo.value:
                lo.insertasbefore(mi.value)
                tmp = mi.after
                self.drop(mi)
                mi = tmp
                m -= 1
            else:
                break
        lo = pp.after


    def quick_sort(self, start, length):
        end = start
        count = length - 1
        while count > 0:
            end = end.after
            count -= 1
        self.__quick_sort(start, end)

    def check2(self, start, end):
        c = []
        while start is not end:
            c.append(start.value)
            start = start.after
        c.append(start.value)
        print(c)

    def __quick_sort(self, start, end):
        if start is end :
            return
        pivot = self.partition(start, end)
        if pivot is not start:
            self.__quick_sort(start, pivot.before)
        if pivot is not end:
            self.__quick_sort(pivot.after, end)

    '''
    def check(self):
        c = []
        for item in self:
            c.append(item.value)
        print(c)
    '''
    '''
    def partition(self, start, end):
        pivot = listnode()
        pivot.value = start.value
        opening = start
        while end is not start:
                while pivot.value <= end.value and end is not start:
                    end = end.before
                opening.value = end.value
                opening = end
                while start.value <= pivot.value and end is not start:
                    start = start.after
                opening.value = start.value
                opening = start
        start.value = pivot.value
        return start
    '''

    def partition(self, start, end):
        pivot = start.value
        while end is not start:
            while pivot <= end.value and end is not start:
                end = end.before
            start.value = end.value
            while start.value <= pivot and end is not start:
                start = start.after
            end.value = start.value
        end.value = pivot
        return end







def my_iter(target, function):
    iterator = iter(target)
    while True:
        try:
            function(next(iterator))
        except StopIteration:
            return

from random import randint
if __name__ == "__main__":
    ll = linklist()
    l = [randint(0, 100000) for i in range(10000)]
    print(l)
    contain = []
    for item in l:
        ll.insertaslast(item)
    ll.quick_sort(ll.header.after, ll.size)
    for item in ll:
        contain.append(item.value)
    print(contain)





