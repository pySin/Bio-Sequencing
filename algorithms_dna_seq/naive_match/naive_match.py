# Naive match
import random


def read_genome(filename):
    genome = ""
    with open(filename, "r") as f:
        for line in f:
            if not line[0] == ">":
                genome += line.rstrip()
    return genome


genome = read_genome("phix.fa")  # Reference genome file


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



# t = "AGCTTAGATAGC"
# p = "AG"
# results_match = naive(p, t)
# print(f"Matches: {results_match}")

# Generate random reads
reads = generate_reads(genome, 100, 100)
# print(f"Reads: {reads}")

num_matched = 0
for r in reads:
    matches = naive(r, genome)
    if len(matches) > 0:
        num_matched += len(matches)

print(f"Matches found: {num_matched} out of {len(reads)} reads.")
