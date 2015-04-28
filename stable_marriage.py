import json
import sys
import copy
from pprint import pprint


input_filename = sys.argv[2]
m_or_w = sys.argv[1]




f = open(input_filename, 'r')
j = json.load(f)

f.close()


def StableMarriageMatch(pr,pd):
    Matched = {}
    
    Unmatched = list(pr.keys())
    UnmatchedCopy = Unmatched
    ListOfPreviousMatched = dict(zip(Unmatched,[0]*len(pr)))
    while (len(UnmatchedCopy) > 0):
        for U in UnmatchedCopy:
            Upartner = pr[U][ListOfPreviousMatched[U]]
        if(Upartner in Matched):
            
            if (pd[Upartner].index(U) < pd[Upartner].index(Matched[Upartner])):
                Unmatched.append(Matched[Upartner])
                Unmatched.remove(U)
                Matched[Upartner] = U
        else:
             Matched[Upartner] = U
             Unmatched.remove(U)
        ListOfPreviousMatched[U] =  ListOfPreviousMatched[U] + 1
        UnmatchedCopy = Unmatched
    iMatched = {v: k for k, v in Matched.items()}
    return iMatched
   
if m_or_w == "-m":
    a = j['men_rankings']
    b = j['women_rankings']
else:
    b = j['men_rankings']
    a = j['women_rankings']

final_j =  json.dumps(StableMarriageMatch(a, b))
print (final_j)
