# Human genome Chromosome 1 exploratory
import itertools


class OpenReadChr1:

    def __init__(self, file_path):
        self.file_path = file_path
        self.current_dna_sequence = ""
        self.last_four_characters = ""
        self.pattern_results = {}

    def get_chr1_sequence(self):
        bases_count = {
            "A": 0,
            "T": 0,
            "C": 0,
            "G": 0
        }
        sequence_chr1 = 0
        with open(self.file_path, "r") as f:
            for line in f.readlines()[1:]:
                if line.startswith("N") and line.endswith("N"):
                    continue
                else:
                    for n_base in line:
                        if n_base == "N" or n_base == "\n":
                            continue
                        else:
                            bases_count[n_base] += 1
                            sequence_chr1 += 1
        return sequence_chr1, bases_count

    def triple_nucleotide_follower_ratio(self):
        perms = itertools.product(["A", "T", "G", "C"], repeat=3)
        for perm in perms:
            pattern = "".join(perm)
            self.pattern_results[pattern] = {"A": 0, "T": 0, "G": 0, "C": 0}
        print(f"Patterns dict: {self.pattern_results}")
        patterns = ["ATT", "GCG", "CCC"]

        with open(self.file_path, "r") as f:
            for line in f.readlines()[1:]:
                if line.startswith("N") and line.endswith("N"):
                    continue
                else:
                    for n_base in line:
                        if n_base == "N" or n_base == "\n":
                            continue
                        else:
                            self.current_dna_sequence += n_base
                            if len(self.current_dna_sequence) == 1000:
                                # for pattern in patterns:
                                    # self.follower_of_3_bases_per_1000(self.current_dna_sequence, pattern)
                                self.follower_of_random_length(self.current_dna_sequence, 3)
                                self.current_dna_sequence = self.current_dna_sequence[-4:]
                                # print(f"Add 4 to next 1000: {self.current_dna_sequence}")
                                # print("-=-=---=-=-=-=-==-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-==")
        return self.pattern_results

    def follower_of_3_bases_per_1000(self, seq_1000, pattern):
        if pattern not in self.pattern_results:
            self.pattern_results[pattern] = {"A": 0, "T": 0, "G": 0, "C": 0}
        # print(f"In follower missing 4: {seq_1000[:4]}")

        for i in range(len(pattern), len(seq_1000) - 1):
            # print(f"i: {i}")
            # print(f"i - len pattern: {i - len(pattern)}")
            # print(f"Current Seq: {seq_1000[i - len(pattern): i]}")
            # print(f"Pattern: {pattern}")
            # print(f"1000 seq: {seq_1000}")
            # print(f"First i: {i}, current 3 seq {seq_1000[i - len(pattern): i]}, Current i: {seq_1000[i]}")
            if seq_1000[i - len(pattern): i] == pattern:
                # print(f"Pattern Match!")
                self.pattern_results[pattern][seq_1000[i]] += 1

    def follower_of_random_length(self, seq_1000, length):

        for i in range(length, len(seq_1000) - 1):
            # print(f"i: {i}")
            # print(f"i - len pattern: {i - len(pattern)}")
            # print(f"Current Seq: {seq_1000[i - len(pattern): i]}")
            # print(f"Pattern: {pattern}")
            # print(f"1000 seq: {seq_1000}")
            # print(f"First i: {i}, current 3 seq {seq_1000[i - len(pattern): i]}, Current i: {seq_1000[i]}")
            # if seq_1000[i - len(pattern): i] == pattern:
                # print(f"Pattern Match!")
            self.pattern_results[seq_1000[i - length: i]][seq_1000[i]] += 1


chromosome_1 = OpenReadChr1("Homo_sapiens.GRCh38.dna.chromosome.1.fa")
three_ratio = chromosome_1.triple_nucleotide_follower_ratio()  # Finishes in about a minute and a half
print(three_ratio)
# chromosome_1_seq, bases_count = chromosome_1.get_chr1_sequence()
# print(f"Number of clear chr1 bases: {chromosome_1_seq}")
# print(f"Bases Count: {bases_count}")
# print(f"Bases Count All: {bases_count["A"] + bases_count["T"] + bases_count["C"] + bases_count["G"]}")
