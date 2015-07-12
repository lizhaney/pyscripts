with open ("mascots.csv", "r") as mascots_import:
    Teams = mascots_import.read().split("\r")

##change back to mascots.csv
##started as split "\r"
Rounds=2
RoundThree=[]
SweetSixteen=[]
EliteEight=[]
FinalFour=[]
Championship=[]
Winner=[]
TeamCount=62
Index=0

Teams[Index]

while Index < 64:
     Winner = raw_input('Who would win (A) {0} or (B) {1}?'.format(Teams[Index],Teams[Index+1]))
     print TeamCount, 'more teams'
     print 'Round', Rounds
     if Winner is 'A':
          RoundThree.append(Teams[Index])
     if Winner is 'B':
          RoundThree.append(Teams[Index+1])
              # elif:
                   #print 'Thats not a value' 
     TeamCount -= 2
     Index +=2
     print 'index', Index

print 'Made it to Round 3:', RoundThree
Index=0
TeamCount=30

while Index < 32:
     Winner = raw_input('Who would win (A) {0} or (B) {1}?'.format(RoundThree[Index],RoundThree[Index+1]))
     print TeamCount, 'more teams'
     if Winner is 'A':
          SweetSixteen.append(RoundThree[Index])
     if Winner is 'B':
          SweetSixteen.append(RoundThree[Index+1])
              # elif:
                   #print 'Thats not a value' 
     TeamCount -= 2
     Index +=2
     print 'index', Index

print 'Made it to SweetSixteen:', SweetSixteen
Index=0
TeamCount=30

while Index <16:
     Winner = raw_input('Who would win (A) {0} or (B) {1}?'.format(SweetSixteen[Index],SweetSixteen[Index+1]))
     print TeamCount, 'more teams'
     print 'Round', Rounds
     if Winner is 'A':
          EliteEight.append(SweetSixteen[Index])
     if Winner is 'B':
          EliteEight.append(SweetSixteen[Index+1])
              # elif:
                   #print 'Thats not a value' 
     TeamCount -= 2
     Index +=2
     print 'index', Index
print 'Made it to EliteEight:', EliteEight

Index=0
TeamCount=14

while Index <8:
     Winner = raw_input('Who would win (A) {0} or (B) {1}?'.format(EliteEight[Index],EliteEight[Index+1]))
     print TeamCount, 'more teams'
     print 'Round', Rounds
     if Winner is 'A':
          FinalFour.append(EliteEight[Index])
     if Winner is 'B':
          FinalFour.append(EliteEight[Index+1])
              # elif:
                   #print 'Thats not a value' 
     TeamCount -= 2
     Index +=2
     print 'index', Index

print 'Made it to FinalFour:', FinalFour
Index=0
TeamCount=6

while Index <4:
     Winner = raw_input('Who would win (A) {0} or (B) {1}?'.format(FinalFour[Index],FinalFour[Index+1]))
     print TeamCount, 'more teams'
     print 'Round', Rounds
     if Winner is 'A':
          Championship.append(FinalFour[Index])
     if Winner is 'B':
          Championship.append(FinalFour[Index+1])
              # elif:
                   #print 'Thats not a value' 
     TeamCount -= 2
     Index +=2
     print 'index', Index

print 'Made it to Championship:', Championship
Index=0
TeamCount=2

Winner = raw_input('Who would win (A) {0} or (B) {1}?'.format(Championship[Index],Championship[Index+1]))

if Winner is 'A':
     print'The NCAA Champion is {0}'.format(Championship[Index])
if Winner is 'B':
     print'The NCAA Champion is {0}'.format(Championship[Index+1])

print 'RoundThree\n',RoundThree 
print 'SweetSixteen\n',SweetSixteen
print 'Elite Eight\n', EliteEight
print 'FinalFour\n', FinalFour
print 'Championship\n',Championship

#cc
