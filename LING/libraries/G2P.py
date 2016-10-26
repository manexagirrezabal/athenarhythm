import os
import sys
from subprocess import check_output

def splitAlpha(st):
  resultalpha=""
  resultnonalpha=""

  for ch in st:
    if ch.isalpha():
      resultalpha+=ch
    else:
      resultnonalpha+=ch
  return (resultalpha,resultnonalpha)


lines=["my name is manex","what did you say?"]
f=open(sys.argv[1])
lines=[line.decode("utf8").rstrip().lower() for line in f]
f.close()

for line in lines:
  tmpfile=open("tmp.txt",'w')
  linev=line.split(" ")
  nonalphas=[]
  for word in linev:
    alpha,nonalpha=splitAlpha(word)
#    print alpha, nonalpha
    tmpfile.write(alpha.encode("utf8")+"\n")
    nonalphas.append(nonalpha)
  tmpfile.close()
  result=check_output(["phonetisaurus-g2pfst","--model=/home/magirrezaba008/athenarhythm-working/athenarhythm/LING/newdicg2p.fst","--wordlist=tmp.txt"])
  words=[line.split("\t")[2].replace(' ','') for line in result.split("\n") if line!='']
#  print words
#  for indw,word in enumerate(words):
#    print word, nonalphas[indw]
  print ' '.join([word for word in words])
