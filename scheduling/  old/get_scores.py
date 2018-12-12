import csv

def removeHeaders():
    rawScoreData.pop(0)
    for t in rawScoreData:
        t.pop(0)
    return
    
rawScoreData = []

with open("program files/scores.csv", newline='') as f:
    reader = csv.reader(f)
    for r in reader:
        rawScoreData.append(r)

removeHeaders()

# for rowid
