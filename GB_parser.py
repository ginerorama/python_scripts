# encoding: utf-8
""" generate a multifasta file from a GBK or GB format file containing all the CDS proteins. It also generate a txt table 
containning information about description, locus_tag and protein sequence.
usage: GB_parser [input gbk]
Require Biopython
"""


from __future__ import division
import sys
from Bio import SeqIO
import pandas as pd 
import sys


try:
	input = sys.argv[1] #"NC_003210.gbk"
except:
    sys.exit("error: too few arguments\nusage: GB_parser [input gbk]... \n") 



sequence_name = str(input.split(".")[0])
#input_genes = str(input.split(".")[0])
outcsv = open(sequence_name+'.csv', 'w')
output = open(sequence_name+'.txt',"w")


with open(input, "rU") as input_handle:
	for record in SeqIO.parse(input_handle, "genbank"):
		for feature in record.features:
			if feature.type == 'CDS':
				start = feature.location.start.position
				stop = feature.location.end.position
				position= int(start)+((int(stop)-int(start))/2)
				orf = feature.qualifiers['protein_id'][0]
				try:
					name = feature.qualifiers['product'][0]
				except:
					name = feature.qualifiers['locus_tag'][0]
				gene = feature.qualifiers['locus_tag'][0]
				protein = feature.qualifiers['translation'][0]
				output.write(">"+str(orf)+"\n")
				output.write(str(protein)+"\n")


				csv_line = "{0},{1},{2},{3}\n".format(gene,orf,name,protein)
				outcsv.write(csv_line)




