

## Part 3
with open("states.csv", "r") as states_file:
	states = states_file.read().split("\n")

for index, state in enumerate(states):
	states[index] = states.split("\t")

print states

##part1

with open("states.txt", "r")as states_file:
	states = states_file.read()

print states

## Part 2

with open("states.txt", "r")as states_file:
	states = states_file.read().split("\n")

print states