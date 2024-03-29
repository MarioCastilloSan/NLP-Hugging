import argparse
#MAIN ARGUMENTS
parser= argparse.ArgumentParser()
parser.add_argument('-en', dest='evalue',action='store_true',required=False)
parser.add_argument('-sp', dest='spvalue',action='store_true',required=False)


#ENGLISH TRANSFORMER ARGUMENTS
parser.add_argument('-q',dest='qvalue', help="Question", type=str,required=False)
parser.add_argument('-c',dest='cvalue', help="Context", type=str,required=False)

#SPANISH ARGUMENTS
parser.add_argument('-qsp',dest='qspvalue', help="Question", type=str,required=False)
parser.add_argument('-csp',dest='cspvalue', help="Context", type=str,required=False)
args=parser.parse_args()
"""_summary_
        Brief documentation about the arguments parser
         Arguments : 
         -en select the English Transformer for use it.
         In case you use it it requiers the following values:
         -q is the question for the model
         -c is the context for the model
         -sp select the Spanish Transformer for use it.
            In case you use it it requiers the following values:
         -qsp is the question for the model
         -csp is the context for the model
"""
from roberta import*
from ixambert import*
def main():
    if(args.evalue):
        print(qa(args.qvalue,args.cvalue))
    if(args.spvalue):
       print(qaSP(args.qspvalue,args.cspvalue))

if __name__== "__main__" :
    main()