import sys
import getopt


class SortFastaFile:
    """
    Create a dictionary
    """
    def __init__(self, filename):
        self.filename = filename
        self.seqs = {}

    def read_fasta(self):
        try:
            f_file = open(self.filename, "r")
            print(f"Arguments: {sys.argv}")
        except Exception:
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
        # print(f"FASTA dict: {self.seqs}")
        f_file.close()


    def show_sequences(self):
        for key, value in self.seqs.items():
            print(f"Name: {key}")
            print(f"Value: {value}")

    def usage(self):
        print(f"Some options connected with the arguments received from the command line.")

    def arg_options(self):
        o, a = getopt.getopt(sys.argv[1:], "l:h")
        opts = {}
        seqlen = 0

        for k, v in o:
            opts[k] = v

        if "-h" in opts.keys():
            print(f"Exiting!")
            self.usage(); sys.exit()


def caller():

    # print(f"Command line arguments: {sys.argv}")
    file_name = sys.argv[1]
    f_file = SortFastaFile(file_name)
    f_file.read_fasta()
    # f_file.show_sequences()
    f_file.arg_options()


if __name__ == "__main__":
    caller()


