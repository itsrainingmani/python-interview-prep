import csv, time

# class Cell:

#     def __init__(self, posX, posY, val):
#         self.X = posX
#         self.Y = posY
#         self.value = val
#         self.alt_vals = []

#     def __str__(self):
#         return "Value: " + self.value + ", Pos: (" + self.X + ", " + self.Y + ")"

class Sudoku:

    def __init__(self, board_file_location):
        self.board = []
        self.sector_dict = {
            1: [(0,0), (2,2)],
            2: [(0,3), (2,5)],
            3: [(0,5), (2,8)],
            4: [(3,0), (5,2)],
            5: [(3,3), (5,5)],
            6: [(3,5), (5,8)],
            7: [(6,0), (8,2)],
            8: [(6,3), (8,5)],
            9: [(6,6), (8,8)]
        }
        self.num_set = set([1,2,3,4,5,6,7,8,9])
        self.alt_vals = [[[] for j in range(0, 9)] for i in range(0, 9)]

        with open(board_file_location, newline='') as csvfile:
            linereader = csv.reader(csvfile, delimiter=',')
            for row in linereader:
                self.board.append([int(i) for i in row])

    def __str__(self):
        s = ' '
        s += "_ "*3 + ' ' + "_ "*3 + ' ' + "_ "*3 + '\n'
        for i in range(0, len(self.board)):
            if i in [3,6]:
                s += ' '
                s += "_ "*3 + ' ' + "_ "*3 + ' ' + "_ "*3 + '\n'
            s += '|'
            for j in range(0, len(self.board)):
                if j in [2,5,8]:
                    s += str(self.board[i][j]) + '| '
                else:
                    s += str(self.board[i][j]) + ' '
            s += '\n'
            if i in [2,5,8]:
                s += ' '
                s += "‾ "*3 + ' ' + "‾ "*3 + ' ' + "‾ "*3 + '\n'
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
        for i in range(lower_bnd[0], upper_bnd[0]+1):
            for j in range(lower_bnd[1], upper_bnd[1]+1):
                sector_vals.append(self.board[i][j])
        
        return sector_vals

    def is_solved(self):
        for row in self.board:
            if 0 in row:
                return False

        for i in range(0, 9):
            col = self.get_column(i)
            if 0 in col:
                return False

        for k in self.sector_dict.keys():
            sector = self.get_sector_values(k)
            if 0 in sector:
                return False

        return True
        # return self.alt_vals == [[[] for j in range(0, 9)] for i in range(0, 9)]
    
    def update_board(self, x, y, val):
        self.board[x][y] = val

        # since the below functions are actually list comprehensions
        # we can't use them to modify the alt_vals state
        # So we have to manually traverse row, col and sector
        # row = self.get_row(x)
        # col = self.get_column(y)
        # sector = self.get_sector_values(self.which_sector(x, y))

        self.alt_vals[x][y] = []

        for j in range(0, 9):
            if val in self.alt_vals[x][j]:
                del self.alt_vals[x][j][self.alt_vals[x][j].index(val)]

        for i in range(0, 9):
            if val in self.alt_vals[i][y]:
                del self.alt_vals[i][y][self.alt_vals[i][y].index(val)]

        sec_num = self.which_sector(x, y)
        sec_bounds = self.sector_dict[sec_num]
        lower_bnd = sec_bounds[0]
        upper_bnd = sec_bounds[1]

        for i in range(lower_bnd[0], upper_bnd[0]+1):
            for j in range(lower_bnd[1], upper_bnd[1]+1):
                if val in self.alt_vals[i][j]:
                    del self.alt_vals[i][j][self.alt_vals[i][j].index(val)]

    def solve(self):
        start_time = time.time()
        total_num_passes = 0
        while not self.is_solved() and total_num_passes < 10000:
            for i in range(0, 9):
                for j in range(0, 9):
                    if self.board[i][j] == 0:
                        if len(self.alt_vals[i][j]) == 0:
                            row = self.get_row(i)
                            col = self.get_column(j)
                            sector = self.get_sector_values(self.which_sector(i, j))
                            tot_pos_vals = [self.num_set - (row & col & sector) - {0}]
                            if len(tot_pos_vals) == 1:
                                self.update_board(i, j, tot_pos_vals[0])
                            else:
                                self.alt_vals[i][j] = tot_pos_vals
                        elif len(self.alt_vals[i][j]) == 1:
                            self.update_board(i, j, self.alt_vals[i][j][0])
                        else:
                            pass
            total_num_passes += 1

        end_time = time.time()
        elapsed_time = end_time - start_time
        print("Sudoku Solved in %i seconds" % elapsed_time)

        

def main():
    s = Sudoku("./sudoku_easy.csv")
    # s1 = Sudoku("./sudoku_easy_4035_solved.csv")
    print("Beginning to Solve")
    print(s)
    s.solve()
    print(s.is_solved())
    # print(s.alt_vals)

if __name__ == "__main__":
    main()