from svmutil import *
from liblinearutil import *

solverType = sys.argv[1]
corpusFile = sys.argv[2]
numfeats = int(sys.argv[3])
modelFile = sys.argv[4]

if (solverType != 'N') and (solverType != 'L'):
    print "Error! You can only use Linear (L) or non-linear (N) solvers!"
    exit()

optionsN = '-s 0 -t 2 -c 1024 -g 0.0078125'
optionsL = '-s 1'

print corpusFile, numfeats, modelFile, optionsL, optionsN

print "Ok! I'm gonna start reading the problem!"
y, x = svm_read_problem(corpusFile)
print "Problem read!"
print len(y)
print len(x)

if (numfeats == 0):
    print "Training model with all training instances"
    if (solverType == 'L'):
        m = train(y, x, optionsL)
    else:
        m = svm_train(y, x, optionsN)
else:
    print "Training model with only",numfeats,"training instances"
    if (solverType == 'L'):
        m = train(y[:numfeats], x[:numfeats], optionsL)
    else:
        m = svm_train(y[:numfeats], x[:numfeats], optionsN)

if (solverType == 'L'):
    save_model(modelFile, m)
else:
    svm_save_model(modelFile, m)
