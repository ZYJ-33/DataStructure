from flask import request, Flask
f = Flask()
f.before_request
f.after_request
request.endpoint
class stack(list):
    def empty(self):
        return len(self) == 0

    def push(self, e):
        self.append(e)

    def top(self):
        return self[len(self)-1]

    def __iter__(self):
        while not self.empty():
            yield self.pop()

    def find(self, ele):
        last = len(self)-1
        while last >= 0:
            if self[last] == ele:
                return last
            last -= 1
        return last





def transform(value, basic):
    s = stack()
    while value > 0:
        s.push(value % basic)
        value = int(value/basic)
    return s


def pattern_check(string):
    s = stack()
    for char in string:
        if char in ('(', '[', '{'):
            s.push(char)
        elif char in (')', ']', '}'):
            if s.empty():
                return False
            top = s.top()
            if top == '(' and char == ')':
                s.pop()
            elif top == '[' and char == ']':
                s.pop()
            elif top == '{' and char == '}':
                s.pop()
            else:
                return False
    return s.empty()



class queen(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.y == other.y or self.x+self.y == other.x+other.y or self.x-self.y == other.x - other.y

    def copyself(self):
        cls = self.__class__
        return cls(self.x, self.y)


def nqueen(n):
    s = stack()
    q = queen(0, 0)
    nsolu = 0
    while q.y < n or q.x > 0:
        while s.find(q) >= 0 and q.y < n:
            q.y += 1
        if q.y < n :
            s.push(q.copyself())
            if len(s) == n:
                nsolu += 1
                print(nsolu)
            else:
                q.x += 1
                q.y = 0
        elif q.y >= n or len(s) == n:
            q = s.pop()
            q.y += 1
    return nsolu



if __name__ == "__main__":
    print(nqueen(9))

