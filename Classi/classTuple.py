class C:
    def __init__(self,N):
        self.tuple = tuple([0]*N)
    
    def prnt(self):
        print self.tuple
    
    def sum(self, i, k):
        my_list = list(self.tuple)
        my_list[i] += k
        self.tuple = tuple(my_list)


class D(C):
    def new(self, N, j):
        self.tuple2 = tuple([j]+[0]*N-1)
        print self.tuple2