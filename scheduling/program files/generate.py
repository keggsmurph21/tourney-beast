import csv

def findPoolSize(N):
    # find out the best teams out of the division, separate them, totally different script that doesn't interact
    # make tournament day 2 sched capabilities
    """Takes the number of teams in the divisions and determines by brute
force how best to arrange those divisions into pools.  Acceptable number of
teams are even numbers between 8 and 40, inclusive."""
    if N == 4: L = [4]
    elif N == 6: L = [6]
    elif N == 8: L = [4,4]
    elif N == 10: L = [5,5] #
    elif N == 12: L = [6,6] ############  ***Changed***
    elif N == 14: L = [7,7]
    elif N == 16: L = [4,4,4,4]
    elif N == 18: L = [5,5,4,4]
    elif N == 20: L = [5,5,5,5]
    elif N == 22: L = [7,7,4,4] # Unconfirmed, could also be [7,7,4,4]
    elif N == 24: L = [6,6,6,6] # Confirmed, was [6,6,3,3,3,3]
    elif N == 26: L = [5,5,4,4,4,4] # Unconfirmed
    elif N == 28: L = [7,7,7,7] # [6,6,4,4,4,4] # Confirmed, but could also be [7,7,7,7]
    elif N == 30: L = [7,7,4,4,4,4]
    elif N == 32: L = [4,4,4,4,4,4,4,4] #
    elif N == 34: L = [5,5,4,4,4,4,4,4] #
    elif N == 36: L = [5,5,5,5,4,4,4,4] #
    elif N == 38: L = [5,5,5,5,5,5,4,4] #
    elif N == 40: L = [5,5,5,5,5,5,5,5] # 
    else:
        print("Invalid entry.")
        L = [0]
    return L

def splitUpIntoPools(numList,nameList):
    """Cuts the divisions into their correct size based on the pools assigned
by the method breakup_into_pools."""
    total = 0
    divideIntoPool = []
    for j in listPoolSize[divIndex]:
        tempList = nameList[total:total+j]
        total += j
        divideIntoPool.append(tempList)
    return divideIntoPool    

try:
    print(use_manual_pools)
except NameError:
    use_manual_pools = True

# Pull out the information in the divisions.csv file
rawData = []
listTeamsDiv = []
listDivInfo = []
listDivNumTeams = []
listPoolSize = []

with open(input_path,newline='') as f:
    reader = csv.reader(f)
    for r in reader:
        rawData.append(r)
        
if use_manual_pools:
    for r in rawData[1:]:
        if len(r[9]):
            r[8] += "-"
            r[8] += r[9]
        
for r in rawData[1:]:
    listDivInfo.append(r[8])

# Figure out how many divisions there are and make a list of each of their names
listDivInfo = sorted(list(set(listDivInfo)))

listDivs = [[] for d in listDivInfo]

# Put each team into its correct division
for r in rawData[1:]:
    d = listDivInfo.index(r[8])
    state = ''
    if len(r[6]):
        state = " (" + r[6] + ")"
    listDivs[d].append(r[5] + state)
    
# Count the number of teams in each division
for divInfoIndex in range(len(listDivInfo)):
    listDivNumTeams.append(len(listDivs[divInfoIndex]))

# Check the findPoolSize method to see the best arrangement for the pools
for divNumTeams in listDivNumTeams:
    listPoolSize.append(findPoolSize(divNumTeams))

# Take the best arrangement for the pools and then split the division up into
# those pools
for divIndex in range(len(listDivInfo)):
    listTeamsDiv.append(splitUpIntoPools(divNumTeams,listDivs[divIndex]))
