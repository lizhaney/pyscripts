## WLratio
## WLratioconf
## conf
## topg
## rank
## mascot
## top25WL

teams = {
	"Duke":{
		"WLratio": ".5",
		"WLconf":".83",
		"rank":"2",
		"mascot": "Blue Devils",
	},

	"Villanova":{
		"WLratio": ".93",
		"WLconf":".88",
		"rank":"2",
		"mascot": "Wildcats",
	},

}

teams.keys()

for team in teams.keys():
	print team

teams.items()


##Trying to replicate but for different purposes. 
#I think I can create a function to load the CSV I built.
def load_teamz(Order, Team, Rank, WinP, Away, Jesuit, Mascot):
	##upload csv

##I then want python to score the teams.
#It could do this now or later.

load_teamz()

def choose winna():

#I want to evaluate the teams in pairs going down my list
#score= (WinP*2)+(Away) - (Rank*.1) + (If Jesuit=YES,.3, 0)
#if score{}>score{}
# if the team wins, I want add that line of the CSV to the next dictionary round
# keep doing this until gone through dicitonary

#Create a Dictionary for Each Round

second_round={}
third_round={}
elite_eight={}
final_four={}
championship={}
winner={}

print "Game: {0} vs {1}".format(march.get(rounds[index]), bracket.get(rounds[index+1])) #Prints Game

