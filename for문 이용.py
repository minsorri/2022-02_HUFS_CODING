score = [70,60,55,75,95,90,80,80,85,100]

allscore = 0
people = 10

for i in range(0,10):
	allscore = allscore + score[i]

ave = allscore/people

print(ave)
