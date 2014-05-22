import sys
from svmutil import *
from liblinearutil import *
from FS1 import *

#This program gets two arguments. The first argument is the solver type, which can be linear (L) or non-linear (N).
#The second argument is the model file.

solverType = sys.argv[1]
modelFile = sys.argv[2]

if (solverType != 'N') and (solverType != 'L'):
    print "Error! You can only use Linear (L) or non-linear (N) solvers!"
    exit()

if (solverType == 'N'):
    m=svm_load_model(modelFile)    
else:
    m=load_model(modelFile)

nelements=0
ok=0
totconfid=0.0
print m

if (m != 0):
    #print "Write the word yo want to analyze:"
    wordComplete=sys.stdin.readline()
    wordComplete=wordComplete.rstrip()
    #wordComplete="abacone+`-'-"

    while (wordComplete != ''):
        lenw = wordComplete.find("+")
        word=wordComplete[:lenw]
        stPatt = removeSecondary(wordComplete[lenw+1:])
        goldPos=stPatt.find("'")
        (f, nv)=getFeatures(word)
        if (nv>0):
            res=[cl[stPatt]]*1
            print res
            if (solverType == 'N'):
                p_labels, p_acc, p_val = svm_predict(res, f, m, '-q')
            else:
                p_labels, p_acc, p_val = predict(res, f, m, '')
            predicted = invcl[p_labels[0]]
            goldPos = predicted
            minpos = stPatt
            print "Model predicted pattern: ."+ predicted+".", word, " Expected patt: ."+ stPatt+"."

            if (minpos == goldPos):
                ok=ok+1
                nelements=nelements+1
            else:
                nelements=nelements+1

        wordComplete=sys.stdin.readline()
        wordComplete=wordComplete.rstrip()

    print "Ok, totconfid, nelements"
    print ok, totconfid, nelements
    print "Precision:", float(ok)/nelements
    



