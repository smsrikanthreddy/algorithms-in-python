#!/usr/bin/env python

import sys
sys.path.append("../")
from linear_probing_hash_st import LinearProbingHashST as HashST

class SparseVector(object):
    """docstring for SparseVector"""
    def __init__(self, N): # N is the number of elements including zeors
        self.__st = HashST()
        self.__N = N

    def size(self):
        return st.size()

    def put(self, i, x):
        self.__st.put(i, x)

    def get(self, i):
        if not self.__st.contains(i):
            return 0.0
        else:
            return self.__st.get(i)

    def dot(self, that):
        result = 0.0 
        for i in self.__st._keys():
            result += that.get(i) * self.get(i)
        return result

    def plus(self, that):
        result = SparseVector(self.__N)
        index = set(self.__st._keys()) | set(that.__st._keys())
        for i in index:
            tmp = self.get(i) + that.get(i)
            if tmp is not 0:
                result.put(i, tmp)
        return result

    def minus(self, that):
        result = SparseVector(self.__N)
        index = set(self.__st._keys()) | set(that.__st._keys())
        for i in index:
            tmp = self.get(i) - that.get(i)
            if tmp is not 0:
                result.put(i, tmp)
        return result

    def show(self):
        print '[',
        for i in range(self.__N):
            print self.get(i),
        print ']'

if __name__ == '__main__':
    import random
    a = range(10)
    sv = SparseVector(10)
    index = range(10)
    index = random.sample(index, 5)
    print index
    for i in index:
        sv.put(i, a[i])
    print sv.dot(sv)
    sv.plus(sv).show()
    sv.minus(sv).show()