class Simulation:
    def __init__(self, mapMatrix, robotsCount, stationsCount, robotSpeed, robotBaterry, timestamp):
        
        self.mapMatrix = mapMatrix
        self.robotsCount = robotsCount
        self.stationsCount = stationsCount
        self.timestamp = timestamp

        self.simulationTime = 0
        self.robots = [] 
        self.robotStartPositions = pkt2robot(self.mapMatrix,self.robotsCount,self.stationsCount)
 
        for x, y in self.robotStartPositions:
            self.robots[i] = Robot(robotSpeed,robotBaterry,self.mapMatrix,[x,y])

    def show(self):
        #tutaj Grzesiu wyswietla

    def checkIfReady(self):
        for robot in self.robots:
            if robot.pos != robot.start_position and robot.current_path is None:
                return False
        return True
     
    #def report() - Domi napisała
    
    def step(self):
        result = checkIfReady()
        while(!ready):
            show()
            for robot in self.robots:
                robot.next_step()
                sleep(1)
                self.simulationTime += 1