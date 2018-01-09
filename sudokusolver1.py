############################
### Name: Cameron English
### Univ. Num.:
############################

import time, copy
from tkinter import Tk, Canvas, Frame, Button, BOTH, TOP, RIGHT, BOTTOM

MARGIN = 20  # Pixels around the board
SIDE = 50  # Width of every board cell.
WIDTH = HEIGHT = MARGIN * 2 + SIDE * 9  # Width and height of the whole board
DELAY = 0.01  # the delay time makes the changing number visible


# Contains answer and checker function
class Problem():
    def __init__(self, canvas, num):
        self.canvas = canvas
        self.cnt = 0

        # Set of the Answer
        self.sol1 = [[4, 8, 3, 9, 2, 1, 6, 5, 7],
                     [9, 6, 7, 3, 4, 5, 8, 2, 1],
                     [2, 5, 1, 8, 7, 6, 4, 9, 3],
                     [5, 4, 8, 1, 3, 2, 9, 7, 6],
                     [7, 2, 9, 5, 6, 4, 1, 3, 8],
                     [1, 3, 6, 7, 9, 8, 2, 4, 5],
                     [3, 7, 2, 6, 8, 9, 5, 1, 4],
                     [8, 1, 4, 2, 5, 3, 7, 6, 9],
                     [6, 9, 5, 4, 1, 7, 3, 8, 2]]
        self.sol2 = [[1, 4, 5, 3, 2, 7, 6, 9, 8],
                     [8, 3, 9, 6, 5, 4, 1, 2, 7],
                     [6, 7, 2, 9, 1, 8, 5, 4, 3],
                     [4, 9, 6, 1, 8, 5, 3, 7, 2],
                     [2, 1, 8, 4, 7, 3, 9, 5, 6],
                     [7, 5, 3, 2, 9, 6, 4, 8, 1],
                     [3, 6, 7, 5, 4, 2, 8, 1, 9],
                     [9, 8, 4, 7, 6, 1, 2, 3, 5],
                     [5, 2, 1, 8, 3, 9, 7, 6, 4]]

        # Set of the problem
        self.prob_easy = [[4, 0, 3, 0, 2, 0, 6, 0, 0],
                          [9, 6, 0, 3, 0, 5, 0, 2, 1],
                          [2, 0, 1, 8, 0, 6, 0, 9, 0],
                          [0, 0, 8, 1, 0, 2, 9, 0, 0],
                          [7, 2, 0, 0, 6, 0, 0, 0, 8],
                          [0, 0, 6, 7, 0, 8, 2, 0, 0],
                          [0, 0, 2, 6, 0, 9, 5, 0, 0],
                          [8, 0, 0, 2, 0, 3, 0, 0, 9],
                          [0, 0, 5, 0, 1, 0, 3, 0, 0]]
        self.prob_normal = [[1, 0, 5, 3, 0, 0, 6, 0, 0],
                            [8, 0, 9, 6, 0, 0, 0, 2, 0],
                            [0, 7, 0, 0, 1, 0, 5, 0, 0],
                            [4, 0, 6, 0, 0, 5, 3, 0, 0],
                            [0, 1, 0, 0, 7, 0, 0, 0, 6],
                            [0, 0, 3, 2, 0, 0, 4, 8, 0],
                            [0, 6, 0, 5, 0, 0, 0, 0, 9],
                            [0, 0, 4, 0, 0, 0, 0, 3, 0],
                            [5, 2, 0, 0, 0, 9, 7, 0, 0]]

        if num is 1:
            self.puzzle = self.prob_easy
            self.solution = self.sol1
            self.puzzle_init = copy.deepcopy(self.prob_easy)
        elif num is 2:
            self.puzzle = self.prob_normal
            self.solution = self.sol2
            self.puzzle_init = copy.deepcopy(self.prob_normal)

    # display function inform you whether the input value is correct for position (x, y)
    def display(self, x, y, value):
        if self.puzzle_init[x - 1][y - 1] is 0:
            self.cnt += 1
            self.update_text(x, y, value)
        else:
            print("Error : Don't access a given number in the problem")
            print("The coordinates trying to be accessed are: ", x-1, y-1)

    # every time you use checker, this function update the value in canvas
    def update_text(self, i, j, k):
        time.sleep(DELAY)
        self.canvas.update()
        self.canvas.itemconfig(9 * (i - 1) + j, text=k, tags="numbers", fill="red")

    # is_done function show "Finished" at the end of solver
    def is_done(self, puzzle):
        # create a oval (which will be a circle)
        x0 = y0 = MARGIN + SIDE * 2.5
        x1 = y1 = MARGIN + SIDE * 6.5
        time.sleep(0.5)
        if puzzle == self.solution:
            self.canvas.create_oval(
                x0, y0, x1, y1,
                tags="done", fill="blue", outline="blue"
            )
            x = y = MARGIN + 4 * SIDE + SIDE / 2
            self.canvas.create_text(
                x, y,
                text="Correct!", tags="done",
                fill="white", font=("Arial", 32)
            )
        else:
            self.canvas.create_oval(
                x0, y0, x1, y1,
                tags="done", fill="red", outline="red"
            )
            x = y = MARGIN + 4 * SIDE + SIDE / 2
            self.canvas.create_text(
                x, y,
                text="Fail!", tags="done",
                fill="white", font=("Arial", 32)
            )
    def is_correct(self, puzzle):
        if puzzle == self.solution:
            return True
        else:
            return False


