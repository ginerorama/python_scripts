#!/usr/bin/env python

""" retrieve a DNA sequence located between two genomic positions (seq_start and seq_end).
 The script generate a fasta file with the target sequence 
 Require Biopyton
 """

import sys
from Bio import SeqIO

try:
   input = sys.argv[1]
   seq5= sys.argv[2]
   seq3= sys.argv[3]
   output = sys.argv[4]
except:
    sys.exit("\nERROR: too few arguments\n\nusage: seq_retriever {Fasta file} seq_start seq_end output_file...\n\n"
    "Arguments:\n----------\nFasta_file: input fasta file\nseq_start:  DNA 5' star position\nseq_end:    DNA 3' end position\noutput:     output file (ex. myseq.fa)\n") 


def openfastafile(input):
	record = SeqIO.read(input, "fasta")
	return record
	

def retrieving_sequence(seq5,seq3,record,output):
	output_file = open(output, "w")
	seq5 = int(seq5)
	seq3= int(seq3)
	data = record[seq5:seq3]
	if "." in output:
		output = output.split(".")[0]
	output_file.write(">"+str(output)+"_"+str(seq5)+":"+str(seq3)+"\n"+str(data.seq))
	return ">"+str(output)+"_"+str(seq5)+":"+str(seq3)+"\n"+str(data.seq)

record = openfastafile(input)

retrieving_sequence(seq5,seq3,record,output)