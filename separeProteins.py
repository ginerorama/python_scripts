#!/usr/bin/env python

import os,sys
from Bio import SeqIO

current_directory = os.path.dirname(os.path.abspath(__file__))
queryFile = sys.argv[1]
outDir = current_directory+"/sequences/"


handle = open(queryFile,"rU")
record_dict = SeqIO.parse(handle, "fasta")

outArray = []
for record in record_dict:
	record.name = record.id
	record.description = record.id
	record.id = record.id
	outArray.append(record)
	handleLoop = open(outDir+record.id+".fa","w")
	SeqIO.write([record],handleLoop,"fasta")
	handleLoop.close()

handle.close()
