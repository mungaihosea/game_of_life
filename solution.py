import os
import time
import random

#clears the terminal screen
def clear_screen():
    try:
        os.system('clear') #for Mac and linux
    except:
        os.system('cls') #for Windows

#the first menu
menu_1 = f'''
    Welcome to the Game of Life.
    select your prefered game mode.

    1) Automatic fast simulation
    2) Automatic slow simualation
    3) Manual simulation
    '''

#the second menu
menu_2 = f'''
    Select your prefered starting configuration.
    1) Read from file
    2) Random
    '''
#available options
game_mode_options = [1, 2, 3] 
grid_source_options = [1, 2]

#initialize the options
game_mode = 0
grid_source = 0


running = True #boolean variable used to terminate the program

while running:

    while True:
        #display the first menu and collect the input
        print(menu_1)
        game_mode = int(input())
        if game_mode_options.__contains__(game_mode):
            break
        else:
            clear_screen()

    clear_screen()

    #display the second menu and collect the input
    while True:
        print(menu_2)
        grid_source = int(input())
        if grid_source_options.__contains__(grid_source):
            break
        else:
            clear_screen()
    clear_screen()
    
    if grid_source == 2:
        #generate a grid containing random structure
        row_number = random.randint(5, 10)
        column_number = random.randint(5, 10)
        grid  = [[random.choice(['x','-']) for y in range(column_number)] for x in range(row_number)] #initialize empty grid


    elif grid_source == 1:
        #use a text file as the grid source    
        filename = input("Enter the file name containing your grid source: ")
        grid = []
        grid_file = open(filename, 'rb')
        grid_text = grid_file.read().decode().strip().split('\n') #split using '\n' as the delimiter
        for line in grid_text:
            if not line.__contains__('#'): #avoid comments
                if line.strip().__len__() != 0: #avoid white spaces
                    grid.append([x for x in line])
                    
        grid_file.close() #close the file

        #get the grid dimensions
        row_number = len(grid)
        column_number =len(grid[1])

    while True:        
        #initialize empty grid
        next_grid  = [['-' for y in range(column_number)] for x in range(row_number)]

        #loop through every available space
        for row_index in range(len(grid)):
            for column_index in range(len(grid[row_index])):
                neighbour_count = 0 #holds the number of neighbours a space or cell hass
                cell = grid[row_index][column_index]
                
                try:
                    row = row_index - 1
                    column = column_index
                    if row < 0 or column < 0: #avoid negative references
                        pass
                    else:
                        if grid[row_index - 1][column_index] == 'x':
                            neighbour_count += 1 #increment the neighbour count for the cell/space
                except:
                    pass

                try:
                    row = row_index + 1
                    column = column_index
                    if row < 0 or column < 0:
                        pass
                    else:
                        if grid[row_index + 1][column_index] == 'x':
                            neighbour_count += 1
                except:
                    pass
                
                try:
                    row = row_index
                    column = column_index - 1
                    if row < 0 or column < 0:
                        pass
                    else:
                        if grid[row_index][column_index - 1] == 'x':
                            neighbour_count += 1
                except:
                    pass

                try:
                    row = row_index
                    column = column_index + 1
                    if row < 0 or column < 0:
                        pass
                    else:
                        if grid[row_index][column_index + 1] == 'x':
                            neighbour_count += 1
                except:
                    pass
                
                try:
                    row = row_index + 1
                    column = column_index + 1
                    if row < 0 or column < 0:
                        pass
                    else:
                        if grid[row_index + 1][column_index + 1] == 'x':
                            neighbour_count += 1
                except:
                    pass

                try:
                    row = row_index - 1
                    column = column_index - 1
                    if row < 0 or column < 0:
                        pass
                    else:
                        if grid[row_index - 1][column_index - 1] == 'x':
                            neighbour_count += 1
                except:
                    pass

                try:
                    row = row_index + 1
                    column = column_index - 1
                    if row < 0 or column < 0:
                        pass
                    else:
                        if grid[row_index + 1][column_index - 1] == 'x':
                            neighbour_count += 1
                except:
                    pass

                try:
                    row = row_index - 1
                    column = column_index + 1
                    if row < 0 or column < 0:
                        pass
                    else:
                        if grid[row_index - 1][column_index + 1] == 'x':
                            neighbour_count += 1
                except:
                    pass
                #conditions if the space has not cell
                if cell == '-':
                    if neighbour_count <= 1: #has one neighbour
                        next_grid[row_index][column_index] = '-' 
                    elif neighbour_count == 2: #has two neighbours
                        next_grid[row_index][column_index] = '-'
                    elif neighbour_count == 3: #has three neighbours
                        next_grid[row_index][column_index] = 'x'
                    elif neighbour_count >= 4: #has more than 4 neighbours
                        next_grid[row_index][column_index] = '-'
                
                #conditions for an occupied cell
                if cell == 'x':
                    if neighbour_count <= 1:
                        next_grid[row_index][column_index] = '-'
                    elif neighbour_count == 2:
                        next_grid[row_index][column_index] = 'x'
                    elif neighbour_count == 3:
                        next_grid[row_index][column_index] = 'x'
                    elif neighbour_count >= 4:
                        next_grid[row_index][column_index] = '-'
        clear_screen()
        print("This is the new generation simulation output: \n")
        if game_mode == 1 or game_mode == 2:
            print("The Simulation is on automatic mode press (ctrl + c) to stop It ")
        for x in next_grid:
            print(x)
        if game_mode == 1: #sleep for 1 second if the simulation is on fast mode
            time.sleep(1)
        elif game_mode == 2:
            time.sleep(2) #slee for 2 seconds if the simulation is on slow mode
        elif game_mode == 3:
            response =  input(" \nPress Enter to generate the next simulation or x to close: ")
            if response == 'x':
                running = False
                break
        grid = [] #empty the grid

        for row in next_grid: #set the grid to the current generation
            grid.append(row)
        clear_screen()