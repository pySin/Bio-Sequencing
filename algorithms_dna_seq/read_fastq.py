# with open("SRR835775_1.first1000.fastq", "r") as f:
#     for line in f:
#         print(f"Line: {line}")

import matplotlib.pyplot as plt
import collections


count = collections.Counter()

def read_fastq(filename):
    sequences = []
    qualities = []
    with open(filename) as f:
        while True:
            f.readline()
            seq = f.readline().rstrip()
            f.readline()
            qual = f.readline().rstrip()
            if len(seq) == 0:
                break
            sequences.append(seq)
            qualities.append(qual)
    return sequences, qualities


def phred33ToQ(qual):
    return ord(qual) - 33



seqs, quals = read_fastq("SRR835775_1.first1000.fastq")
# print(f"Sequences: {seqs[:2]}")
# print(f"Qualities: {quals[:30]}")

# print(phred33ToQ("J"))

def create_hist(qualities):
    hist = [0] * 50
    for qual in qualities:
        for phred in qual:
            q = phred33ToQ(phred)
            hist[q] += 1
    return hist

histo = create_hist(quals)
# print(f"Histo: {histo}")
# plt.bar(range(len(histo)), histo)
#
# plt.show()

def find_gc_by_pos(reads):
    gc = [0] * 100
    totals = [0] * 100

    for read in reads:
        for i in range(len(read)):
            if read[i] == "C" or read[i] == "G":
                gc[i] += 1
            totals[i] += 1

    for i in range(len(gc)):
        if totals[i] > 0:
            gc[i] /= float(totals[i])
    return gc

# gc = find_gc_by_pos(seqs)
# plt.plot(range(len(gc)), gc)
# plt.show()

for seq in seqs:
    count.update(seq)
print(f"Bases Frequency: {count}")
