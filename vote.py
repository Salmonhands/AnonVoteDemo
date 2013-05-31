#!/usr/bin/python

# vote.py
# Demonstrate a technique for collecting votes
# Preserves the anonymity of the voter
# Voter is still able to verify that vote counted
# TODO:
#  upgrade to long / deal with overflow (currently enforce limit of 5 voters/candidates)
#   allow stepping through instead of printing all results
#   possible update text to better communicate what is going on / how anonymity is preserved

# Eric Lovelace - 2013
# Implementing idea presented by Dr. Xou at IUPUI 
# (though he is not associated with me programming this so my mistakes should not be taken as an indication of any flaw on his part)

import random
from random import shuffle

# Get the number of candidates (2-8)
candidates = raw_input("Enter the number of candidates [3]: ")
if (candidates == "") : candidates = "3"
candidates = int(candidates)
if (candidates < 2) : candidates = 2
if (candidates > 5) : candidates = 5

# Get the number of voters (2-8)
voters = raw_input("Enter the number of voters [3]: ")
if (voters == "") : voters = "3"
voters = int(voters)
if (voters < 2) : voters = 2
if (voters > 5) : voters = 5

# How will votes be decided?
#method = raw_input("How will votes be decided ([a]utomatic or [m]anual): ")
method = "a" #skipping this for now
if (method.lower == "a") : method = "automatic"
elif (method.lower == "m") : method = "automatic"
else :
	print "Invalid input: deciding votes automatically"
	method = "automatic"

# Decide votes automatically
votes = []
for i in range(voters):
	votes.append(random.randint(1,candidates))
	
# Randomize voters place in output
place = range(voters)
shuffle(place)

# Print summary
print
print "%-25s%d" % ("Number of Candidates:", candidates)
print "%-25s%d" % ("Number of Voters:", voters)
print "%-25s%s" % ("Voting method:", method)

# Print votes and voting vector
print
print "%-24s" % "Voter Number:",
print [x+1 for x in range(voters)]
print "%-24s" % "Place in final:",
print place
print "%-24s" % "Vote:",
print votes
print
print "Voting Vector:"
for i in range(voters) :
	votingVector = []
	for j in range(1,candidates+1) :
		if (j == votes[i]) : votingVector.append(1)
		else : votingVector.append(0)
	print votingVector
	
# Get everybody's special vote number
magicNumber = []
print "\nGetting everyone's \"magic\" number"
for i in range(voters) :
	print
	thisVoter = i + 1
	print "---- Voter #%d ----" % thisVoter
	thisPosition = place[i]
	print "     %-20s%d" % ("Position:", thisPosition)
	thisVote = votes[i]
	print "     %-20s%d" % ("Voted for:", thisVote)
	powerOfTwo = thisPosition * voters + thisVote - 1
	print "     %-20s%-5d%s" % ("Power of Two:", powerOfTwo, "(position * numberOfVoters + vote - 1)")
	magicNumber.append(2**powerOfTwo)
	print "     %-20s%d" % ("Magic number:", magicNumber[i])
	
# Print Magic Number Summary
print
print "Magic Number Summary:"
print "%-15s%-15s" % ("Voter Number", "Magic Number")
for i in range(voters) : print "%-15d%-15d" % (i+1, magicNumber[i])

# Sectioning off the magic numbers
print
print "Sectioning off"
sections = []
for i in range(voters) :
	thisMagic = magicNumber[i]
	thisSection = []
	for j in range(voters-1) :
		thisSection.append(random.randint(-1000,1000))
	thisSection.append(thisMagic - sum(thisSection))
	print "%-24s" % ("Voter #%d sections: " % (i + 1)),
	print thisSection
	sections.append(thisSection)
	
# Distributing the sections
print
print "Distributing the sections"
distributions = []
for i in range(voters) :
	thisDistribution = []
	for j in range(voters) :
		thisSection = sections[j]
		thisDistribution.append(thisSection[i])
	print "%-24s" % ("Voter #%d distribution: " % (i + 1)),
	print thisDistribution
	distributions.append(thisDistribution)
	
# Calculating the sums
print 
print "Calculating the sums"
sums = []
for i in range(voters) :
	print "%-24s" % ("Voter #%d sum: " % (i + 1)),
	print sum(distributions[i])
	sums.append(sum(distributions[i]))

# Final Results
print 
print "------- Final Results -----"
print "%-25s%d" % ("Total sum:", sum(sums))
binary = "{0:b}".format(sum(sums))
binary = binary.rjust(voters*candidates, "0")
reverseBinary = binary[::-1]
print "%-25s%s" % ("Binary:", binary)
for i in range(voters) :
	j = place[i]
	thisBinary = reverseBinary[(j*candidates):(j+1)*candidates]
	thisBinary = thisBinary[::-1]
	print "%-24s" % ("Voter #%d (position: %d) binary:" % (i+1, j)),
	print thisBinary,
	print "     Original Vote: %d" % votes[i]
	

