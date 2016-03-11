package G2P;
my $model = '/Users/manex/phonetisaurus/phonetisaurus-0.7.5/script/toy/new.fst'; #The model that we will use to do the G2P conversion
my $model = '/home/magirrezaba008/athenarhythm-working/athenarhythm/LING/newdicg2p.fst';
my $phonetisaurusDir='/home/magirrezaba008/Phonetisaurus/src/bin/'; #Phonetisaurus program location. Empty if it is in the $PATH variable



sub convert {

my @input = @{shift()};

open(TMPFILE, ">tmp.txt") or die "I couldn't open the temorary file";
foreach my $word (@input) {
  print TMPFILE $word."\n";
}
close(TMPFILE);

my $res = `${phonetisaurusDir}phonetisaurus-g2pfst --model=$model --wordlist=tmp.txt`;

chomp($res);
my @res = split(/\n/, $res);
#print "g2p: ".$res."\n";
foreach my $el (@res) {
  $el =~ s/[^\t]*\t[^\t]*\t//;
  $el =~ s/\ //g;
}
return @res;
}

1;
