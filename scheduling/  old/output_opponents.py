import csv

outCSV = [["Team","Game 1","Game 2","Game 3"]]

for d in range(len(listTeamsDiv)):
    for p in range(len(listTeamsDiv[d])):
        for t in range(len(listTeamsDiv[d][p])):
            row = [listDivInfo[d] + listTeamsDiv[d][p][t]]
            for opp in allOpp[d][p][t]:
                row.append(listDivInfo[d] + opp)
            outCSV.append(row)

with open('program files/opponents.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(outCSV)
