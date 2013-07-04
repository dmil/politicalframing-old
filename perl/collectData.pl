#!/usr/bin/perl/
use strict;
use warnings;
use LWP::Simple;

# Set variables
my $key = "574110e6685841eca77b2d72561355f2"; # your API key to Capitol Words API
my $individualFiles = 1;

my $usageMessage = ">> perl collectData.pl topicName \{party\}\n\nwhere:\n\ttopicName is a string, enclosed in quotes if contains a space\n\tparty is optional R for republican or D for democrat (case-sensitive)\n\n";
my $count = 0; # do not change this variable, it is used to name files as they are output

# Check for command line inputs
if($key eq ""){
	die("Error! Please modify the script to contain your Capitol Words API key on line 7.");
}
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
my $year;
my $page;

# Check on necessary directories
if($individualFiles){
	unless(-d "$topic"){
		mkdir "$topic"
	}
	unless(-d "$topic/$party"){
		mkdir "$topic/$party"
	}
}
else{
	unless(-d "D"){
		mkdir "D"
	}
	unless(-d "R"){
		mkdir "R"
	}
}


my $response;
my $fullText;

# If writing to all one file, open the file here
if(!$individualFiles){
	open(MYFILE, ">>$party/$topic.txt");
}

# Set up for loops to loop through each year and each possible page.
# We can get up to 2000 results displayed 50 at a time, so there are at most 40 pages to loop through.
# Looping through excess pages will not interfere with the script, it will just slow it down.
for($year = 2012; $year >= 1996; $year--){
	for($page = 1; $page <= 40; $page++){
		# Get search results
		my $url = "http://capitolwords.org/api/text.json?phrase=$topic&party=$party&apikey=$key&page=$page&start_date=$year-01-01&end_age=$year-12-31";
		$response = get($url);

		if($response eq ""){
			next;
		}

		my @lines = split('\n',$response); # splits response into an array by line
		my @parsed;
		my $flag = 0;

		for my $line (@lines){ # iterate through all of the lines returned by the API
			@parsed = split("\:\ ", $line); # parse each line into 2 tokens: the property and the value
			for my $foo (@parsed){
				# There's probably a better way to do this, but... I'm not very good with regex.
				$foo =~ s/^\s+//; #remove leading spaces
				$foo =~ s/\s+$//; #remove trailing spaces
				$foo =~ s/("|")//g; #remove quotation marks
				if($flag == 1){
					$foo = substr($foo, 0, length($foo)-1); # remove trailing comma

					# get full text of the speech
					$fullText = get($foo);
					$fullText =~ s/^(?:.*\n){1,13}//; # remove the first 13 lines of the full text of the speech, which is header

					if($fullText eq ""){
						next;
					}

					# write full text of the speech to file
					if($individualFiles){
						open(MYFILE, ">>$topic/$party/$count.txt");
					}
					print MYFILE $fullText;
					if($individualFiles){
						close(MYFILE);
					}

					$count++; # increment the count, so that the next speech gets its own file name
					$flag = 0; # clear the signal flag
				}
				if($foo eq "origin_url"){
					$flag = 1; # this is a line with the URL, the next token will be the URL we want
				}
				if($count > 10000){
					exit 0;
				}
			}
		}
	}
}
if(!$individualFiles){
	# if we've been writing to all one file, close the file
	close(MYFILE);
}
