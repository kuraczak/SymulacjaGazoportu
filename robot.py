class Robot:
    def __init__(self, speed, battery, map, start_position):
        self.speed = speed
        self.battery = battery
        self.start_position = start_position
        self.pos = (0, 0)
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
            path_to_point = BFS(self.pos, next_point)
            path_to_battery = BFS(next_point, self.start_position)

            if len(path_to_battery) + len(path_to_point) < self.battery:
                self.current_path = path_to_point
            else:
                self.current_path = BFS(self.pos, self.start_position)


        

