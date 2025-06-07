# k-mer index
import bisect


class Index(object):
    def __init__(self, t, k):
        self.k = k
        self.index = []
