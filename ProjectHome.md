## Project description ##

In this project we address the task of automatically assigning primary stress to out-of-vocabulary words in English. This work forms a necessary component in a scansion system for English poetry (http://zeuscansion.googlecode.com). We have developed three different approaches based on (1) word similarity, (2) hand- written linguistic rules and (3) machine learning. The first and last approach require stress-annotated corpora to train a model for stress assignment, while the linguistic approach relies on grapheme to phoneme conversion, a syllabification procedure and hand-written stress assignment rules. The linguistic approach proves to be the most effective, but the machine learning approach is not far behind.

## Dependencies ##

### Closest Word Finding approach ###

  * Foma (http://foma.googlecode.com): Finite-state compiler and C library


### Linguistic approach ###

  * Foma (http://foma.googlecode.com)
  * Phonetisaurus (http://phonetisaurus.googlecode.com): A WFST implementation that performs grapheme-to-phoneme conversion


### Machine learning approach ###

  * Python 2.7.5

  * LIBSVM (http://www.csie.ntu.edu.tw/~cjlin/libsvm): A library for Support Vector Machines

  * LIBLINEAR (http://www.csie.ntu.edu.tw/~cjlin/liblinear): A library for Large Linear Classification


## Training corpus ##

We have used the NETtalk pronunciation dictionary to train and test our models. The dictionary has information concerning to words, pronunciations, number of syllables, possible part of speech and and primary and secondary stress location. It can be downloaded from http://dingo.sbs.arizona.edu/~hammond/lsasummer11/newdic

## References ##