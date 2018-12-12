checkTeams = []
checkOpps = []

for d in range(len(listTeamsDiv)):
    for p in range(len(listTeamsDiv[d])):
        for t in range(len(listTeamsDiv[d][p])):
            checkTeams.append(listDivInfo[d] + listTeamsDiv[d][p][t])
            for opp in allOpp[d][p][t]:
                checkOpps.append(listDivInfo[d] + opp)
for team in checkTeams:
    if checkOpps.count(team) != numberOfGames:
        print("ERROR:", team, checkOpps.count(team))
