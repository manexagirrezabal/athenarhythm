import sys

dict={}
dict['#']=0 ##I changed this! Rememmber that some OLD models won't work! ;-) 28 -> 0
dict['a']=1
dict['b']=2
dict['c']=3
dict['d']=4
dict['e']=5
dict['f']=6
dict['g']=7
dict['h']=8
dict['i']=9
dict['j']=10
dict['k']=11
dict['l']=12
dict['m']=13
dict['n']=14
dict['eine']=15
dict['o']=16
dict['p']=17
dict['q']=18
dict['r']=19
dict['s']=20
dict['t']=21
dict['u']=22
dict['v']=23
dict['w']=24
dict['x']=25
dict['y']=26
dict['z']=27

maxel = 30

def str2num(str):
    if (len(str) == 3):
        num = (dict[str[0]]*maxel**0) + (dict[str[1]]*maxel**1) + (dict[str[2]]*maxel**2)
        #        return (float(num)/(maxel**3)).__str__()
        return (num)
    else:
        return '0'

def char2num(ch):
    #    return (float(dict[ch])/maxel**3).__str__()
    return (dict[ch]).__str__()
