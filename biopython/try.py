import Bio
from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML


## Find the origin of unknown DNA sequence. ->

# print(f"Biopython version: {Bio.__version__}")
# fasta_string = open("myseq.fa").read()
# result_handle = NCBIWWW.qblast("blastn", "nt", fasta_string)
# blast_record = NCBIXML.read(result_handle)
# print(f"Alignments: {len(blast_record.alignments)}")
#
# E_VALUE_THRESH = 0.01
#
# for alignment in blast_record.alignments:
#     for hsp in alignment.hsps:
#         if hsp.expect < E_VALUE_THRESH:
#             print(f"****Alignment****")
#             print(f"sequence: {alignment.title}")
#             print(f"length: {alignment.length}")
#             print(f"e value: {hsp.expect}")
#             print(f"match: {hsp.match}")
#             print(f"alignment subject: {hsp.sbjct}")

## Create a random DNA sequence
import random


class RandomString:

    def __init__(self):
        self.alphabet = "ATGC"

    def create_dna_sequence(self):
        rand_seq = "".join([random.choice(self.alphabet) for i in range(30)])
        return rand_seq


def call():
    rs = RandomString()
    random_seq = rs.create_dna_sequence()
    print(f"Random Sequence: {random_seq}")

if __name__ == "__main__":
    call()


