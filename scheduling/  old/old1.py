import os

class Complex(object):
    def __init__(self, name, address, number_of_fields, number_of_games):
        self.name = name
        self.address = address
        self.number_of_fields = number_of_fields
        self.number_of_games = number_of_games
    def build_field_matrix(self):
        self.field_matrix = []
        field_matrix_list = [0] * (self.number_of_games + 1)
        for i in range(self.number_of_fields):
            self.field_matrix.append(field_matrix_list)
            self.field_matrix[i][0] = self.name[0]
        return self.field_matrix
    def pull_complex_info(self, file_name):
        f = open(file_name,"r")
        self.name = f.readline()
        self.address = f.readline()
        self.number_of_fields = int(f.readline())
        self.number_of_games = int(f.readline())
        f.close()

class Division(object):
    def __init__(self, name, teams, age, level):
        self.name = name
        self.teams = teams
        self.age = age
        self.level = level
    def pull_division_info(self, file_name):
        f = open(file_name,"r")
        self.name = f.readline()
        self.teams = f.readline().split()
        self.age = int(f.readline())
        self.level = f.readline()
        f.close()

def write_schedule_file_field(matrix):
    f = open(" outputs/schedule_output.txt","w")
    for comp_id in range(len(matrix)):
        f.write("\t\t" + str(matrix[comp_id][0][0]) + "\n")
        for time in range(len(matrix[0][0])):
            if not(time):
                f.write("\t")
                for field in range(len(matrix[comp_id])):
                    f.write(str(field+1) + " ")
            else:
                f.write(str(time_list[time-1][0]) + ":" + str(time_list[time-1][1]) + "\t")
                for field in range(len(matrix[comp_id])):
                    f.write(str(matrix[comp_id][field][time]) + " ")
            f.write("\n")
        f.write("\n")
    f.close()

setup_f = open("setup.txt","r")
complex_list = setup_f.readline().split()
division_list = setup_f.readline().split()
setup_f.close()

time_list = [(8,50),(9,40),(10,30),(11,20),(12,10),(1,00),(1,50),(2,40),(3,30),(4,20),(5,10),(6,00)]
#get rid of this ^^ and use the "datetime" module

master_field_matrix = []
for item in complex_list:
    file_name = " complexes/" + item + ".txt"
    item = Complex("", "", 0, 0)
    item.pull_complex_info(file_name)
    master_field_matrix.append(item.build_field_matrix())

for item in division_list:
    file_name = " divisions/" + item + ".txt"
    item = Division("",[],0,"")
    item.pull_division_info(file_name)
    print (item.teams)

write_schedule_file_field(master_field_matrix)
