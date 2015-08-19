#!/usr/bin/perl

my $sum = 0;
my $prev_key = "";

while (my $line=<>) {
	chomp($line);

	my ($key, $value) = split('\t', $line);

	#지금 읽은 키가 앞서 키와 같다면
	if ($key eq $prev_key) {
		# 값을 더함
		$sum += $value;
	} 
	else { # 키가 다르면
		if($prev_key ne "") {
			# key \t count 쌍을 출력 
			print $prev_key . "\t" . $sum . "\n";
		}
		# sum 과 prev_key 갱신
		$sum = $value;
		$prev_key = $key;
	}
}
print $prev_key . "\t" . $sum . "\n";
