# DNA -> RNA Transcription
from typing import Union

TRANSCRIPTION_MAPPING = {"A": "U", "C": "G", "T": "A", "G": "C"}
ALLOWED_NUC = TRANSCRIPTION_MAPPING.keys()

def transcribe(seq: str, reverse: bool = False) -> str:
    """
    Write a function that will transcribe (replace DNA sequence to RNA
    by replacing all 'T' to 'U') in an input sequence
    """

    # Test if the input string contains invalid characters
    if not all(char in {'A', 'T', 'C', 'G'} for char in seq):
        print('The input string may contain invalid characters...\n')
        return ''

    transcribed_seq = "".join(TRANSCRIPTION_MAPPING[nuc] for nuc in seq if nuc in ALLOWED_NUC)

    if reverse:
        reversed_seq = transcribed_seq[::-1]
        return reversed_seq

    return transcribed_seq

def reverse_transcribe(seq: str) -> str:
    """
    Write a function that will transcribe an input sequence and reverse
    the sequence
    """
    return transcribe(seq, True)

# Testing cases
print(transcribe('ATCG'))
print(reverse_transcribe('ATCG'))

print(transcribe(''))
print(reverse_transcribe(' '))

