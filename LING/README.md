#HOW TO TRAIN THE MODEL

Here you can see a step by step explanation of how to train the G2P model in phonetisaurus (Extended from a tutorial in FSMNLP 2012):

1.- Download the dataset (Sejnowski and Rosenberg, 1987).

`wget http://dingo.sbs.arizona.edu/~hammond/lsasummer11/newdic`

2.- Create a folder for temporary files.

`mkdir tmp`

3.- Convert the dataset to the format that the phonetisaurus aligner accepts. (NEW!!) Convert also the '|' character to e.g. '=', as there are conflicts with it.

`cat newdic | sed 's/|/=/g;' | perl newdic2phonetiaurus.pl > tmp/toy.train`

4.- Align graphemes and phonemes.

`phonetisaurus-align --input=tmp/toy.train --ofile=tmp/toy.corpus`

5.- Calculate a language model with these parameters (You can use SRILM, Google ngram, ...).

`ngram-count  -order 7 -kn-modify-counts-at-end -gt1min 0 -gt2min 0 -gt3min 0 -gt4min 0 -gt5min 0 -gt6min 0 -gt7min 0 -ukndiscount -ukndiscount1 -ukndiscount2 -ukndiscount3 -ukndiscount4 -ukndiscount5 -ukndiscount6 -ukndiscount7 -text tmp/toy.corpus -lm tmp/toy.arpa`

6.- Train the G2P system.

`phonetisaurus-arpa2wfst-omega --lm=tmp/toy.arpa -ofile=newdicg2p.fst`

7.- Remove temporary files.

`rm tmp/*; rmdir tmp; rm newdic`

#HOW TO USE THE TRAINED MODEL

`phonetisaurus-g2p --model=newdicg2p.fst --input="abjection" | sed 's/=/|/g;s/\ //g'`

#CLEAN OUTPUT

`phonetisaurus-g2p --model=newdicg2p.fst --input="abjection" | cut -f3 | sed 's/=/|/g;s/\ //g'`


##References

T. J. Sejnowski and C. R. Rosenberg, “Parallel networks that learn to pronounce English text,” Complex systems, vol. 1, no. 1, pp. 145–168, 1987.
