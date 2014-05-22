package SYLL;

use IPC::Open2;

sub start {
  open2(*ReaderSyll, *WriterSyll, "flookup -i -b -x libraries/syllabify-shortest.fst");
}

sub syllabify {

my $input = shift();
my $res="";

print WriterSyll $input."\n";

while ((my $returnword = <ReaderSyll>) ne "\n") {
    chomp ($returnword);
    $res = $returnword;
}

return $res;
}

1;
