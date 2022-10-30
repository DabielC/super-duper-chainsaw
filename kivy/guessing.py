import random

Name = ["0","s","e"]#text file 3 --> Begin Mid Advance

#user input()

def guesser(Name):
	quest = list(random.choice(Name))
	Name.remove(''.join(quest))
	times = random.randint(0,len(quest))


	for i in range(times):
		index_quest = random.randint(0, len(quest)-1)
		if quest[index_quest] != ' ':
			quest[index_quest] = '_'
		elif quest[index_quest] == ' ':
			times += 1

	return ''.join(quest)

sec = len(Name)
score = 0
name = Name.copy()

for i in range(sec):
	print(guesser(name))
	ans = input()
	if ans in Name:
		score += 1
	sec -= 1

print("%d / %d" %(score, len(Name)))
