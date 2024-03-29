import random as r
import matplotlib.pyplot as plt

class RandowWalk:

    def __init__(self, num = 5000):         
        self.num = num        # Number of dots
        self.x_values = [0]
        self.y_values = [0]
        self.fill_walk()


    def fill_walk(self):
        while len(self.x_values) < self.num:

            x_step = self.__get_step()
            y_step = self.__get_step()

            if x_step == 0 and y_step == 0:
                continue

            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)


    def __get_step(self):
        direction = r.choice([1, -1])
        distance = r.choice(list(range(0,5)))
        return direction * distance


rw = RandowWalk()
plt.figure(dpi = 128, figsize = (10, 6))      #the size of figure
plt.scatter(rw.x_values, rw.y_values, s = 5, c = 'black')
plt.scatter(0, 0, s = 100, c = 'green')
plt.scatter(rw.x_values[-1], rw.y_values[-1], s = 100, c = 'red')
plt.show()
