import svmattr
import sys
import re

#Feature Set 1

#The function's name must be getFeatures, whose input argument will be a word
#The output will be (1) a dict. Each element's index will be a number (1, 2, 3...)
#and the elements will be float numbers, features of the classifying element.
#And the number of vowels in the input word.

cl={}
cl["'"]=1
cl["'_"]=2
cl["'__"]=3
cl["'___"]=4
cl["'____"]=5
cl["'_____"]=6
cl["_"]=7
cl["_'"]=8
cl["_'_"]=9
cl["_'__"]=10
cl["_'___"]=11
cl["_'____"]=12
cl["__'"]=13
cl["__'_"]=14
cl["__'__"]=15
cl["__'___"]=16
cl["___'"]=17
cl["___'_"]=18
cl["___'__"]=19
cl["___'___"]=20
cl["____'"]=21
cl["____'_"]=22
cl["____'__"]=23
cl["_____'_"]=24
cl["_____'__"]=25
cl["__"]=26 #Manually added for the CMU0.6 dictionary
cl["___"]=27 #Manually added for the CMU0.6 dictionary
cl["____"]=28 #Manually added for the CMU0.6 dictionary
cl["_____"]=29 #Manually added for the CMU0.6 dictionary
cl["______"]=30 #Manually added for the CMU0.6 dictionary
cl["_______"]=31 #Manually added for the CMU0.6 dictionary

invcl = {v:k for k, v in cl.items()}
#print invcl[[25.0][0]]

def isVow (ch):
    return ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u' or ch=='y'

def getClass (stressPatt):
    return cl[stressPatt]

def str2num(str):
    return svmattr.dict[str[0]]+svmattr.dict[str[1]]*30

def getFeatures(word):
    lenw=len(word)
    features=[]
    vowelPoss=[]
    f={}
    #f['1']=float(len(word))
    f[1]=float(len(word))
    for i in range (2, svmattr.maxel**2):
        #f[i.__str__()]=0.0
        f[i]=0.0

    for ind, char in enumerate(word):
        if ind==0:
            gr1="#"
        else:
            gr1=word[ind-1]
        gr2=char
        index=str2num(gr1+gr2)
        f[index]=f[index]+0.03333333333333 ##I suppose that a 2-gram will not appear more than 30 times in a single word (It'd be weird)

    #This is to model the final part of the word, the right boundary
    index = str2num(gr2+"#")
    f[index]=f[index]+0.03333333333333
    features.append(f)
    vowelPoss.append(ind)
    return (features, len(vowelPoss))

def removeSecondary (stressPatt):
    return re.sub("`", "_", stressPatt)


# (fe, vn) = getFeatures("introduction")
# for i in fe[0]:
#     print i, fe[0][i]
#     if (fe[0][i] !=0):
#         sys.stdin.readline()
