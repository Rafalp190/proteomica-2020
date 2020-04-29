import argparse
from Bio import SeqIO
from protease import protease_split
from molecular_weight import total_weight

help_text = "Protease used in experiment. Options: Tripsina, Elastasa, Proteinasa-K, ArgC, AspN, Quimiotripsina, GluC, LysC, LysN"
par=argparse.ArgumentParser(description='This script simulates a protein digestion')
par.add_argument('--fasta','-f',dest='fasta',type=str,help='Regular expression for choosing files with the protein sequence',required=True)
par.add_argument('--protease','-p',dest='protease',type=str,help=help_text,required=True)
par.add_argument('--output', '-o', dest='output', type=str, help='Name of the output csv file')

args=par.parse_args()

records = list(SeqIO.parse("./input/"+args.fasta, "fasta"))
for i in range(len(records)):
  split_array = protease_split(args.protease, str(records[i].seq))
  total_weight(split_array, "seq_"+str(i), args.fasta, args.protease, args.output+'_seq'+str(i))