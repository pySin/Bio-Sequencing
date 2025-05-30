## Complementary base

# def longestCommonPrefix(s1, s2):
#     i = 0
#     while i < len(s1) and i < len(s2) and s1[i] == s2[i]:
#         i += 1
#     return s1[:i]
#
# long_same_part = longestCommonPrefix("ATCGAAGC", "ATCGGGAG")
# print(f"Same Prefix: {long_same_part}")


## Complementary dictionary

# dna_dict = {"A":"T", "T":"A", "G":"C", "C":"G"}
#
# def getComplimentaryString(string):
#
#     c_string = "".join([dna_dict[l] for l in string])
#     return c_string
#
# print(getComplimentaryString("AATTCC"))

## Download genome

# import IPython

# IPython.!wget --no-check https://d28rh4a8wq0iu5.cloudfront.net/ads1/data/lambda_virus.fa

def read_genome(filename):
    genome = ""
    with open(filename, "r") as f:
        for line in f:
            if not line[0] == ">":
                genome += line.rstrip()
    return  genome

genome_red = read_genome("lambda_virus.fa")
print(f"Genome sequence: {genome_red}")
