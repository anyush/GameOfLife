import sys
import copy
import os


class Cell:
    def __init__(self, state):
        self.state = state
        self.neighbours = 0

    def change_state(self):
        if self.state == "*":
            self.state = "."
        else:
            self.state = "*"

    def count_neighbours(self, x, y, field):
        if self.state == "*":
            self.neighbours -= 1
        for i in range(x-1, x+2):
            for j in range(y-1, y+2):
                try:
                    if field[i][j].state == "*":
                        self.neighbours += 1
                except IndexError:
                    continue
        return self.neighbours


gen = 1
os.system('color 7')

while True:
    try:
        if gen == 1:
            file = "in.txt"
        else:
            file = "out.txt"
        with open(file, "r") as infile:
            line_in_file = 0
            n = 0
            field = []
            for line in infile:
                line = line.rstrip("\n")
                line_in_file += 1
                if line_in_file == 2:
                    size = line.split(" ")
                    try:
                        a = int(size[0])
                        b = int(size[1])
                        field = [[] for line in range(a)]
                    except ValueError:
                        sys.exit()
                if line_in_file > 2:
                    line = line.replace(".", ". ").replace("*", "* ")
                    line_splited = line.split(" ")
                    line_splited.pop()
                    for symbol in range(b):
                        try:
                            field[n].append(Cell(line_splited[symbol]))
                        except IndexError:
                            sys.exit()
                    n += 1
            if not field[a - 1]:
                print("Wrong data.4")
                sys.exit()
    except IOError:
        print("Can't open the in.txt.")

    with open("out.txt", "w") as outfile:
        print("\nGeneration {}:".format(gen))
        outfile.write("Generation {}:\n{} {}\n".format(gen, a, b))
        for i in range(a):
            for j in range(b):
                n = field[i][j].count_neighbours(i, j, field)
                cell = copy.copy(field[i][j])
                if ((field[i][j].state == "*") and ((n < 2) or (n > 3))) or \
                   ((field[i][j].state == ".") and (n == 3)):
                    cell.change_state()
                outfile.write(cell.state)
                print(cell.state, end='')
            print()
            outfile.write("\n")
        gen += 1
        input()
        os.system('cls')
