# with open("SRR835775_1.first1000.fastq", "r") as f:
#     for line in f:
#         print(f"Line: {line}")


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

print(create_hist(quals))
