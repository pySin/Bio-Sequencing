# k-mer index
import bisect


class Index(object):
    def __init__(self, t, k):
        self.k = k
        self.index = []
        for i in range(len(t) - k + 1):
            self.index.append((t[i:i + k], i))
        self.index.sort()

    def query(self, p):
        kmer = p[:self.k]
        i = bisect.bisect_left(self.index, (kmer, -1))  # -1 is to look for the leftmost first result
        hits = []
        while i < len(self.index):
            if self.index[i][0] != kmer:
                break
            hits.append(self.index[i][1])
            i += 1
        return hits


def query_index(p, t, index):  # p = pattern, t = text(Genome)
    """
    Check if the rest of the pattern matches before authorising the offsets.
    :param p: pattern to look for
    :param t: text to look in (DNA sequence)
    :param index: indexes in "t" where the first k(2) letters from "p" match
    :return: indexes in "t" where the whole of "p" matches (not only the first 2 letters).
    """
    k = index.k
    offsets = []
    for i in index.query(p):  # returns list of possible places where matches of "p" could start
        if p[k:] == t[i + k:i + len(p)]:
            offsets.append(i)
    return offsets


t = "GCTCACGATCTAGAATCTA"
p = "TCTA"
print(Index(t, 2).query(p))
print(query_index(p, t, Index(t, 2)))
