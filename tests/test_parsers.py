# write tests for parsers

from seqparser import (
        FastaParser,
        FastqParser)

import pytest


def test_freebie_parser_1():
    """
    This one is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert True # things after the assert are true statements


def test_freebie_parser_2():
    """
    This too is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert 1 != 2


def test_FastaParser():
    """
    Write your unit test for your FastaParser class here. You should generate
    an instance of your FastaParser class and assert that it properly reads in
    the example Fasta File.

    Some example of "good" test cases might be handling edge cases, like Fasta
    files that are blank or corrupted in some way. Two example Fasta files are
    provided in /tests/bad.fa and /tests/empty.fa
    """

    """
    Test FastaParser with a normal fasta file.
    """
    fasta_parser = FastaParser('./tests/good.fa')
    records = list(fasta_parser)
    assert len(records) == 3
    assert records[0] == ("sequence_1", "ACGGACCACCATGAA")
    assert records[1] == ("sequence_2", "ACGGACCTGAA")

    """
    Test FastaParser with an empty fasta file.
    """
    fasta_parser = FastaParser('./tests/blank.fa')
    with pytest.raises(ValueError):
        list(fasta_parser)


    """
    Test FastaParser with a badly formatted fasta file.
    """
    fasta_parser = FastaParser('./tests/bad.fa')
    with pytest.raises(ValueError):
        list(fasta_parser)

    pass


def test_FastaFormat():
    """
    Test to make sure that a fasta file is being read in if a fastq file is
    read, the first item is None
    """

    fasta_parser = FastaParser('./tests/good.fq')
    records = list(fasta_parser)
    assert records[0][0] == None

    pass


def test_FastqParser():
    """
    Write your unit test for your FastqParser class here. You should generate
    an instance of your FastqParser class and assert that it properly reads 
    in the example Fastq File.
    """

    """
    Test FastaParser with a normal fastq file.
    """
    fastq_parser = FastqParser('./tests/good.fq')
    records = list(fastq_parser)
    assert len(records) == 3
    assert records[0] == ("seq0", "TGTGGTCGTATAGTTATTGTCATAAATTACACAGAATCG", "*540($=*,=.062565,2>'487')!:&&6=,6,*7>:")
    assert records[1] == ("seq1", "CCCCGGACGACTGATCCCGATAGAGCTCACTCTTCGAGG", "'(<#/0$5&!$+,:=%7=50--1;'(-7;0>=$(05*9,")

    """
    Test FastaParser with an empty fastq file.
    """
    fastq_parser = FastqParser('./tests/blank.fq')
    with pytest.raises(ValueError):
        list(fastq_parser)


    """
    Test FastaParser with a badly formatted fastq file.
    """
    fastq_parser = FastqParser('./tests/bad.fq')
    with pytest.raises(ValueError):
        list(fastq_parser)

    pass

def test_FastqFormat():
    """
    Test to make sure fastq file is being read in. If this is a fasta file, the
    first line is None
    """

    fastq_parser = FastqParser('./tests/good.fa')
    records = list(fastq_parser)
    assert records[0][0] == None

    pass