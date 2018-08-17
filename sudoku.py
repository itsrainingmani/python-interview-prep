import csv, time

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
        self.num_set = {i for i in range(1,10)}
        self.temp_vals = [[[] for j in range(0, 9)] for i in range(0, 9)]

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
            if 0 in row or len(set(row)) < 9:
                return False

        for i in range(0, 9):
            col = self.get_column(i)
            if 0 in col or len(set(col)) < 9:
                return False

        for k in self.sector_dict.keys():
            sector = self.get_sector_values(k)
            if 0 in sector or len(set(sector)) < 9:
                return False

        return True
    
    def update_board(self, x, y, val):
        self.board[x][y] = val

        row = self.get_row(x)
        col = self.get_column(y)
        sector = self.get_sector_values(self.which_sector(x, y))

    def solve(self):
        start_time = time.time()
        total_num_passes = 0
        while not self.is_solved() and total_num_passes < 10000:
            for i in range(0, 9):
                for j in range(0, 9):
                    if self.board[i][j] == 0:
                        if len(self.temp_vals[i][j]) == 0:
                            row = self.get_row(i)
                            col = self.get_column(j)
                            sector = self.get_sector_values(self.which_sector(i, j))
                            possible_row_vals = self.num_set - {row} - {0}
                            possible_col_vals = self.num_set - {col} - {0}
                            possible_sec_vals = self.num_set - {sector} - {0}
                            tot_pos_vals = [possible_row_vals + possible_col_vals + possible_sec_vals]
                            if len(tot_pos_vals) == 1:
                                self.update_board(i, j, tot_pos_vals[0])
                            else:
                                self.temp_vals[i][j] = tot_pos_vals
                        elif len(self.temp_vals[i][j]) == 1:
                            self.update_board(i, j, self.temp_vals[i][j][0])
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
    # print(s.is_solved())

if __name__ == "__main__":
    main()