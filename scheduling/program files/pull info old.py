import csv
import datetime

file_path = schedule_name + ' | field grid.csv'
csvFile = []
extra_columns = [1,7,8,9]
team_columns = [2,3,4,5,6]
div_columns = [10,11,12,13,14]
change_fields = {"Girls U11A-RED" : ['','','',"3A","3B","4A"]}

if file_path == "sat.csv": date = '5/2/2015'
elif file_path == 'sun.csv': date = '5/3/2015'
elif file_path == 'Liberty 2015 _ field grid  DRAFT 06032015 5PM.csv': date = 'Jun 6 2015'
elif file_path == 'liberty 2015.csv': date = 'Jun 6 2015'
else: date = 'Jan 1 2000'

chrono = [[      'Game',
                 'Date',
                 'Time',
                 'Field',
                 'Bracket',
                 'Round',
                 'Team',
                 'Game Score',
                 'Sportsmanship Rating',
                 'Sportsmanship Notes',
                 'Ref Rating',
                 'Ref Rating Notes']]

with open(file_path, newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        csvFile.append(row)

old_rows = 0

for day in range([r[0] for r in csvFile[:-1]].count('Time')):
    start_at_row = [r[0] for r in csvFile[old_rows:]].index('Time') - 1 + old_rows
    try:
        end_at_row = [r[0] for r in csvFile[old_rows:]].index('') - 1
    except ValueError:
        end_at_row = len(csvFile[old_rows:]) + start_at_row

    pulled = csvFile[start_at_row:end_at_row]

    first_col = 1 + (len(pulled[2][1])==0)
    last_col = pulled[1].index('Pool Key')

    div_last_col = len(pulled[2]) - 1
    while pulled[2][div_last_col] == '': div_last_col -= 1
    div_first_col = div_last_col - (last_col - first_col)
    
    timelist = [r[0].split(' ')[0] for r in pulled[2:]]
    fields = [c.split('#')[1] for c in pulled[1][first_col:last_col]]
    divs = [r[div_first_col:div_last_col] for r in pulled[2:]]
    grid = [r[first_col:last_col] for r in pulled[2:]]

    for m in range(len(grid)):
        for n in range(len(grid[m])):
            newrow = ['' for i in chrono[0]]

            newrow[0] = day*len(grid)*len(grid[m]) + int(m/2)*len(grid[m]) + n + 1
            newrow[1] = str(datetime.datetime.strptime(date, '%b %d %Y') + datetime.timedelta(days=day)).split(' ')[0]
            newrow[2] = timelist[m]
            newrow[3] = fields[n]
            
            div = divs[m][n]
            team = grid[m][n]
            
            newrow[4] = div * (len(team.split(':')) < 2)
            newrow[5] = sum([sum([divs[i][j]==div and grid[i][j]==team for j in range(len(grid[i]))]) for i in range(len(grid[:m]))]) + 1
            newrow[6] = (team * (len(team.split(':')) < 2)).split(' <EX>')[0]
            
            if len(newrow[6]): chrono += [newrow]

    old_rows = end_at_row + 2

with open(file_path[:-4] + ' chrono.csv','w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(chrono)

with open('create pool standings.py') as f:
    code = compile(f.read(), f, 'exec')
    exec(code, globals())

with open('create score cards.py') as f:
    code = compile(f.read(), f, 'exec')
    exec(code, globals())
