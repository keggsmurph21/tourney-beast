from tkinter import *
from tkinter import filedialog as fdialog
from datetime import *
import csv

win = Tk()
win.title('Tournament Scheduler')
win.geometry('800x600')

def get_time_inputs():
    global numberOfGames
    global gamesPerDay
    global start_h
    global start_m
    global gmWidth
    
    numberOfGames = int(ent_nog.get())
    gamesPerDay = int(ent_gpd.get())
    start_h = int(ent_s_h.get())
    start_m = int(ent_s_m.get())
    gmWidth = int(ent_len.get())

    global listT
    listT = gen_timelist(start_h, start_m, gmWidth)

def gen_timelist(sh,sm,w):
    offH = 0
    offM = 0
    listT = []

    for t in range(gamesPerDay):
        if sm + t*w + offM >= 60:
            offH += 1
            offM -= 60
        listT.append(time(sh + offH, sm + t*w + offM))

    return listT

def get_comps():
    global listComp
    global cumFieldsNum
    
    listComp = []

    get_time_inputs()
    
    for i in range(10):
        if len(listCompNames[i].get()):
            listComp.append([listCompNames[i].get(),int(listCompSizes[i].get())])

    if listComp == []:
        return
    
    cumFieldsNum = gen_cum_fields(listComp)
    disp_init_setup()

def gen_cum_fields(comp):
    cumFields = []
    
    for c in range(len(comp)):
        if c:
            cumFields.append(cumFields[c-1] + listComp[c-1][1])
        else:
            cumFields.append(0)

    return cumFields

def disp_init_setup():
    btn = Button(win, text='Input teams', command=init_setup)
    btn.grid(row=100, column=1)

def init_setup():
    global input_path
    input_path = fdialog.askopenfilename(filetypes=[('csv files','.csv')])

    lbl = Label(win, text=input_path)
    lbl.grid(row=100,column=2)
    
    do('generate.py')
    do('opponents.py')
    do('check_teams.py')

    disp_secnd_setup()

def disp_secnd_setup():
    btn = Button(win, text='Create schedules', command=secnd_setup)
    btn.grid(row=101, column=1)

def secnd_setup():
    global sched_name
    lbl = Label(win, text="Scheduled created")
    lbl.grid(row=101,column=2)
    sched_name = ent_sn.get()
    
    do('schedule.py')
    
def do(path):
    with open(path) as c:
        code = compile(c.read(),c,'exec')
        exec(code,globals())

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

L1 = Label(win, text="TEAM, TIME, AND GAME INFORMATION")
L1.grid(row=0)
lbl_sn = Label(win, text="SCHEDULE NAME (opt)")
lbl_sn.grid(row=14)
ent_sn = Entry(win)
ent_sn.grid(row=15)

quit_btn = Button(win, text='Quit', command=quit)
quit_btn.grid(row=0,column=4)

lbl_nog = Label(win, text = 'How many games will each team play per day?')
ent_nog = Entry(win)
lbl_nog.grid(row=1,sticky=W)
ent_nog.grid(row=1,column=1, padx = 15)

lbl_gpd = Label(win, text = 'How many total games will there be per day?')
ent_gpd = Entry(win)
lbl_gpd.grid(row=2,sticky=W)
ent_gpd.grid(row=2,column=1, padx = 15)

L2 = Label(win, text="")
L2.grid(row=3)

lbl_s_h = Label(win, text = 'Start time (hours):')
ent_s_h = Entry(win)
lbl_s_h.grid(row=4,sticky=W)
ent_s_h.grid(row=4,column=1, padx = 15)

lbl_s_m = Label(win, text = 'Start time (mins):')
ent_s_m = Entry(win)
lbl_s_m.grid(row=5,sticky=W)
ent_s_m.grid(row=5,column=1, padx = 15)

lbl_len = Label(win, text = 'Length of each game (mins):')
ent_len = Entry(win)
lbl_len.grid(row=6,sticky=W)
ent_len.grid(row=6,column=1, padx = 15)

B1 = Button(win, text='Enter', command=get_time_inputs)
B1.grid(row=7)

L2.grid(row=8)

lbl_comp1 = Label(win, text="COMPLEX INFORMATION")
lbl_comp2 = Label(win, text = "Complex Name")
lbl_comp3 = Label(win, text = "Number of Fields")
lbl_comp1.grid(row=9)
lbl_comp2.grid(row=9, column=1)
lbl_comp3.grid(row=9, column=2)

btn_comp = Button(win, text = 'Enter', command = get_comps)
btn_comp.grid(row=10)

lcn0 = Entry(win)
lcn1 = Entry(win)
lcn2 = Entry(win)
lcn3 = Entry(win)
lcn4 = Entry(win)
lcn5 = Entry(win)
lcn6 = Entry(win)
lcn7 = Entry(win)
lcn8 = Entry(win)
lcn9 = Entry(win)

lcs0 = Entry(win)
lcs1 = Entry(win)
lcs2 = Entry(win)
lcs3 = Entry(win)
lcs4 = Entry(win)
lcs5 = Entry(win)
lcs6 = Entry(win)
lcs7 = Entry(win)
lcs8 = Entry(win)
lcs9 = Entry(win)

listCompNames = [lcn0, lcn1, lcn2, lcn3, lcn4, lcn5, lcn6, lcn7, lcn8, lcn9]
listCompSizes = [lcs0, lcs1, lcs2, lcs3, lcs4, lcs5, lcs6, lcs7, lcs8, lcs9]

for i in range(10):
    listCompNames[i].grid(row=10+i, column=1)
    listCompSizes[i].grid(row=10+i, column=2)

win.mainloop()
