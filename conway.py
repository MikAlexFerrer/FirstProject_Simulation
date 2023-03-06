"""
conway.py 
A simple Python/matplotlib implementation of Conway's Game of Life.
"""

import sys, argparse
import numpy as np
from datetime import date
import matplotlib.pyplot as plt 
import matplotlib.animation as animation
from variations import *

ON = 255
OFF = 0
frame = 0
vals = [OFF, ON]
counter = open("output.txt", "a")

def addShip(AliveCells, grid):
    global var_sizes
    glider = 0

    for cells in AliveCells:
        glider = np.random.randint(15, 18)

        grid[cells[0]:cells[0]+var_sizes[glider][0], cells[1]:cells[1]+var_sizes[glider][1]] = var_sizes[glider][2]

def randomGrid(row, col):
    return np.random.choice(vals, row*col, p=[0.93, 0.07]).reshape(row, col)
 
def countLifes(grid, x, y, col, row):
    sum = 0

    for i in range(-1, 2):
        for j in range(-1, 2):
            ROW = (x + i + row) % row
            COL = (y + j + col) % col
            sum += grid[ROW][COL]

    sum -= grid[x][y]

    return sum/255

def update(frameNum, img, grid, row, col):
    global frame
    newGrid = grid.copy()

    for x in range (row):
        for y in range (col):
            total = countLifes(grid, x, y, col, row)
            
            if grid[x][y] == ON and (total < 2 or total > 3):  
                newGrid[x][y] = OFF
            elif grid[x][y] == OFF and total == 3:
                newGrid[x][y] = ON

    img.set_data(newGrid)
    grid[:] = newGrid[:]

    outputValues(row, col, grid, frameNum)

    return img,

def readInput():
    file = open("input.txt", "r")
    info = []
    parameters = file.read().splitlines()

    for parameter in parameters:
        values = parameter.split()
        for value in values:
            info.append(value.split())
    
    file.close()

    return info

def outputValues(row, col, grid, frame):
    global counter, var_sizes
    today = date.today()

    variations = [0] * len(var_sizes)

    print("Frame N: " + str(frame))

    for x in range (row):
        for y in range (col):
            for i in range (len(var_sizes)):
                for j in range(var_sizes[i][3]):
                    if(np.array_equal(grid[x:x+var_sizes[i][0], y:y+var_sizes[i][1]], np.rot90(var_sizes[i][2], j), equal_nan=True)):
                        variations[i] += 1
                        i = len(var_sizes)
                        break
                    
    total_variations = np.sum(variations)

    counter.write("Simulation at " + str(today))
    counter.write("\nUniverse size " + str(row) + " " + str(col))
    counter.write("\nIteration " + str(frame))
    counter.write("\n__________________________________")
    counter.write("\n|       \t|  Count  |  Percent  ")
    counter.write("\n|Block   \t|" + str(variations[0]) + "        |" + str(round((100*variations[0])/total_variations, 2)))
    counter.write("\n|Beehive \t|" + str(variations[1]) + "        |" + str(round((100*variations[1])/total_variations, 2)))
    counter.write("\n|Loaf     \t|" + str(variations[2]) + "        |" + str(round((100*variations[2])/total_variations, 2)))
    counter.write("\n|Boat     \t|" + str(variations[3]) + "        |" + str(round((100*variations[3])/total_variations, 2)))
    counter.write("\n|Tub      \t|" + str(variations[4]) + "        |" + str(round((100*variations[4])/total_variations, 2)))
    blinker = variations[5] + variations[6]
    counter.write("\n|Blinker  \t|" + str(blinker) + "        |" + str(round((100*blinker)/total_variations, 2)))
    toad = variations[7] + variations[8]
    counter.write("\n|Toad     \t|" + str(toad) + "        |" + str(round((100*toad)/total_variations, 2)))
    beacon = variations[9] + variations[10]
    counter.write("\n|Beacon   \t|" + str(beacon) + "        |" + str(round((100*beacon)/total_variations, 2)))
    glider = variations[11] + variations[12] + variations[13] + variations[14]
    counter.write("\n|Glider    \t|" + str(glider) + "        |" + str(round((100*glider)/total_variations, 2)))
    lightweightship = variations[15] + variations[16] + variations[17] + variations[18]
    counter.write("\n|LG sp ship\t|" + str(lightweightship) + "        |" + str(round((100*lightweightship)/total_variations, 2)))
    counter.write("\n__________________________________")
    counter.write("\n|Total     \t|" + str(total_variations) + "        |          ")
    counter.write("\n__________________________________\n")
    
def main():
    info = readInput()

    updateInterval = 50

    grid = np.array([])

    row = int(info[0][0])
    col = int(info[1][0])

    AliveCells = []

    for i in range(6, len(info), 3):
        if i > len(info): 
            break
        AliveCells.append([int(info[i][0]), int(info[i+1][0])])  

    grid = randomGrid(row, col)
    addShip(AliveCells, grid)

    fig, ax = plt.subplots(figsize=(9, 9))
    ax.set_xticks([])
    ax.set_yticks([])
    img = ax.imshow(grid, interpolation='nearest')

    gens = int(info[4][0])+1

    ani = animation.FuncAnimation(fig, frames = gens, func=update, fargs=(img, grid, row, col), interval = updateInterval, save_count=50, repeat = False)

    plt.show()

if __name__ == '__main__':
    main()