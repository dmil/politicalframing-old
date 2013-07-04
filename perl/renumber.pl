#!/usr/bin/perl/
use strict;
use warnings;

# Set variables
my $usageMessage = ">> perl collectData.pl topicName \{party\}\n\nwhere:\n\ttopicName is a string, enclosed in quotes if contains a space\n\tparty is optional R for republican or D for democrat (case-sensitive)\n\n";

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

# Set up for loops to loop through each year and each possible page.
# We can get up to 2000 results displayed 50 at a time, so there are at most 40 pages to loop through.
# Looping through excess pages will not interfere with the script, it will just slow it down.
my $file1;
my $file2=5001;
for($file1 = 0; $file1 <= 5000; $file1++){
	if(-e "$topic/$party/$file1.txt"){
		# if $file1 exists
		rename "$topic/$party/$file1.txt", "$topic/$file2.txt";
		$file2++; 
	}
}
