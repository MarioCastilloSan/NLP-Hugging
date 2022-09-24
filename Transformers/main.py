import argparse
#MAIN ARGUMENTS
parser= argparse.ArgumentParser()
parser.add_argument('-en', dest='evalue',action='store_true')
parser.add_argument('--en', dest='evalue', action='store_false')
parser.add_argument('-sp', dest='spvalue',action='store_true')
parser.add_argument('--sp', dest='spvalue', action='store_false')

#ENGLISH TRANSFORMER ARGUMENTS
parser.add_argument('-q',dest='qvalue', help="Question", type=str)
parser.add_argument('-c',dest='cvalue', help="Context", type=str)

#SPANISH ARGUMENTS
parser.add_argument('-qsp',dest='qspvalue', help="Question", type=str)
parser.add_argument('-csp',dest='cspvalue', help="Context", type=str)
args=parser.parse_args()

from roberta import*
from ixambert import*
def main():
    if(args.evalue):
        print(qa(args.qvalue,args.cvalue))
    if(args.spvalue):
       print(qaSP(args.qspvalue,args.cspvalue))

if __name__== "__main__" :
    main()