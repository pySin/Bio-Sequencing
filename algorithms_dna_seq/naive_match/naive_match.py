# Naive match
import random


def read_genome(filename):
    genome = ""
    with open(filename, "r") as f:
        for line in f:
            if not line[0] == ">":
                genome += line.rstrip()
    return genome


genome = read_genome("phix.fa")


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


def generate_reads(genome, num_reads, read_len):
    #  Random reads from genome
    reads = []
    for _ in range(num_reads):
        start = random.randint(0, len(genome) - read_len) - 1
        reads.append(genome[start: start + read_len])
    return reads



t = "AGCTTAGATAGC"
p = "AG"
results_match = naive(p, t)
print(f"Matches: {results_match}")

