import argparse

help_text = "Protease used in experiment. Options: Tripsina, Elastasa, Proteinasa K, ArgC, AspN, Quimiotripsina, GluC, LysC, LysN"
par=argparse.ArgumentParser(description='This script simulates a protein digestion')
par.add_argument('--fasta','-f',dest='fasta',type=str,help='Regular expression for choosing files with the protein sequence',required=True)
par.add_argument('--protease','-p',dest='protease',type=str,help=help_text,required=True)
args=par.parse_args()