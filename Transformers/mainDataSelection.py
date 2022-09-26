import argparse
#MAIN ARGUMENTS
parser= argparse.ArgumentParser()
parser.add_argument('-en', dest='evalue',action='store_true')
parser.add_argument('--en', dest='evalue', action='store_false')
parser.add_argument('-qsel',dest='qselect', help="Question Selection", type=int)
parser.add_argument('-csel',dest='cselect', help="Content Selection", type=int)

args=parser.parse_args()
"""_summary_
        Brief documentation about the arguments parser
         Arguments : 
         -en select the English Transformer for use it.
         --en indicates the you dont use the English Transformer.
         the transformer requires the following parameters:
        -qsel is the question selection for the model 
         -csel is the context selection for the model
    
"""
from roberta import*
from dataModule import*
def main():
    if(args.evalue):
        q,c=qaSelection(args.qselect,args.cselect)
        print(qa(q,c))

if __name__== "__main__" :
    main()