import sys
import svmattr
from FS1 import *

#This program reads the corpus file (ARG1) and prints in the ARG2 file a SVM format file whose class will be the stress pattern that each word follows.
#The model has the following format, or feature set:
#c.f. the imported *feat* file


#It prints the "hash" dict in one single line
def inline(hash):
    str=""
    for keys,values in hash.items():
        str = str+keys.__str__()+":"+values.__str__()+" "
    return str


corpusFile = sys.argv[1]
outFile = sys.argv[2]
f=open(outFile, 'w')

#Read corpus. Must follow specific format:
#word+stressPat[-'`]+
words = [line.strip() for line in open(corpusFile)]

k=0
for word in words:
    lenw = word.find("+")
    nos = len(word) - lenw - 1 # Number of syllables

    trainingInstances,vowelPoss=getFeatures(word[:lenw]) #At this moment I don't use the vowelPoss feature for ML, but I think I'll have to use it soon    
    C=getClass(removeSecondary(word[lenw+1:])) ##This only works with feat2.py
    f.write(C.__str__()+" "+inline(trainingInstances[0])+"\n")
    print k
    k=k+1

f.close()
