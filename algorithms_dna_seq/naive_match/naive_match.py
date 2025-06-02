# Naive match




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

t = "AGCTTAGATAGC"
p = "AG"
results_match = naive(p, t)
print(f"Matches: {results_match}")

