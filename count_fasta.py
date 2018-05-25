
"""
this script count the number of fasta entries and the length of the different sequence of 
a multifasta file
Require: Biopython

usage python count_fasta <file.fasta>

"""



import sys
from Bio import SeqIO




file = sys.argv[1] 
frame = sys.argv[2]
fasta = open(file,"r")

def fasta_count (file):
	fasta_number= 0
	for line in file:
		if line[0]==">":
			fasta_number += 1
	
	print fasta_number


def fasta_length (file):
	seq_dict = {}
	record_dict = SeqIO.parse(file, "fasta")
	for record in record_dict:
		name = record.id
		seq = record.seq
		length = len(seq)
		seq_dict[name]= len(seq)
		print name, length 
	print (sorted(seq_dict.items(), key = lambda x : x[1]))





fasta_count(fasta)	
fasta_length(file)
