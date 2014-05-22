package G2P;
my $model = '/Users/manex/phonetisaurus/phonetisaurus-0.7.5/script/toy/new.fst'; #The model that we will use to do the G2P conversion
my $phonetisaurusDir='~/phonetisaurus/phonetisaurus-0.7.5/'; #Phonetisaurus program location. Empty if it is in the $PATH variable



sub convert {

my @input = @{shift()};

open(TMPFILE, ">tmp.txt") or die "I couldn't open the temorary file";
foreach my $word (@input) {
  print TMPFILE $word."\n";
}
close(TMPFILE);

my $res = `$phonetisaurusDirphonetisaurus-g2p --model=$model --isfile --input=tmp.txt`;

chomp($res);
my @res = split(/\n/, $res);
#print "g2p: ".$res."\n";
foreach my $el (@res) {
  $el =~ s/[^\t]*\t//;
  $el =~ s/\ //g;
}
return @res;
}

1;
