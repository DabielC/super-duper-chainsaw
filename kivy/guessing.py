import random
import csv
from googletrans import Translator

"""translator = Translator()

translated_text = translator.translate('Mhong', dest='th')
print(translated_text.text)"""

temp = []
Name = []

with open('ez.csv', 'r', newline='', encoding="latin") as mycsv:
	reader = csv.reader(mycsv)
	for i in reader:
		temp.append(i)


user = int(input())
for i in range(user):
	a = random.choice(temp)
	Name.append(a[0])
	temp.remove(a)


def guesser(Name):
	quest = list(random.choice(Name))
	Name.remove(''.join(quest))
	times = random.randint(2,len(quest)-2)


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
