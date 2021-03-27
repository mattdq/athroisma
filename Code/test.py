# import csv
# with open(r'gcode\circle.csv', newline='\n') as file:
#     gcode = list(csv.reader(file))
import numpy as np


class Printer:
    def __init__(self, x=0, y=0, z=0):
        self.zero = np.array([0,0,0])
        self.current_pos = np.array([x, y, z])

    def move(self, size, step, angle, percentage = 0.001):
        initial = self.current_pos
        final = self.zero
        director = np.array([np.cos(angle), np.sin(angle), 0])
        while not (np.add(initial, director*size)[0]*(1-percentage)<=final[0]<=np.add(initial, director*size)[0]*(1+percentage) and np.add(initial, director*size)[1]*(1-percentage)<=final[1]<=np.add(initial, director*size)[1]*(1+percentage) and np.add(initial, director*size)[2]*(1-percentage)<=final[2]<=np.add(initial, director*size)[2]*(1+percentage)):
            final = np.add(self.current_pos, director*step)
            zero_initial = self.current_pos - self.zero
            zero_final = final - self.zero
            step_angle = np.arccos((np.inner(zero_initial, zero_final))/(np.linalg.norm(zero_initial)*np.linalg.norm(zero_final)))
            step_size = np.linalg.norm(zero_final) - np.linalg.norm(zero_initial)
            self.current_pos = final
            print(f'Step Size: {step_size}, Step Angle: {step_angle}, Current Position: {self.current_pos}.')
printer = Printer(1,0,0)
printer.move(2,0.1,0)
printer.move(2,0.1,np.pi/2)