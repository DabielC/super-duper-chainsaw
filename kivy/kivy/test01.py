import random
import csv
from googletrans import Translator

translator = Translator()

translated_text = translator.translate('pan', dest='th')

temp = []
Name = []

with open('ez.csv', 'r', newline='', encoding="latin") as mycsv:
	reader = csv.reader(mycsv)
	for i in reader:
		temp.append(i)


user = int(input())
for i in range(user):
	a = random.choice(temp)
	Name.append(str(a[0]).lower().rstrip())
	temp.remove(a)

def guesser(Name):
	ran = random.choice(Name)
	trans = translator.translate('%s' %(ran), dest='th')
	print(trans.text)
	quest = list(ran)
	Name.remove(''.join(quest))
	times = random.randint(2,len(quest)-1)


	for i in range(times):
		index_quest = random.randint(0, len(quest)-1)
		if quest[index_quest] != ' ':
			quest[index_quest] = '_'
		elif quest[index_quest] == ' ':
			times += 1

	return ''.join(quest), ran

sec = len(Name)
score = 0
name = Name.copy()

for i in range(sec):
	a, b = guesser(name)
	print(a)
	ans = input().lower()
	if ans in Name:
		score += 1
		print(b)
	else:
		print(b)
	sec -= 1

print("%d / %d" %(score, len(Name)))
