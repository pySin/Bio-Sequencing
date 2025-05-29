class SortFastaFile:

    def __init__(self, filename):
        self.filename = filename
        self.seqs = {}

    def read_fasta(self):
        try:
            f_file = open(self.filename, "r")
        except IOError:
            print(f"{self.filename} does not exist!")

        for line in f_file:
            # Remove new line at end of row
            line = line.rstrip()

            # Check if line is header
            if line[0]==">":
                words = line.split()
                name = words[0][1:]
                self.seqs[name] = ""
            else:  # Sequence is not a header
                self.seqs[name] += line
        print(f"FASTA dict: {self.seqs}")
        f_file.close()



def caller():
    f_file = SortFastaFile("gene.fna")
    f_file.read_fasta()


if __name__ == "__main__":
    caller()


