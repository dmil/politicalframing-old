#!/usr/bin/perl/

# Set variables
my $usageMessage = ">> perl collectData.pl topicName \{party\}\n\nwhere:\n\ttopicName is a string, enclosed in quotes if contains a space\n\tparty is optional R for republican or D for democrat (case-sensitive)\n\n";

# Check for command line inputs
if($#ARGV < 0){
	print "Error! Script was given $#ARGV arguments, but requires 2 argument.\n".
		"Proper usage of this script is as follows:\n" . $usageMessage;
	exit -1;
}

# Set Variables to Usable Names
my $topic = $ARGV[0];
$topic =~ s/\ /\+/g;
my $filea;
for($filea = 1000; $filea < 10000; $filea++){
	if(-e "$topic/$filea.txt"){
		unlink("$topic/$filea.txt");
	}
}
