from tkinter import *
from tkinter import filedialog as fdialog
import datetime
import csv

win = Tk()
win.title('Tournament Scheduler v1.1')
win.geometry('800x600')

def get_comp():
    global listComp
    listComp = []

    for c in comp_entry:
        if len(c[0].get()):
            listComp.append([c[0].get(), c[1].get()])
    
    if len(listComp):
        Button(win, text='Select teams', command=get_teams).grid()

def get_teams():
    global input_path
    input_path = fdialog.askopenfilename(filetypes=[('csv files', '.csv')])

    do('generate.py')
    do('opponents.py')
    do('check_teams.py')

    print('a')
    Label(win, text='')
    Button(win, text='Create schedule', command=get_sched).grid()

def get_sched():
    do('schedule.py')

def do(py):
    with open(py) as f:
        code = compile(f.read(), f, 'exec')
        exec(code, globals())
    
cn1 = Entry(win)
cs1 = Entry(win)
cn2 = Entry(win)
cs2 = Entry(win)
cn3 = Entry(win)
cs3 = Entry(win)
cn4 = Entry(win)
cs4 = Entry(win)
cn5 = Entry(win)
cs5 = Entry(win)
cn6 = Entry(win)
cs6 = Entry(win)

comp_entry = [[cn1,cs1],[cn2,cs2],[cn3,cs3],[cn4,cs4],[cn5,cs5],[cn6,cs6]]

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
listT = []
cumFieldsNum = []

do('initial_values.py')

quit_button = Button(win, text='Quit', command=quit)
quit_button.grid(column=3,sticky=NE)

L1 = Label(win, text='Complex name')
L1.grid(row=1, column=0)
L2 = Label(win, text='Number of fields')
L2.grid(row=1, column=1)

for c in range(len(comp_entry)):
    comp_entry[c][0].grid(row=2+c, column=0)
    comp_entry[c][1].grid(row=2+c, column=1)

Label(win, text='').grid()
Button(win, text='Save complexes', command=get_comp).grid()

win.mainloop()
