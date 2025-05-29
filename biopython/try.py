import Bio
from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML

print(f"Biopython version: {Bio.__version__}")
fasta_string = open("myseq.fa").read()
result_handle = NCBIWWW.qblast("blastn", "nt", fasta_string)
blast_record = NCBIXML.read(result_handle)
print(f"Alignments: {len(blast_record.alignments)}")

E_VALUE_THRESH = 0.01

for alignment in blast_record.alignments:
    for hsp in alignment.hsps:
        if hsp.expect < E_VALUE_THRESH:
            print(f"****Alignment****")
            print(f"sequence: {alignment.title}")
            print(f"length: {alignment.length}")
            print(f"e value: {hsp.expect}")
            print(f"match: {hsp.match}")
            print(f"subject: {hsp.sbjct}")

