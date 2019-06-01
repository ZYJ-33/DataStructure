from copy import deepcopy
from random import randint

class mylist(list):

    def bubble_sort_update(self, lo, hi):
        while lo < hi:
            hi = self.bubble_update(lo, hi)
            if hi <= lo:
                break

    def greedysort(self, lo, hi):
        lo += 1
        while lo < hi:
            tmp = lo
            while lo > 0 and self[lo-1] > self[lo]:
                self.swap(lo-1, lo)
                lo -= 1
            lo = tmp
            lo += 1

    def bubble_update(self, lo, hi):
        last = lo
        lo += 1
        while lo < hi:
            if self[lo-1] > self[lo]:
                self.swap(lo-1, lo)
                last = lo
            lo += 1
        return last

    def bubble_sort(self, lo, hi):
        while lo < hi:
            if self.bubble(lo, hi):
               break
            else:
                hi -= 1

    def bubble(self, lo, hi):
        been_sort = True
        lo += 1
        while lo < hi:
            if self[lo-1] > self[lo]:
                self.swap(lo-1, lo)
                been_sort = False
            lo += 1
        return been_sort

    def swap(self, a, b):
        t = self[a]
        self[a] = self[b]
        self[b] = t

    def selectmax(self, a, b):
        max = a
        a += 1
        while a < b:
            if self[a] > self[max]:
                max = a
            a += 1
        return max

    def selectsort(self, a, b):
        while b > a:
            max_index = self.selectmax(a, b)
            self.swap(max_index, b-1)
            b -= 1

    def mergesort(self, lo, hi):
        if hi - lo <= 1:
            return
        mi = int((hi + lo)/2)
        self.mergesort(lo, mi)
        self.mergesort(mi, hi)
        self.merge(lo, mi, hi)

    def merge(self, lo, mi, hi):
        tmp = mylist(self[lo:mi])
        left_length = mi-lo
        right_length = hi-mi
        l = r = p = 0
        while l < left_length and r < right_length:
            if tmp[l] < self[mi+r]:
                self[lo+p] = tmp[l]
                l += 1
            else:
                self[lo+p] = self[mi+r]
                r += 1
            p += 1
        while l < left_length:
            self[lo+p] = tmp[l]
            l += 1
            p += 1
        while r < right_length:
            self[lo + p] = self[mi + r]
            r += 1
            p += 1

    def quicksort(self, lo, hi):
        if hi-lo <= 1:
            return
        r = self.partition(lo, hi-1)
        self.quicksort(lo, r+1)
        self.quicksort(r+1, hi)

    def partition(self, lo, hi):
        pivot = self[lo]
        opening = lo
        while lo < hi:
            while pivot <= self[hi] and lo < hi:
                hi -= 1
            self[opening] = self[hi]
            opening = hi
            while self[lo] <= pivot and lo < hi:
                lo += 1
            self[opening] = self[lo]
            opening = lo
        self[lo] = pivot
        return lo

    def is_ordered(self):
        l = len(self)
        i = 1
        while i < l:
            if self[i] < self[i-1]:
                return False
            i += 1
        return True

    def liner_find(self, target, lo=0, hi=None):
        if hi == None:
            hi = len(self)
        for index, item in enumerate(self[lo:hi]):
            if item == target:
                return index
        return -1

    def sorted_liner_find(self, target, lo=0, hi=None):
        if hi == None:
            hi = len(self)

        while lo < hi:
            if self[lo] == target:
                return lo
            elif self[lo] < target:
                lo += 1
            else:
                break
        return lo-1

    def bin_search(self, target, lo=0, hi=None):
        if hi is None:
            hi = len(self)
        while lo < hi:
            mi = int((lo+hi)/2)
            if self[mi] <= target:
                lo = mi + 1
            else:                             #target < self[mi]
                hi = mi
        return lo-1

    def insert_sort(self,lo=0,hi=None):
        if hi is None:
            hi = len(self)
        index = lo + 1
        while index < hi:
            self.insert(self.bin_search(self[index], lo, index)+1, self[index])
            del self[index+1]
            index += 1

    def find_first_less(self, index):
        target = self[index]
        index -= 1
        while index >= 0:
            if self[index] < target:
                return index
            index -= 1
        return index




if __name__ == "__main__":
    v = mylist([5, 4, 2, 9, 12])
    v.quicksort(0, len(v))
    print(v)
    print(v.sorted_liner_find(1))
