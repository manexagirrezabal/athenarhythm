#AthenaRhythm

In this project we address the task of automatically assigning primary stress to out-of-vocabulary words in English.
This work forms a necessary component in a scansion system for English poetry (https://github.com/manexagirrezabal/zeuscansion).
We have developed three different approaches based on (1) word similarity, (2) hand- written linguistic rules and (3) machine learning.
The first and last approach require stress-annotated corpora to train a model for stress assignment, while the linguistic approach relies on grapheme to phoneme conversion, a syllabification procedure and hand-written stress assignment rules. The linguistic approach proves to be the most effective, but the machine learning approach is not far behind.

##Dependencies

###Closest Word Finding approach

- Foma: Finite-state compiler and C library (http://foma.googlecode.com)

###Linguistic approach

- Foma
- Phonetisaurus: A WFST implementation that performs grapheme-to-phoneme conversion (http://phonetisaurus.googlecode.com, https://github.com/AdolfVonKleist/Phonetisaurus/)

###Machine learning approach

- Python 2.7.5
- LIBSVM: A library for Support Vector Machines (http://www.csie.ntu.edu.tw/~cjlin/libsvm)
- LIBLINEAR: A library for Large Linear Classification (http://www.csie.ntu.edu.tw/~cjlin/liblinear)

##Training corpus

We have used the NETtalk pronunciation dictionary to train and test our models. The dictionary has information concerning to words, pronunciations, number of syllables, possible part of speech and and primary and secondary stress location. It can be downloaded from http://dingo.sbs.arizona.edu/~hammond/lsasummer11/newdic

##References
Agirrezabal, M., Heinz, J., Hulden, M., & Arrieta, B. (2014, January). Assigning stress to out-of-vocabulary words: three approaches. In Proceedings on the International Conference on Artificial Intelligence (ICAI) (p. 1). The Steering Committee of The World Congress in Computer Science, Computer Engineering and Applied Computing (WorldComp).
