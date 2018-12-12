numberOfGames = 0
gamesPerDay = 0
listTeamsDiv = []
listDivInfo = []
allOpp = []
listFields = {}

with open("schedule_h.py") as f:
    code = compile(f.read(),f,'exec')
    exec(code,globals())

listSz = []
listSp = []
poolLong = []

for div in listTeamsDiv:
    listSzDiv = []
    listSpDiv = []
    for poolIndex in range(len(div)):
        if poolIndex % 2:
            szEx = len(div[poolIndex]) + len(div[poolIndex - 1])
            listSzDiv.append(szEx)
            spEx = int(szEx/2 * numberOfGames)
            split = not((szEx/2) % 2)
            listSpDiv.append([spEx,split])
    listSz.append(listSzDiv)
    listSp.append(listSpDiv)

for d in range(len(listSz)):
    for p in range(len(listSz[d])):
        if listSp[d][p][1]:
            poolLong.append([listDivInfo[d],p,int(listSz[d][p]/2)])
            poolLong.append([listDivInfo[d],p,int(listSz[d][p]/2)])
        else:
            poolLong.append([listDivInfo[d],p,listSz[d][p]])

for unit in poolLong:
    pass
