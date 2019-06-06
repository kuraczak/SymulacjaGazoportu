import pandas as pd

def BFS(start, end, maze):

    queue = [start]
    visited = set()

    while len(queue) != 0:
        if queue[0] == start:
            path = [queue.pop(0)]
        else:
            path = queue.pop(0)
        front = path[-1]
        if front == end:
            return path
        elif front not in visited:
            for adjacentSpace in getAdjacentSpaces(maze, front, visited):
                newPath = list(path)
                newPath.append(adjacentSpace)
                queue.append(newPath)
            visited.add(front)
    return None


def getAdjacentSpaces(maze, space, visited):

    spaces = list()
    spaces.append((space[0]-1, space[1]))  # Up
    spaces.append((space[0]+1, space[1]))  # Down
    spaces.append((space[0], space[1]-1))  # Left
    spaces.append((space[0], space[1]+1))  # Right

    final = list()
    for i in spaces:
        if maze[i[0]][i[1]] != (2 or 3 or 4 or 5) and i not in visited:
            final.append(i)
    return final


def findStart(maze):
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == 7:
                return tuple([i, j])
    return None


def findEnd(maze):
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == 8:
                return tuple([i, j])
    return None


maze = pd.read_csv('mapka_s101.csv').values
# startPoint = (13, 118)
# endPoint = (23, 118)
startPoint = findStart(maze)
endPoint = findEnd(maze)
print(startPoint)
print(endPoint)
path = BFS(startPoint, endPoint, maze)
print(path)