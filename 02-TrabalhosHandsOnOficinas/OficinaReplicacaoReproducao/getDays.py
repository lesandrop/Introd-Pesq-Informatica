import json

def checkAuthorCommitsDays(dados_api, authorMap, fileLogRaw):
	for i in range(len(dados_api)):
		date = dados_api[i]['commit']['author']['date']
		author = dados_api[i]['commit']['author']['email']
		d = date + "," + str(author) +"\n"
		fileLogRaw.write(d)

		day = date.split("T")[0]

		if not author in authorMap:
			authorMap[author] = [day]
		else:
			if not day in authorMap[author]:
				authorMap[author].append(day)
	
def computeAuthorRanks(fileActivity, authorMap):
	
	numCommits = []
	for key, value in authorMap.items():
		print(key, len(value))
		numCommits.append(len(value))

	i = 1
	for value in sorted(numCommits,reverse=True):
		fileActivity.write(str(i)+","+str(value)+"\n")
		i += 1


fileJSON = open('data.json', 'r', encoding='utf-8') 
dados_api = json.load(fileJSON)
fileLogRaw = open("logBasicRawData.data", "w")
authorMap = {}
checkAuthorCommitsDays(dados_api, authorMap,fileLogRaw)
fileLogRaw.close()

fileActivity = open("activity.data", "w")
fileActivity.write("Rank,Frequency\n")
computeAuthorRanks(fileActivity, authorMap)
fileActivity.close