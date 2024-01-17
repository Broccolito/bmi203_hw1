from seqparser import (
        FastaParser,
        FastqParser,
        transcribe,
        reverse_transcribe)

def main():
    """
    The main function
    """
    # Create instance of FastaParser
    # Create instance of FastqParser
        
    # For each record of FastaParser, Transcribe the sequence
    # and print it to console
       
    fasta_parser = FastaParser('./tests/good.fa')
    fasta_records = list(fasta_parser)

    print("\n\n")
    print("Printing transcribed fasta sequence...\n")
    for fasta_sequence in fasta_records:
        print(transcribe(fasta_sequence[1]))


    # For each record of FastqParser, Transcribe the sequence
    # and print it to console

    fastq_parser = FastqParser('./tests/good.fq')
    fastq_records = list(fastq_parser)
    
    print("\n\n")
    print("Printing transcribed fastq sequence...\n")
    for fastq_sequence in fastq_records:
        print(transcribe(fastq_sequence[1]))


    # For each record of FastaParser, Reverse Transcribe the sequence
    # and print it to console

    print("\n\n")
    print("Printing reverse transcribed fasta sequence...\n")  
    for fasta_sequence in fasta_records:
        print(reverse_transcribe(fasta_sequence[1]))

       
    # For each record of FastqParser, Reverse Transcribe the sequence
    # and print it to console
    
    print("\n\n")
    print("Printing reverse transcribed fastq sequence...\n")  
    for fastq_sequence in fastq_records:
        print(reverse_transcribe(fastq_sequence[1]))


"""
When executing a python script from the command line there will
always be a hidden variable `__name__` set to the value `__main__`.

Since this is guaranteed you can execute your `main` function with
the following if statement
"""
if __name__ == "__main__":
    main()
