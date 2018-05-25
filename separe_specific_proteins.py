#!/usr/bin/env python

import os,sys
from Bio import SeqIO


current_directory = os.path.dirname(os.path.abspath(__file__))

try:
	queryFile = sys.argv[1]
	targetFile = sys.argv[2]
	outDir = current_directory+"/output/"
except:
	sys.exit("separe_specific_Proteins script\nRetrieve all proteins or genes from a fasta file using an IDs-containing list file .txt\n\nusage:separe_specific_Proteins.py <list_IDs.txt> <target.fasta>")


handle = open(targetFile,"rU")
record_dict = SeqIO.parse(handle, "fasta")



protein_list=[]

proteins = open(queryFile,"rU")
for line in proteins:
	protein_name=line.rstrip("\n")
	protein_list.append(protein_name)


print protein_list

outArray = []
for record in record_dict:
	record.name = record.id
	record.description = record.id
	record.id = record.id
	if record.name in protein_list:
		outArray.append(record)
		handleLoop = open(outDir+record.name+".fa","w")
		SeqIO.write([record],handleLoop,"fasta")
		handleLoop.close()

handle.close()
