# Read real FASTQ reads


def read_genome(filename):
    genome = ""
    with open(filename, "r") as f:
        for line in f:
            if not line[0] == ">":
                genome += line.rstrip()
    return genome


genome = read_genome("phix.fa")


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

def naive(p, t):
    occurrences = []
    for i in range(len(t) - len(p) + 1):
        match = True
        for j in range(len(p)):
            if not t[i + j] == p[j]:
                match = False
                break
        if match:
            occurrences.append(i)  # Append only the starting index of the match
    return occurrences

phix_reads, _ = read_fastq("ERR266411_1.first1000.fastq")

num_matched = 0
n = 0
for r in phix_reads:
    r = r[:30]
    matches = naive(r, genome)
    n += 1
    if len(matches) > 0:
        num_matched += 1

print(f"Number of reads: {n}\nNumber of matches: {num_matched}")

