#!/usr/bin/perl/

# Set variables
my $usageMessage = ">> perl collectData.pl topicName \{party\}\n\nwhere:\n\ttopicName is a string, enclosed in quotes if contains a space\n\tparty is optional R for republican or D for democrat (case-sensitive)\n\n";
my $count = 0;

# Check for command line inputs
if($#ARGV < 1){
	print "Error! Script was given $#ARGV arguments, but requires 2 argument.\n".
		"Proper usage of this script is as follows:\n" . $usageMessage;
	exit -1;
}
if($ARGV[1] ne "R" && $ARGV[1] ne "D"){
	print "Error! Second argument must be an \"R\" or a \"D\".\n".
		"Proper usage of this script is as follows:\n" . $usageMessage;
	exit -1;
}

# Set Variables to Usable Names
my $topic = $ARGV[0];
$topic =~ s/\ /\+/g;
my $party = $ARGV[1];
my $page;

# Set up for loops to loop through each year and each possible page.
# We can get up to 2000 results displayed 50 at a time, so there are at most 40 pages to loop through.
# Looping through excess pages will not interfere with the script, it will just slow it down.
my $filea;
my $fileb;
my $text1;
my $text2;
for($filea = 0; $filea < 10000; $filea++){
	if(($filea % 1000) == 0){
		print "Removing duplicates for $filea.txt in $topic/$party/\n";
	}
	unless(-e "$topic/$party/$filea.txt"){
		next;
	}
	for($fileb = $filea+1; $fileb < 10000; $fileb++){
		open(FILE1, "$topic/$party/$filea.txt");
		$text1 = readline(FILE1);
		unless(-e "$topic/$party/$fileb.txt"){
			next;
		}
		open(FILE2, "$topic/$party/$fileb.txt");
		$text2 = readline(FILE2);
		if($text1 eq $text2){
			$text1 = readline(FILE1);
			$text2 = readline(FILE2);
			if($text1 eq $text2){
				$text1 = readline(FILE1);
				$text2 = readline(FILE2);
				if($text1 eq $text2){
					close(FILE2);
					unlink("$topic/$party/$fileb.txt");
					$count++;
					next;
				}
			}
		}
	}
}
print "Deleted $count files from $topic/$party/\n";
