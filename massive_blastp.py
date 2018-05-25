"""This script is gona make massive blastp to remote NCBI server using sequences stored at
/sequences folder and will store the results at /output folder

Require (Biopython and click)

/sequences and /output folder previously created in the path the script will be runned. All the query fasta file for blastp
have to be at /sequence.
"""


import os,sys
from Bio.Blast.Applications import NcbiblastnCommandline
from Bio import SeqIO
import click
from subprocess import call


current_directory = os.path.dirname(os.path.abspath(__file__))#guarda en la variable el directorio del script
queryDir = current_directory+"/sequences/"
outputDir = current_directory+"/output/"


with click.progressbar(os.listdir(queryDir)) as bar:
    for i in bar:
		if i != ".DS_Store":
			queryFile = queryDir+i
			handle = open(queryFile,"rU")
			record_dict = SeqIO.to_dict(SeqIO.parse(handle, "fasta"))
			handle.close()
			queryFile = queryDir+i
			queryName = record_dict.keys()[0]
			call(["blastp", "-db", "nr", "-query",queryFile,"-out",outputDir+queryName+".txt","-remote"])
