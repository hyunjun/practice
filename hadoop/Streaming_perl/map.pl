#!/usr/bin/perl

my $ngram = 3;
my $line = "";

while ($line = <>) {
	chomp($line);

	#tab 구분자로 필드 추출
	my ($coll, $docid, $title, $content, $url, $time) = split('\t', $line);

	#content 에서 trigram 추출
	my @tokens = split(' ', $content);
	for( my $i = $ngram-1; $i <= $#tokens; $i++ ) {
		#print ngram based on current index
		for( my $j = $i-($ngram-1); $j <= $i; $j++ ) {
			print $tokens[$j];
			if($j != $i){ print " "; }
		}
		print "\t1\n";
	}
}
