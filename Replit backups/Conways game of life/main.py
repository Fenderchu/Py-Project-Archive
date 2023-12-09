import random, time
#constants
bordw, bordh = 25, 41
board = []
speed = 0.5
sim_rep = 0
no_print = False
live_range = ["n", "n", "n", 3, "n", "n", "n", "n", "n"]
kill_range =[0, 1, "n", "n", 4, 5, 6, 7, 8]
def build_board(fill = False):
    global board
    board = []
    for i in range (0, bordh+1):
        board.append([])
    for row in board:
        for i in range(0, bordw+1):
            if fill:
                row.append(random.randint(0, 1))
            else:
                row.append(0)
 
 
def board_print(prev = 0, tot = 0, rep = 0, tot2 = 0):
    printable = ""
    if not no_print:
        printable += (str(prev) +":" + str(tot) + ":" + str(rep) + "\n")
  
    printable += str(tot2) + ":" + str(sim_rep) + "\n"  
    
    if not no_print:
        for row in board:
            for col in row:
                if col == 1:
                    printable += "█"
                elif col == 0:
                    printable += "░"
                else:
                    printable += "#"
            printable += "\n"
    print(printable)

def edit_range(rng):
    loop = True 
    while loop:
        print(rng)
        in1 = input ("add: + \nremove: -\n>>>")
        in2 = input ("number: ")
        
        if in2.isnumeric():

            for i in range(0, 9):
                if i == int(in2):
                    if in1 == "+":
                        rng[i] = int(in2)
                        print(rng[i])
                    else:
                        rng[i] = "n"
        else:
            print("Nan")
        print(in1, in2)
        in3 = input ("continue?\ny/n\n>>>")
        if in3 == "n":
            loop = False
        
                    

def build_mode():
    cursorPos = [0,0]
    cursor = "#"
    current_cell = 0
    run = True
    global speed, sim_rep
    while run:
        curent_cell = board[cursorPos[0]][cursorPos[1]]
        board[cursorPos[0]][cursorPos[1]] = cursor
        no_choice = True
        board_print()
        board[cursorPos[0]][cursorPos[1]] = curent_cell
        while no_choice:
            choice = input (">>> ")
            if choice.lower() == "l":
                no_choice = False
                cursorPos[1] -= 1
            elif choice.lower() == "r":
                no_choice = False
                cursorPos[1]+= 1
            elif choice.lower() == "u":
                no_choice = False
                cursorPos[0] -= 1
            elif choice.lower() == "d":
                no_choice = False
                cursorPos[0] += 1
            elif choice.lower() == "set":
                no_choice = False
                curent_cell = 1
                board[cursorPos[0]][cursorPos[1]] = curent_cell
            elif choice.lower() == "reset":
                no_choice = False
                curent_cell = 0
                board[cursorPos[0]][cursorPos[1]] = curent_cell
            elif choice.lower() == "play":
                no_choice = False
                play_mode()
            elif choice.lower() == "speed":
                speed = float(input("Input speed 1-0.1:"))
                speed = 1.1 - speed
                if speed < 0:
                    speed = 0
            elif choice.lower() == "repeat":
                while True:
                    sim_rep += 1
                    play_mode()
            elif choice.lower() ==  "no print":
                global no_print
                no_print = True
            elif choice.lower() == "edit range":
                in1 = input( "1:kill range \n2:live range\n>>>")
                if in1 == "1":
                    edit_range(kill_range)
                elif in1 == "2":
                    edit_range(live_range)
            elif choice.lower() == "fill":
                build_board(True)
                board_print()

def play_mode():
    run = True
    repeat_count = 0
    prev_living = 0
    while run:
        empty = True
        tot_living = 0
        scaner = [0, 0]
        make_living = []
        kill = []
        for row in board:
            for col in row:
                living = 0
                surrounding = [[scaner[0]-1,scaner[1]-1],[scaner[0]-1,scaner[1]],
                [scaner[0]-1,scaner[1]+1],[scaner[0]+1,scaner[1]-1],
                [scaner[0]+1,scaner[1]+1],[scaner[0]+1,scaner[1]],
                [scaner[0],scaner[1]-1],[scaner[0],scaner[1]+1]]
                for cell in surrounding:
                    
                    if cell[0] > bordh:
                        cell[0] = 0
                    elif cell[0] < 0:
                        cell[0] = bordh
                    
                    if cell[1] > bordw:
                        cell[1] = 0
                    elif cell[1] < 0:
                        cell[1] = bordw

                    cell_value = board[cell[0]][cell[1]]
                    
                    if cell_value == 1:
                        living += 1
                        

                if living != 0 and empty:
                    empty = False
                if board[scaner[0]][scaner[1]] == 1:
                    tot_living += 1
                    if living in kill_range:
                        kill.append([scaner[0],scaner[1]])
                else:
                    if living in live_range:
                        make_living.append([scaner[0],scaner[1]])
        
                scaner[1] += 1
            scaner[1] = 0
            scaner[0] += 1

        for cell in make_living:
            if cell[0] > bordh:
                cell[0] = 0
            elif cell[0] < 0:
                cell[0] = bordh
                    
            if cell[1] > bordw:
                cell[1] = 0
            elif cell[1] < 0:
                cell[1] = bordw
            
            board[cell[0]][cell[1]] = 1
        for cell in kill:
            if cell[0] > bordh:
                cell[0] = 0
            elif cell[0] < 0:
                cell[0] = bordh
                    
            if cell[1] > bordw:
                cell[1] = 0
            elif cell[1] < 0:
                cell[1] = bordw

            board[cell[0]][cell[1]] = 0
            
        if tot_living in range(prev_living - 4, prev_living + 4):
            repeat_count += 1
        else:
            repeat_count = 0
        if repeat_count >= 100:
            run = False
        board_print(prev_living, tot_living, repeat_count,tot_living)
        prev_living = tot_living
        if empty:
            run = False
            
        
        time.sleep(speed)
        
        
    build_board(True)

build_board()
board_print()

build_mode()
