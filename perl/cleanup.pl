#!/usr/bin/perl/
use strict;
use warnings;

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

# Set up for loops to loop through each year and each possible page.
# We can get up to 2000 results displayed 50 at a time, so there are at most 40 pages to loop through.
# Looping through excess pages will not interfere with the script, it will just slow it down.
my $file1;
my $file2=10000;
for($file1 = 1; $file1 <= 10000; $file1++){
	unless(-e "$topic/$file1.txt"){
		# if $file1 doesn't exist
		for($file2; $file2 > $file1; $file2--){
			# find the highest numbered existing file
			if(-e "$topic/$file2.txt"){
				# rename this file to replace the missing file1
				rename "$topic/$file2.txt", "$topic/$file1.txt";
				$file2--; # this file will not exist next time through, so go ahead and decrement now
				last; # exit this inner loop
			}
		}
	}
	if($file1 == $file2){
		last;
	}
}
print "Cleaned up filenames for $topic/\n";
