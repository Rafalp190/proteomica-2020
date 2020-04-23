import argparse
from Bio import SeqIO
from protease import protease_split

help_text = "Protease used in experiment. Options: Tripsina, Elastasa, Proteinasa-K, ArgC, AspN, Quimiotripsina, GluC, LysC, LysN"
par=argparse.ArgumentParser(description='This script simulates a protein digestion')
par.add_argument('--fasta','-f',dest='fasta',type=str,help='Regular expression for choosing files with the protein sequence',required=True)
par.add_argument('--multiseq','-m' ,dest='m',help='Multi sequence input fasta file',action='store_true')
par.add_argument('--protease','-p',dest='protease',type=str,help=help_text,required=True)

args=par.parse_args()

#FUNCTION FOR MULTISEQUENCE FASTA
if args.m == True:
  records = list(SeqIO.parse("./input/"+args.fasta, "fasta"))
  for record in records:
    split_array = protease_split(args.protease, str(record.seq))
    print(split_array)
    #TODO JULIO
    #ADD WEIGHT FUNCTION
    #ADD PRINT TO CSV with name =  args.fasta_record.id.csv
    #CSV STRUCTURE: args.fasta,record.id,sequence_chunk,weight
else:
#FUNCTION FOR SINGLESEQUENCE FASTA
  records = list(SeqIO.parse("./input/"+args.fasta, "fasta"))
  split_array = protease_split(args.protease, str(records[0].seq))
  print(split_array)
    #TODO JULIO
    #ADD WEIGHT FUNCTION
    #ADD PRINT TO CSV with name =  args.fasta_record.id.csv
    #CSV STRUCTURE: args.fasta,record[0].id,sequence_chunk,weight
