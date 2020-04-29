import argparse
from Bio import SeqIO
from protease import protease_split
from molecular_weight import total_weight

help_text = "Protease used in experiment. Options: Tripsina, Elastasa, Proteinasa-K, ArgC, AspN, Quimiotripsina, GluC, LysC, LysN"
par=argparse.ArgumentParser(description='This script simulates a protein digestion')
par.add_argument('--fasta','-f',dest='fasta',type=str,help='Regular expression for choosing files with the protein sequence',required=True)
par.add_argument('--multiseq','-m' ,dest='m',help='Multi sequence input fasta file',action='store_true')
par.add_argument('--protease','-p',dest='protease',type=str,help=help_text,required=True)
par.add_argument('--output', '-o', dest='output', type=str, help='Name of the output csv file')

args=par.parse_args()

#FUNCTION FOR MULTISEQUENCE FASTA
if args.m == True:
  records = list(SeqIO.parse("./input/"+args.fasta, "fasta"))
  for i in range(len(records)):
    split_array = protease_split(args.protease, str(records[i].seq))
    #print(split_array)
    #TODO JULIO
    #ADD WEIGHT FUNCTION
    #ADD PRINT TO CSV with name =  args.fasta_record.id.csv
    #CSV STRUCTURE: args.fasta,record.id,sequence_chunk,weight
    total_weight(split_array, "seq_"+str(i), args.fasta, args.protease, args.output+'_seq'+str(i))
else:
#FUNCTION FOR SINGLESEQUENCE FASTA
  records = list(SeqIO.parse("./input/"+args.fasta, "fasta"))
  split_array = protease_split(args.protease, str(records[0].seq))
    #TODO JULIO
    #ADD WEIGHT FUNCTION
    #ADD PRINT TO CSV with name =  args.fasta_record.id.csv
    #CSV STRUCTURE: args.fasta,record[0].id,sequence_chunk,weight
  total_weight(split_array, "seq_0", args.fasta, args.protease, args.output)