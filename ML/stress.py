import sys
from svmutil import *
from liblinearutil import *
from FS1 import *
#This program gets two arguments. The first argument is the solver type, which can be linear (L) or non-linear (N).
#The second argument is the model file.
#import svmutil
param = svm_parameter('-q')

class stress(object):

    def __init__(self, solver, model):
        self.solverType = solver
        self.modelFile = model
        if (self.solverType != 'N') and (self.solverType != 'L'):
            #print "Error! You can only use Linear (L) or non-linear (N) solvers!"
            exit()

        if (self.solverType == 'N'):
            self.m=svm_load_model(self.modelFile)    
        else:
            self.m=load_model(self.modelFile)
        if (self.m == 0):
            #print "Something went bad... O couldn't load the model "+self.modelFile
            exit()

    def predict (self, word):
        #print "Get features from "+word
        if (len(word) > 0):
            (f, nv)=getFeatures(word)
        else:
            return ''
            nv=0
        if (nv>0):
            res=[cl["_"]]*1
            #print res
            if (self.solverType == 'N'):
                p_labels, p_acc, p_val = svm_predict(res, f, self.m, '')
            else:
                p_labels, p_acc, p_val = predict(res, f, self.m, '')
            predicted = invcl[p_labels[0]]
            #goldPos = predicted
            #print "Model predicted pattern: ."+ predicted+".", word, " Expected patt: ."+ stPatt+"."
            return predicted





    
def main():
    st=stress(sys.argv[1], sys.argv[2])
    wordComplete=sys.stdin.readline()
    wordComplete=wordComplete.rstrip()
    print ("The stress pattern is "+st.predict(wordComplete))
    print (param)

if __name__ == '__main__':main()
