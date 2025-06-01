# with open("SRR835775_1.first1000.fastq", "r") as f:
#     for line in f:
#         print(f"Line: {line}")


def read_fastq(filename):
    sequences = []
    qualities = []

