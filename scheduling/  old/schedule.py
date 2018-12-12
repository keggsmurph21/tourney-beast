from random import shuffle
import csv

def findPerfectFit(listAvFields, listAvPools, selectedPool):
    size = selectedPool[0]
    success = False
    for f in listAvFields:
        if f[0] == size:
            f[0] -= size
            f[1].append(selectedPool)
            success = True
            break
    return([listAvFields,success])

def findEfficientFit(listAvFields, listAvPools, selectedPool):
    size = selectedPool[0]
    success = False
    unremovedPools = [p[0] for p in listPieces]
    for r in rList:
        unremovedPools.remove(r[0])
    for i in range(0,max(unremovedPools)):
        for f in listAvFields:
            if sum(not((f[0]-size) % u) for u in unremovedPools) and f[0] - size >= 0:
                f[0] -= size
                f[1].append(selectedPool)
                success = True
                return([listAvFields,success])
    return([listAvFields,success])

def findInefficientFit(listAvFields, listAvPools, selectedPool):
    size = selectedPool[0]
    success = False
    for moreFieldsLeft in range(0,max([f[0] for f in listAvFields])):
        for f in listAvFields:
            if f[0] == (size + moreFieldsLeft):
                f[0] -= size
                f[1].append(selectedPool)
                success = True
                return([listAvFields,success])
    return([listAvFields,success])

def checkCorrectNumberGames(teams, opponents, info):
    allTeams = []
    allMatches = []

    for d in teams:
        for p in d:
            for t in p:
                allTeams.append(info[teams.index(d)] + ": " + t)

    for d in range(len(opponents)):
        for p in opponents[d]:
            for P in p:
                for t in P:
                    allMatches.append(info[d] + ": " + t)

    for t in allTeams:
        if allMatches.count(t) != numberOfGames:
            print(t,allMatches.count(t))

    return allTeams

def checkAllTeamsScheduled(teams, grid, info):
    allTeams = []
    allMatches = []
    doubleScheduled = []

    for d in teams:
        for p in d:
            for t in p:
                allTeams.append(info[teams.index(d)] + ": " + t)

    for row in grid:
        for item in row:
            allMatches.append(item)

    for t in allTeams:
        if allMatches.count(t) != numberOfGames:
            doubleScheduled.append(t)

    return [allTeams, doubleScheduled]


def shufflePools():
    for div in fGames:
        for pool in div:
            for timeslot in pool:
                for matchup in timeslot:
                    shuffle(matchup)
                shuffle(timeslot)
    return

def createRow(lookupKey, lookupData):
    origDiv = lookupKey.split(": ")[0]
    origTeam = lookupKey.split(": ")[1]

    newRow = [origDiv, origTeam]

    for row in lookupData[1:]:
        if row.count(lookupKey):
            r = lookupData.index(row)
            c = row.index(lookupKey)
            timeRaw = lookupData[r][0]
            time = timeRaw.split(" ")[0]
            homeOrAway = timeRaw.split(" ")[1]

            if homeOrAway == "H": homeOrAway = " (Home)"
            else: homeOrAway = " (Away)"
            
            if r % 2: r += 1
            else: r -= 1

            newRow.append("")
            newRow.append(lookupData[0][c])
            newRow.append(time)
            newRow.append(lookupData[r][c] + homeOrAway)

    return newRow

def fixDoubleSchedule(team, grid):
    listOppNames = []
    listOppIndex = []
    for row in grid:
        if row.count(team):
            teamRow = grid.index(row)
            oppRow = teamRow - 1 + 2 * (grid.index(row)%2)
            teamCol = row.index(team)
            opponent = grid[oppRow][teamCol]
            listOppNames.append(opponent)
            listOppIndex.append([teamRow,oppRow,teamCol])

    listOppNames = listOppNames[::-1]
    listOppIndex = listOppIndex[::-1]

    for o in range(len(listOppNames)):
        if listOppNames[o + 1:].count(listOppNames[o]):
            delTeam = listOppIndex[o][0]
            delOpp = listOppIndex[o][1]
            delCol = listOppIndex[o][2]

            grid[delTeam][delCol] = "No game -- Error fixed"
            grid[delOpp][delCol] = "No game -- Error fixed"
            
            #print(listOppIndex[o])

    #print(listOppNames)
    #print(listOppIndex)

    return grid

listPieces = []
matrix = []
blocks = int(gamesPerDay/numberOfGames)

# Generate the [listPieces] variable: [sizeOfPuzzlePieces, division, pool, oversizedPiece]

for divID in range(len(listTeamsDiv)):
    for poolID in range(len(listTeamsDiv[divID])):
        size = len(listTeamsDiv[divID][poolID])
        listPieces.append([int(size/(2-size%2)),divID,poolID,size%2])

rList = []

for p in range(len(listPieces)):
    if listPieces[p][3] and listPieces[p][2] % 2:
        rList.append(p)

rList.reverse()

for r in rList:
    del listPieces[r]

for c in range(len(listComp)):
    for b in range(blocks):
        matrix.append([listComp[c][1],[]])

listPieces.sort(reverse=True)
matrix.sort(reverse = True)

# Add the items from [listPieces] to the [matrix] variable

iterations = 0

