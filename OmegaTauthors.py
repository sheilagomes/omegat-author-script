authors = []
author = ''
tm = open('OmegaT-L10N-omegat.tmx', 'r')
allLines = tm.read()
lines = allLines.split('\n')
for j in range(0, len(lines)):
	pos = lines[j].find('changeid=')
	if pos > -1:
		while lines[j][pos+10] != '"':
			author += lines[j][pos+10]
			pos += 1
		if author not in authors:
			authors.append(author.strip('"'))
		author = ''
tm.close()
finalList = open('finalList.txt', 'w')
finalList.write(f'Number of authors: {str(len(authors))}\n')
finalList.write(f'Names: {str(authors)}')
finalList.close()
print(authors)