#MRO = Mthod Resolution Order

class A:
    num = 10

class B(A):
    pass

class C(A):
    num = 1

class D (B, C):
    pass


#http://www.srikanthtechnologies.com/blog/python/mro.aspx

