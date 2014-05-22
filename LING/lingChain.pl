#!/usr/bin/perl

use lib 'libraries';
use IPC::Open2;
use strict;
use G2P;
use SYLL;

open2(*ReaderRules, *WriterRules, "flookup -i -b -x libraries/stressrules.fst");
SYLL::start();

my @input;
while (<STDIN>) {
  push @input, $_
}
# my $input = <STDIN>;
# my @input=split(/\n/, $input);
my @phonemes = G2P::convert(\@input);

my $k=0;
foreach my $phonemes (@phonemes) {
  my $syllphon = SYLL::syllabify($phonemes);
  my $output;
  print WriterRules $syllphon."\n";
  while ((my $returnword = <ReaderRules>) ne "\n") {
    chomp ($returnword);
    $output = $returnword;
    #print $returnword."\n";
  }
  $output =~ s/[^\'\.]//g;
  $output =~ s/\./_/g;
  print $output."\n";
  chomp($input[$k]);
  #print $input[$k]."\t".$phonemes."\t".$syllphon."\t".$output."\n";
    $k++;
}