# this class initializes the canvas
class SudokuUI(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.__initUI()

    def __initUI(self):
        self.parent.title("AI: Sudoku Solver")
        self.pack(fill=BOTH)
        self.canvas = Canvas(self, width=WIDTH, height=HEIGHT)

        # Initialize each cell in the puzzle
        for i in range(1, 10):
            for j in range(1, 10):
                self.item = self.canvas.create_text(
                    MARGIN + (j - 1) * SIDE + SIDE / 2, MARGIN + (i - 1) * SIDE + SIDE / 2,
                    text='', tags="numbers",
                    fill="black", font=("Helvetica", 12)
                )
        self.canvas.pack(fill=BOTH, side=TOP)

        self.start_button1 = Button(self, text="___EASY___", command=self.__start_solver1)
        self.start_button2 = Button(self, text="__NORMAL__", command=self.__start_solver2)
        self.start_button2.pack(side=RIGHT)
        self.start_button1.pack(side=RIGHT)

        self.__draw_grid()

    # Draws 9x9 grid
    def __draw_grid(self):
        for i in range(10):
            width = 3 if i % 3 == 0 else 1
            x0 = MARGIN + i * SIDE
            y0 = MARGIN
            x1 = MARGIN + i * SIDE
            y1 = HEIGHT - MARGIN
            self.canvas.create_line(x0, y0, x1, y1, fill="black", width=width)
            x0 = MARGIN
            y0 = MARGIN + i * SIDE
            x1 = WIDTH - MARGIN
            y1 = MARGIN + i * SIDE
            self.canvas.create_line(x0, y0, x1, y1, fill="black", width=width)

    def __start_solver1(self):
        self.problem = Problem(self.canvas, 1)
        self.board_init()
        self.solver_class.solver()

    def __start_solver2(self):
        self.problem = Problem(self.canvas, 2)
        self.board_init()
        self.solver_class.solver()

    def board_init(self):
        self.start_button1.config(state="disabled")
        self.start_button2.config(state="disabled")
        self.puzzle = self.problem.puzzle
        self.solver_class = SudokuSolver(self.problem)
        for i in range(1, 10):
            for j in range(1, 10):
                if self.puzzle[i - 1][j - 1] is 0:
                    self.item = self.canvas.create_text(
                        MARGIN + (j - 1) * SIDE + SIDE / 2, MARGIN + (i - 1) * SIDE + SIDE / 2,
                        text='', tags="numbers",
                        fill="black", font=("Helvetica", 12)
                    )
                else:
                    self.item = self.canvas.create_text(
                        MARGIN + (j - 1) * SIDE + SIDE / 2, MARGIN + (i - 1) * SIDE + SIDE / 2,
                        text=self.puzzle[i - 1][j - 1], tags="numbers",
                        fill="black", font=("Helvetica", 12)
                    )



class SudokuSolver():
    def __init__(self, problem):
        self.problem = problem

        # We inserted the problem into puzzle array
        self.puzzle = self.problem.puzzle

    def solver(self):
        # TO DO: need to write solver
        # Your code goes here...
        
        # Starts search passing puzzle and first coordinate 
        self.search(self.puzzle, 0, 0)

        """This is just an example to call display function
        print self.problem.display(1, 2, 1)"""

        # Display "Correct" if successfully ended with all correct answers.
        # Display "Fail" if ended with wrong answer.
        self.problem.is_done(self.puzzle)


    def find_square(self, board, x, y):
        for a in range (0, 9):
            for b in range (0, 9):
                if self.puzzle[a][b] == 0:
                    return a, b
        return -1, -1

    def search(self, board, x, y):
        # DFS - Recursive depth-first search, retracts when a path does not lead to answer
        x,y = self.find_square(self.puzzle, x, y)
        if x == -1 and y == -1:
            return True
        for a in range(0, 10):
            # If the number at the position requested is valid
            if self.determine_choices(self.puzzle, x, y, a) == True:
                self.problem.display(x+1, y+1, a)
                self.puzzle[x][y] = a
                # Recurse
                if self.search(self.puzzle, x, y):
                    return True
            self.problem.display(x+1,y+1,"")	
            self.puzzle[x][y] = 0
        return False
   


    def determine_choices(self, board, a, b, c):
        # Displays the legal choices at a given square
        # Checks legality in the current row
        rowlist = self.puzzle[a]
        # Checks legality in the current column
        columnlist = [row[b] for row in self.puzzle]
	# Determines other numbers in 3x3 around current number
        # Checks lower bound of square by integer dividing coordinates, higher is three over
        squarelist = [self.puzzle[i][((b) // 3) * 3:(((b) // 3)+1) * 3] for i in range(((a) // 3) * 3, (((a) // 3)+1) * 3)]
        squarelist = sum(squarelist, [])

        # Ensures only legal moves are returned
        # Probably a better way to do this but I am new to Python
        alllist = [1,2,3,4,5,6,7,8,9]
        alllist = [x for x in alllist if x not in rowlist]
        alllist = [x for x in alllist if x not in columnlist]
        alllist = [x for x in alllist if x not in squarelist]
        if c in alllist:
            return True
        else:
            return False


if __name__ == "__main__":
    root = Tk()
    SudokuUI(root)
    root.geometry("%dx%d" % (WIDTH, HEIGHT + 40))
    root.mainloop()
