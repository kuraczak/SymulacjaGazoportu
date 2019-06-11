import bfs

class Robot:
    def __init__(self, speed, battery, map, start_position, robotId=0, chargePoint=Chargepoint()):
        self.index = robotId
        self.speed = speed
        self.battery = battery
        self.start_position = start_position
        self.chargePoint = chargePoint
        self.pos = start_position
        self.checkpoints = []
        self.current_path = []
        self.steps = 0
        self.map = map
        self.visited_points = []

    def next_step(self):
        try:
            for i in range(self.speed):
                self.pos = self.current_path.pop(0)
                self.steps += 1
                self.battery -= 1
        except IndexError:
            self.calculate_path()
    
    def calculate_path(self):
        if len(self.visited_points) != len(self.checkpoints):
            next_point = self.checkpoints[len(self.visited_points)]
            path_to_point = bfs.BFS(self.pos, next_point, map)
            path_to_battery = bfs.BFS(next_point, self.start_position, map)

            if len(path_to_battery) + len(path_to_point) < self.battery:
                self.current_path = path_to_point
            else:
                self.current_path = bfs.BFS(self.pos, self.start_position,map)


class Chargepoint:
    def __init__(self, index=0, coord_x=0, coord_y=0):
        self.x = coord_x
        self.y = coord_y
        self.index = index

    def __eq__(self, other):
        if other.x == self.x & other.y == self.y:
            return True
        else:
            return False

class Point:
    def __init__(self, coord_x=0, coord_y=0):
        self.x = coord_x
        self.y = coord_y

class Checkpoint:
    def __init__(self, index=0, coord_x=0, coord_y=0, charge=Chargepoint()):
        self.index = index
        self.y = coord_y
        self.x = coord_x
        self.chargePoint = charge


def evaluatedistance(checkpoint, chargepoint):
    dist = np.sqrt((checkpoint.x - chargepoint.x) ** 2 + (checkpoint.y - chargepoint.y) ** 2)
    return [checkpoint, chargepoint, dist]