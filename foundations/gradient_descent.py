import math
class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        guess = init
        for i in range(iterations):
            gradient = 2 * guess * learning_rate
            guess -= gradient
        return round(guess, 5)
