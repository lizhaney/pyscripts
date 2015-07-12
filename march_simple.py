# Create a dictionary for each round

# A simple way to pick the winners of march madness

# Create a dictionary for each region
north_bracket = {}
south_bracket = {}
east_bracket = {}
west_bracket = {}

#creates teams with their ranking
def create_teams(bracket, region): 

	for index, items in enumerate(range(1,17),1):
	
		#prints University name with region and ranking = index which is the key of the dict
		bracket[index] = '{0}_University{1}'.format(region, index) 
	return bracket

# Turned the bracket into a linear formation
# For example since the winner fo 1 vs. 16 will face off 8 vs. 9  you get this pattern:
# 1 v 16 | 8 v 9  vs.  4 v 13 |  5 v 12
# 2 v 13 | 7 v 10 vs.  3 v 14 |  6 v 11

 
# Function that chooses the higher ranking team and pops the loser from the rounds team
def choose_winner(bracket):
	rounds = [1,16,8,9,4,13,5,12,2,13,7,10,3,14,6,11]
	
	# I will have the higher winner when length of list == 1
	while len(rounds)>1: 
		
		#Enumerate helps me pick the the following team in the list
		for index, rank  in enumerate(rounds): 
		
			print "Game: {0} vs {1}".format(bracket.get(rounds[index]), bracket.get(rounds[index+1])) #Prints Game
			if rounds[index] > rounds[index +1]: # Whoever has the higher ranking loses
				print "\t{0} wins\n".format(bracket.get(rounds[index+1]))
				rounds.pop(index)
		
			else:
				print "\t{0} wins\n".format(bracket.get(rounds[index]))
				rounds.pop(index+1)
		

	print "Yay! {0} Wins!".format(bracket.get(rounds[0]))
	return bracket.get(rounds[0]) #returns winner

# Use functions to get the winner of each round
print "North Region"
north_winner = choose_winner(create_teams(north_bracket, "North"))

print "\n\n\n", "South Region"
south_winner = choose_winner(create_teams(south_bracket, "South"))

print "\n\n\n", "East Region"
east_winner = choose_winner(create_teams(east_bracket, "East"))

print "\n\n\n", "West Region"
west_winner = choose_winner(create_teams(west_bracket, "West"))

print "\n\n\n", "Final Four"

# Since all the #1s from each region won, you can choose which one will win
winner_one = raw_input("Who will win? {0} or {1} ".format(north_winner, south_winner))
winner_two = raw_input("Who will win? {0} or {1} ".format(east_winner, west_winner))

print "\n\n\n", "Championships"

#Final round you also get to choose
final_winner = raw_input("Who will win? {0} or {1} ".format(winner_one, winner_two))

#The winner of the braket
print "The final winner is .... {0}!!!".format(final_winner)
