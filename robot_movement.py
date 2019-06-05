import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


maze = pd.read_csv('mapka_s101.csv').values

road_matrix = maze.copy()
for x, row in enumerate(maze):
    for y, col in enumerate(row):
        if col == 0:
            road_matrix[x][y] = 1
        else:
            road_matrix[x][y] = 0

found_robot_positions_x = np.where(road_matrix == 1)[0][0]
found_robot_positions_y = np.where(road_matrix == 1)[1][0]


from operator import add

rob_pos = [23, 116]

def move_robot(rob_pos, road_matrix):
    robot_surrounding = []
    movement_values = []
    
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            robot_surrounding.append(road_matrix[rob_pos[0]+i][rob_pos[1]+j])
            movement_values.append([i, j])

best_field = 4
    
    for field, i in enumerate(robot_surrounding):
        if i == 1:
            best_field = field

return list( map(add, rob_pos, movement_values[best_field]) )





from IPython import display
import time

rob_pos = [23, 116]
rob_pos_2 = [252, 20]

plt.figure(figsize = (16,16))

for i in range(15):
    
    
    color_mem = maze[rob_pos[0], rob_pos[1]]
    color_mem_2 = maze[rob_pos_2[0], rob_pos_2[1]]
    
    
    maze[rob_pos[0], rob_pos[1]] = 8
    maze[rob_pos_2[0], rob_pos_2[1]] = 8
    
    #Update screen
    plt.imshow(maze)
    display.clear_output(wait=True)
    display.display(plt.gcf())
    time.sleep(1.0)
    
    maze[rob_pos[0], rob_pos[1]] = color_mem
    maze[rob_pos_2[0], rob_pos_2[1]] = color_mem_2
    
    #rob_pos = [rob_pos[0]+1, rob_pos[1]]
    #rob_pos = move_robot(rob_pos, road_matrix)
    robot_surrounding = []
    movement_values = []
    
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            robot_surrounding.append(road_matrix[rob_pos[0]+i][rob_pos[1]+j])
            movement_values.append([i, j])

best_field = 4
    
    for field, i in enumerate(robot_surrounding):
        if i == 1:
            best_field = field

rob_pos = list( map(add, rob_pos, movement_values[best_field]) )

    
    robot_surrounding = []
    movement_values = []
    
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            robot_surrounding.append(road_matrix[rob_pos_2[0]+i][rob_pos_2[1]+j])
            movement_values.append([i, j])

best_field = 4
    
    for field, i in enumerate(robot_surrounding):
        if i == 1:
            best_field = field

rob_pos_2 = list( map(add, rob_pos_2, movement_values[best_field]) )




