import datetime
import os

numberOfGames = 0
gamesPerDay = 0
startD1H = 0
startD1M = 0
gmWidth = 0
listComp = []
cumFieldsNum = []
listT = []
colH = []

with open("program files/initial_values.py") as f:
    code = compile(f.read(),f,'exec')
    exec(code, globals())
    
listTeamsDiv = []
listDivInfo = []
allOpp = []
tourn = []
listDivs = []
listPools = []
listPoolSize = []
listTeams = []
listList = []
listDivNumTeams = []
tourn = []
fGames = []

with open("program files/generate.py") as f:
    code = compile(f.read(),f,'exec')
    exec(code, globals())

with open("program files/opponents.py") as f:
    code = compile(f.read(),f,'exec')
    exec(code, globals())

with open("program files/check_teams.py") as f:
    code = compile(f.read(),f,'exec')
    exec(code, globals())
    
while 1:
    print("Valid operations:")
    print("1. Edit pools.")
    print("2. View specific team's opponent5s.")
    print("3. View all teams and opponents.")
    print("4. View schedule.")
    operation = "5"
    #input("")
    
    if operation == "1":
        with open("program files/manipulate.py") as f:
            code = compile(f.read(),f,'exec')
            exec(code,globals())
        with open("program files/opponents.py") as f:
            code = compile(f.read(),f,'exec')
            exec(code, globals())
        with open("program files/check_teams.py") as f:
            code = compile(f.read(),f,'exec')
            exec(code, globals())
        print("\n**All opponents determined.**\n")

    elif operation == "2":
        divID = int(input("Division index = "))
        poolID = int(input("Pool index = "))
        teamID = int(input("Team index = "))
        print("Chosen team:",listTeamsDiv[divID][poolID][teamID])
        print(allOpp[divID][poolID][teamID])

    elif operation == "3":
        with open('program files/output_opponents.py') as f:
            code = compile(f.read(),f,'exec')
            exec(code, globals())
        break

    elif operation == "4":
        with open("program files/schedule.py") as f:
            code = compile(f.read(),f,'exec')
            exec(code,globals())
        with open('program files/pull info.py') as f:
            code = compile(f.read(),f,'exec')
            exec(code,globals())
        #with open("program files/get_scores.py") as f:
#            code = compile(f.read(),f,'exec')
#            exec(code,globals())

    elif operation == '5':
        with open('program files/create playoff structure.py') as f:
            code = compile(f.read(),f,'exec')
            exec(code, globals())
        break
    
    else:
        break
