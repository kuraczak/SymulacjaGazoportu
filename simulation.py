import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from IPython import display
import time
import pkt2robotMatrix

class Simulation:
    def __init__(self, mapMatrix, robotsCount):
        self.mapMatrix = mapMatrix
        self.robotsCount = robotsCount
        self.simulationTime = 0
        self.robots = pkt2robotMatrix.pkt2robotMatrix(self.mapMatrix, robotsCount)

    def show(self):
        pass
        #tutaj Grzesiu wyswietla

    def checkIfReady(self):
        for robot in self.robots:
            if robot.pos != robot.start_position and robot.current_path is None:
                return False
        return True
     
    #def report() - Domi napisała
    
    def step(self):
        result = self.checkIfReady()
        print('result {}'.format(result))
        if result:
            self.show()
            for robot in self.robots:
                print('before {}'.format(robot.pos))
                robot.next_step()
                print('after {}'.format(robot.pos))
                time.sleep(1)
                self.simulationTime += 1

if __name__ == '__main__':
    maze = pd.read_csv('mapka_s101.csv').values
    sim = Simulation(maze, 1)
    sim.step()
    sim.step()
    sim.step()

    