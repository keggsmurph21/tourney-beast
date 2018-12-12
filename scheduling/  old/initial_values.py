numberOfGames = 3
gamesPerDay = 12
startD1H = 7
startD1M = 0
gmWidth = 50
offsetH = 0
offsetM = 0
listComp = [["Place 1",9],['Place 2',8],['Place 3',7],['Place 4',3]]
input_path = 'program files/patriot-13-divisions.csv'
sched_name = "Saturday"

for t in range(gamesPerDay):
    if startD1M + t * gmWidth + offsetM >= 60:
        offsetH += 1
        offsetM -= 60
    listT.append(datetime.time(startD1H + offsetH,startD1M + t * gmWidth + offsetM))

for c in listComp:
    colH += [c[0] for i in range(c[1])]

for c in range(len(listComp)):
    if c:
        cumFieldsNum.append(cumFieldsNum[c-1] + listComp[c-1][1])
    else:
        cumFieldsNum.append(0)
