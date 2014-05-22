import sys

class wickelFeat(object):

    def __init__(self, corpusFile):
        #corpusFile = sys.argv[1]

        words = [line.strip() for line in open(corpusFile)]
        frec={}
        for w in words:
            for i,ch in enumerate(w):
                if (i==0):
                    gr1="#"
                else:
                    gr1=w[i-1]
                if (i==len(w)-1):
                    gr3="#"
                else:
                    gr3=w[i+1]
                gr2=ch
                #print w, i,gr1+gr2+gr3
                try:
                    frec[gr1+gr2+gr3]=frec[gr1+gr2+gr3]+1
                except KeyError:
                    frec[gr1+gr2+gr3]=1

            
        self.feat={}
        thres=0
        k=0
        for i in frec.keys():
            #print i, frec[i], k
            if (frec[i]>thres):
                self.feat[i]=k
                k=k+1
            else:
                self.feat[i]=2

        #print len(self.feat), kont
        
    def str2num(self, str):
        try:
            return self.feat[str]
        except KeyError:
            return len(self.feat)

    def length(self):
        return len(self.feat)
    
#co=wickelFeat(sys.argv[1])
#print co.str2num("abc")

