import csv
from os import listdir

tracking = "9505 5111 7986 5099 6399 67"

idealHeader = ['game','date','time','field','bracket','round','team','score']
listFiles = listdir('raw data')
altNames = {'game'      :   ['game','game #','game id','db id'],
            'date'      :   ['date','day'],
            'time'      :   ['time','start','start time'],
            'field'     :   ['field','location','place','facility'],
            'bracket'   :   ['bracket','division','group','pool','level'],
            'round'     :   ['round'],
            'team'      :   ['team'],
            'score'     :   ['score','final','final score'] }

def moveCol(matr,newCol,oldCol):
    for row in matr:
        row.insert(newCol,row.pop(oldCol))

    return matr

def delCol(col):
    for row in csvFile:
        row.pop(col)

def insCol(matr,header):
    for r in range(len(matr)):
        if r:
            matr[r].append("")
        else:
            matr[r].append(header)

    return matr

def clearCol(col):
    for row in csvFile:
        if row != csvHeader:
            row[col] = ""

def getHeader():
    headerRaw = csvFile[0]
    header = [i.lower() for i in headerRaw]
    
    return header

def fixHomeAway():
    csvHeader = getHeader()
    
    if csvHeader.count("home"):
        if csvHeader.count("team"):
            delCol(csvHeader.index("team"))
        h = csvHeader.index("home")
    else:
        h = csvHeader.index("team")
        
    if csvHeader.count("away"):
        a = csvHeader.index("away")
    elif csvHeader.count("opponent"):
        a = csvHeader.index("opponent")
    else:
        a = csvHeader.index("visitor")

    csvFileEdited = []

    for r in range(len(csvFile)):
        newRow = csvFile[r][:h] + [csvFile[r][a]] + csvFile[r][h+1:]
        
        del newRow[a]
        del csvFile[r][a]

        csvFileEdited.append(csvFile[r])
        csvFileEdited.append(newRow)

    del csvFileEdited[1]

    csvFileEdited[0][h - (h>a)] = "team"

    return csvFileEdited
            
def fixNoBracket(matr):
    csvHeader = getHeader()
    matr = insCol(matr,"bracket")
    
    tid = matr[0].index("team")
    bid = matr[0].index("bracket")

    if matr[1][tid].count(">"):
        for i in range(len(matr)):
            if i:
                team = matr[i][tid]
                if team[0] == ">": team = team[1:]
                splitTeam = team.split(">")
                if len(splitTeam)>2:
                    bracket = ""
                    for b in range(1,len(splitTeam)-1):
                        bracket += (splitTeam[b] + " ")
                else:
                    bracket = splitTeam[len(splitTeam)-2]
                matr[i][tid] = splitTeam[len(splitTeam)-1]
                matr[i][bid] = bracket
    else:
        for i in range(len(matr)):
            if i:
                team = matr[i][tid]
                splitTeam = team.split(" ")
                splitTeam.reverse()
                bracket = splitTeam[0]
                matr[i][tid] = team[:team.find(bracket)+1]
                matr[i][bid] = bracket

    return matr

def fixNoGameID(matr):
    matr = insCol(matr,"GAME")
    g = matr[0].index("GAME")

    for r in range(len(matr)):
        gameID = int((r+1)/2)
        if r:
            matr[r][g] = gameID

    return matr

def fixNoRound(matr):
    matr = insCol(matr,"ROUND")
    csvHeader = getHeader()
    rid = matr[0].index("ROUND")
    tid = csvHeader.index("team")
    bid = csvHeader.index("bracket")
    
    for i in range(1,len(matr)):
        listTeams = [row[tid] + row[bid] for row in matr[:i]]
        gRound = listTeams.count(matr[i][tid] + matr[i][bid])
        matr[i][rid] = gRound + 1
        
    return matr

def check(csvFile):
    csvHeader = getHeader()

    rowCount = 0

    while csvHeader.count('')/len(csvHeader)>.25:
        csvFile.pop(0)
        csvHeader = getHeader()
        rowCount += 1

    for item in csvHeader: item = item.lower()
    
    deleteableRows = []

    for r in range(len(csvFile)):
        if csvFile[r].count("")/len(csvFile[r]) > .5:
            deleteableRows.append(r)

    for r in reversed(deleteableRows):
        del csvFile [r]

    print("Deleted %i empty rows from sheet." % (rowCount + len(deleteableRows)))

    colCount = 0

    while csvHeader.count(''):
        delCol(csvHeader.index(''))
        colCount += 1
        csvHeader = getHeader()

    print("Deleted %i empty columns from sheet." % colCount)

    if csvHeader.count("home") + csvHeader.count("away") + csvHeader.count("opponent"):
        print("Different home/away columns")
        csvFile = fixHomeAway()

    csvHeader = getHeader()

    for header in idealHeader:
        hCount = 0
        for altHeader in altNames[header]:
            hCount += csvHeader.count(altHeader)
            if csvHeader.count(altHeader):
                csvFile[0][csvHeader.index(altHeader)] = header
                break

    csvHeader = getHeader()

    for header in idealHeader:
        if not(csvHeader.count(header)):
            print("No <%s> entered yet." % header.upper())
            if header == "bracket":
                csvFile = fixNoBracket(csvFile)
            elif header == "game":
                csvFile = fixNoGameID(csvFile)
            elif header == "round":
                csvFile = fixNoRound(csvFile)
            else:
                csvFile = insCol(csvFile,header.upper())

    csvHeader = getHeader()

    for header in reversed(csvHeader):
        if not(idealHeader.count(header)):
            for r in csvFile:
                del r[csvHeader.index(header)]

    csvHeader = getHeader()

    if csvHeader != idealHeader:
        b = 0
        while b < len(csvHeader):
            for colID in range(len(csvHeader)):
                if idealHeader.count(csvHeader[colID]) and idealHeader.index(csvHeader[colID]) != colID:
                    csvFile = moveCol(csvFile,idealHeader.index(csvHeader[colID]),colID)
                    print("Moved column",csvHeader[colID])
                    csvHeader = getHeader()
                    b = 0
                b += 1

    return csvFile

for file in listFiles:
    if file[-4:] != ".csv":
        print("Unable to process file:", file)
        listFiles.remove(file)
        
for file in listFiles:
    
    csvFile = []
    headerID = 0

    print("File:\t",file,"\n")
    
    with open("raw data/" + file, newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            csvFile.append(row)

    csvFile = check(csvFile)

    with open("edited data/" + file[:len(file)-4] + " edited.csv", 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(csvFile)

    print("\n\n")
