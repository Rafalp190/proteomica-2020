import argparse

par=argparse.ArgumentParser(description='This script simulates a protein digestion')
par.add_argument('--fasta','-f',dest='fasta',type=str,help='Regular expression for choosing files with the protein sequence',required=True)
par.add_argument('--protease','-p',dest='protease',type=str,help='Protase used in experiment.',required=True)
args=par.parse_args()