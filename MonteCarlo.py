# Calculate Pi number using Monte Carlo method
# Let's consider a circle (r = 1, [0, 0]) and a square ([-1, -1], [1, -1], [1, 1], [-1, 1]) that encircles the circle.
# Pi = area_of_square * (points that belong to circle / all chosen points)
# The points are chosen according to uniform distribution

import random
from math import sqrt

random.seed(10)


class MonteCarlo:

    def __init__(self, simulations):
        self.simulations = simulations

    @staticmethod
    def generate_random_point(a=-1, b=1):
        if not b > a:
            raise ValueError('Condition b > a was NOT met.')
        return random.uniform(a, b), random.uniform(a, b)

    @staticmethod
    def is_in_circle(point: tuple, coors=(0, 0), radius=1):
        distance = sqrt((point[0] - coors[0]) ** 2 + (point[1] - coors[1]) ** 2)
        if distance < radius:
            return True
        else:
            return False

    def estimate(self):
        points = [self.generate_random_point() for _ in range(self.simulations)]
        flags = [self.is_in_circle(point) for point in points]
        areaOfSquare = 4
        return areaOfSquare * (flags.count(True) / len(points))
