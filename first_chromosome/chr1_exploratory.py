# Human genome Chromosome 1 exploratory


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
                                self.current_dna_sequence = self.current_dna_sequence[-4:]

    def follower_of_3_bases_per_1000(self, seq_1000, pattern):
        if pattern not in self.pattern_results:
            self.pattern_results[pattern] = {"A": 0, "T": 0, "G": 0, "C": 0}

        for i in range(len(pattern) + 1, len(seq_1000) - 4):
            if seq_1000[i - len(pattern), i] == pattern:
                self.pattern_results[pattern][seq_1000[i]] += 1



chromosome_1 = OpenReadChr1("Homo_sapiens.GRCh38.dna.chromosome.1.fa")
chromosome_1.triple_nucleotide_follower_ratio()  # Finishes in about a minute and a half
# chromosome_1_seq, bases_count = chromosome_1.get_chr1_sequence()
# print(f"Number of clear chr1 bases: {chromosome_1_seq}")
# print(f"Bases Count: {bases_count}")
# print(f"Bases Count All: {bases_count["A"] + bases_count["T"] + bases_count["C"] + bases_count["G"]}")
