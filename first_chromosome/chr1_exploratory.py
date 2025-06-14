# Human genome Chromosome 1 exploratory


class OpenReadChr1:

    def __init__(self, file_path):
        self.file_path = file_path

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


chromosome_1 = OpenReadChr1("Homo_sapiens.GRCh38.dna.chromosome.1.fa")
chromosome_1_seq, bases_count = chromosome_1.get_chr1_sequence()
print(f"Number of clear chr1 bases: {chromosome_1_seq}")
print(f"Bases Count: {bases_count}")
print(f"Bases Count All: {bases_count["A"] + bases_count["T"] + bases_count["C"] + bases_count["G"]}")
