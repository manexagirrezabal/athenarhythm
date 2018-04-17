## Introduction

In this page you will see how to use LIBSVM and LIBLINEAR in a very easy way to train a model, in our case, for stress location prediction.
Steps

It's important to make sure that we are not training the models with the whole corpus, as we need some parts of it to evaluate the models (Train/Test or Train/Develop/Test). There are some useful scripts in ... to split the corpora into train and test sets.

Now, we have to convert our training corpus to an SVM readable format. For that purpose, we can use the program called prepareSvmCorpus.py. That program takes to arguments, the corpus that we want to convert to SVM format and the name of the output file.

`python prepareSvmCorpus.py textCorpus svmCorpus-FS1.SVM`

After preparing our corpus, we can just start training our models using the corpus. The program called train.py does that. This program takes four arguments:

- Linear or non-linear SVM
- SVM format corpus file (output of previous step)
- Number of features to use for the training (if 0, all the features are used)
- Name of the file in which the model file (for prediction) will be saved

`python train.py [N|L] svmCorpus-FS1.SVM 0 svmCorpus-FS1.model`

Great! The model has been created. Now we can make predictions based on the models, using the predict.py program. This program takes two arguments:

- Linear or non-linear SVM
- Model file got from the training

...

## Making predictions

`python stress.py [N|L] svmCorpus-FS1.model`

## Evaluation

`cat testCorpus | python predict.py [N|L] svmCorpus-FS1.model`
