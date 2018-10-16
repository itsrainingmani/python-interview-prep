import csv, time


class Cell:
    def __init__(self, posX, posY, val):
        self.X = posX
        self.Y = posY
        self.value = val
        self.possibilities = []
        self.default = False

    def __str__(self):
        return "Value: " + self.value + ", Pos: (" + self.X + ", " + self.Y + ")"


class Sudoku:
    def __init__(self, board_file_location):
        self.board = []
        self.sector_dict = {
            1: [(0, 0), (2, 2)],
            2: [(0, 3), (2, 5)],
            3: [(0, 5), (2, 8)],
            4: [(3, 0), (5, 2)],
            5: [(3, 3), (5, 5)],
            6: [(3, 5), (5, 8)],
            7: [(6, 0), (8, 2)],
            8: [(6, 3), (8, 5)],
            9: [(6, 6), (8, 8)],
        }
        self.num_set = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.move_queue = []

        temp = []

        with open(board_file_location, newline="") as csvfile:
            linereader = csv.reader(csvfile, delimiter=",")
            for row in linereader:
                temp.append([int(i) for i in row])

        for i in range(len(temp)):
            row = temp[i]
            temp_row = []
            for j in range(len(row)):
                new_cell = Cell(i, j, row[j])
                if row[j] == 0:
                    new_cell.possibilities = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                    temp_row.append(new_cell)
                else:
                    new_cell.default = True
                    temp_row.append(new_cell)
            self.board.append(temp_row)

    def __str__(self):
        s = " "
        s += "_ " * 3 + " " + "_ " * 3 + " " + "_ " * 3 + "\n"
        for i in range(0, len(self.board)):
            if i in [3, 6]:
                s += " "
                s += "_ " * 3 + " " + "_ " * 3 + " " + "_ " * 3 + "\n"
            s += "|"
            for j in range(0, len(self.board)):
                if j in [2, 5, 8]:
                    s += str(self.board[i][j].value) + "| "
                else:
                    s += str(self.board[i][j].value) + " "
            s += "\n"
            if i in [2, 5, 8]:
                s += " "
                s += "‾ " * 3 + " " + "‾ " * 3 + " " + "‾ " * 3 + "\n"
        return s

    def get_column(self, col_index):
        return [self.board[i][col_index] for i in range(0, len(self.board))]

    def get_row(self, row_index):
        return self.board[row_index]

    def check_column(self, col_index, num_to_check):
        return num_to_check in self.get_column(col_index)

    def check_row(self, row_index, num_to_check):
        return num_to_check in self.get_row(row_index)

    def which_sector(self, x, y):
        if x <= 2 and y <= 8:
            if x <= 2 and y <= 2:
                return 1
            elif x <= 2 and y <= 5:
                return 2
            else:
                return 3
        elif (x <= 5 and y <= 8) and (x > 2):
            if x <= 5 and y <= 2:
                return 4
            elif x <= 5 and y <= 5:
                return 5
            else:
                return 6
        elif (x <= 8 and y <= 8) and (x > 5):
            if x <= 8 and y <= 2:
                return 7
            elif x <= 8 and y <= 5:
                return 8
            else:
                return 9

    def get_sector_values(self, sec_num):
        sec_bounds = self.sector_dict[sec_num]
        lower_bnd = sec_bounds[0]
        upper_bnd = sec_bounds[1]

        sector_vals = []
        for i in range(lower_bnd[0], upper_bnd[0] + 1):
            for j in range(lower_bnd[1], upper_bnd[1] + 1):
                sector_vals.append(self.board[i][j])

        return sector_vals

    def check_sector(self, sec_num, num_to_check):
        return num_to_check in self.get_sector_values(sec_num)

    def backtrack(self):
        pass

    def move_forward(self):
        pass

    def solve(self):
        pass


def main():
    s = Sudoku("./sudoku_easy.csv")
    # s1 = Sudoku("./sudoku_easy_4035_solved.csv")
    print("Beginning to Solve")
    print(s)

    start_time = time.time()
    total_num_passes = 0
    # s.solve()

    end_time = time.time()
    elapsed_time = end_time - start_time
    print("Sudoku Solved in %i seconds" % elapsed_time)


if __name__ == "__main__":
    main()