while len(listPieces):
    rList = []    
    for pool in listPieces:
        result = findPerfectFit(matrix, listPieces, pool)
        matrix = result[0]
        if result[1]:
            rList.append(pool)
    for pool in rList:
        listPieces.remove(pool)
       
    rList = []
    for pool in listPieces:
        result = findEfficientFit(matrix, listPieces, pool)
        matrix = result[0]
        if result[1]:
            rList.append(pool)
    for pool in rList:
        listPieces.remove(pool)
        
    if iterations > 2:
        rList = []
        for pool in listPieces:
            result = findInefficientFit(matrix, listPieces, pool)
            matrix = result[0]
            if result[1]:
                rList.append(pool)
        for pool in rList:
            listPieces.remove(pool)
        
    iterations += 1

for m in matrix:
    if m[0]:
        m[1].append([])

# Use the [matrix] variable to generate the [fields] variable

fields = [[] for m in matrix]

for m in range(len(matrix)):
    for p in matrix[m][1:][0]:
        if len(p):
            for p_i in range(p[0]):
                fields[m].append(p[1:3])
        else:
            for emptyFields in range(matrix[m][0]):
                fields[m].append([])

# Make sure every team will be attempted to be placed onto the .csv file exactly [numberOfGames] times

listAllTeams = checkCorrectNumberGames(listTeamsDiv, allOpp, listDivInfo)

# Create the [fGames] variable

fGames = [[[[] for timeslot in range(numberOfGames)] for pool in div] for div in listTeamsDiv]

for div in range(len(listTeamsDiv)):
    for pool in range(len(listTeamsDiv[div])):
        for team in range(len(listTeamsDiv[div][pool])):
            for timeslot in range(numberOfGames):
                divInfo = listDivInfo[div] + ": "
                matchup = sorted([divInfo + listTeamsDiv[div][pool][team], divInfo + allOpp[div][pool][team][timeslot]])
                if not(fGames[div][pool][timeslot].count(matchup)):
                    fGames[div][pool][timeslot].append(matchup)
                if len(listTeamsDiv[div][pool]) % 2 and not(pool % 2):
                    matchup = sorted([divInfo + listTeamsDiv[div][pool+1][team], divInfo + allOpp[div][pool+1][team][timeslot]])
                    if not(fGames[div][pool][timeslot].count(matchup)):
                        fGames[div][pool][timeslot].append(matchup)
     
shufflePools()

# preTourn

preTourn = [[] for b in range(blocks)]

for b in range(blocks):
    for c in range(len(listComp)):
        for p in fields[blocks * c + b]:
            preTourn[b].append(p)

# tourn

tourn = [[[] for f in range(len(preTourn[0]))] for g in range(2 * gamesPerDay)]

for b in range(len(preTourn)):
    for ts in range(numberOfGames):
        row = 2 * (int(b/2) * numberOfGames * 2 + ts * 2 + (b%2))
        for p in range(len(preTourn[b])):
            if len(preTourn[b][p]):
                divid = preTourn[b][p][0]
                poolid = preTourn[b][p][1]
                matchid = preTourn[b][:p].count(preTourn[b][p])
                matchup = fGames[divid][poolid][ts][matchid]
            else:
                matchup = ['No game','No game']
            for teamid in range(len(matchup)):
                tourn[row + teamid][p] = matchup[teamid]

tournCSV = tourn

# Generate time list with H/A designation

timelist = [str(listT[int(t/2)]) for t in range(len(listT) * 2)]

for t in range(len(timelist)):
    if t % 2:
        timelist[t] += " A"
    else:
        timelist[t] += " H"

# Add spaces for scores and time list

for rowid in range(len(tournCSV)):
    for teamid in range(len(tournCSV[rowid])):
        tournCSV[rowid].insert(teamid * 2 + 1, "")
    tournCSV[rowid].insert(0,timelist[rowid])

# Generate header and add it to matrix

header = [str(f + 1) for f in range(len(preTourn[0]))]
counter = 0
c = 0

for f in range(len(preTourn[0])):
    if f - counter == listComp[c][1]:
        c += 1
        counter += listComp[c][1] + 1
    compName = listComp[c][0]
    header[f] = compName + " " + header[f]

for f in range(len(header)):
    header.insert(2 * f + 1, "Score")

header.insert(0, "")

tournCSV.insert(0, header)

# Check each team shows up exactly [numberOfGames] times

while len(checkAllTeamsScheduled(listTeamsDiv, tournCSV, listDivInfo)[1]):
    print("Errors occurred: Checking for solution\n")
    checkTwo = checkAllTeamsScheduled(listTeamsDiv, tournCSV, listDivInfo)
    listAllTeams = checkTwo[0]
    schedErrors = checkTwo[1]

    for errorTeam in schedErrors:
        tournCSV = fixDoubleSchedule(errorTeam, tournCSV)

print("No errors occurred")

# Create the grid showing which teams are playing which opponents at which times and fields

scheduleByTeam = [["Division","Team","","Field","Time","Game 1",'',"Field","Time","Game 2",'',"Field","Time","Game 3"]]

for team in listAllTeams:
    createdRow = createRow(team, tournCSV)
    scheduleByTeam.append(createdRow)

# Output all relevant files

with open(sched_name + ' | field grid.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(tournCSV)

with open(sched_name + ' | team schedules.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(scheduleByTeam)
