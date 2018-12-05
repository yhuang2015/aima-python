import agents as ag
# import envgui as gui
import importlib
import traceback
import search
from math import inf
import math

class PathFinding(search.Problem):
    def __init__(self, start, goal, sword):
        self.start = start
        self.goal = goal
        self.sword = sword
        open_list = []
        closed_list = []
        open_list.append(start)

    def actions(self, state):
        return [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]

    def result(self, state, action):
        if state[0] > (len(maze) - 1) or state[0] < 0 or state[1] > (
                len(maze[len(maze) - 1]) - 1) or state[1] < 0:
            return
        if maze[state[0]][state[1]] == 2:
            return
        if maze[state[0]][state[1]] == -1:
            self.sword = True
        if (maze[state[0]][state[1]] == -1) and (self.sword == True):
            return self.result(state, action)

    def heuristic(a, b, bag):
        (x1, y1) = a
        (x2, y2) = b
        if bag == True:
            return math.sqrt(abs(x1 - x2) + abs(y1 - y2))
        else:
            return abs(x1 - x2) + abs(y1 - y2)

    def path_cost(self, c, state1, action, state2):
        neighbors = self.maze[state1]
        cost = neighbors[state2]
        return c + cost

    def goal_test(self, state):
        return state == goal

    def h(self, node):
        state = node.state
        if self.goal_test(state):
            return 0
        else:
            return 1

    def printPath(self, state):
        path = []
        current = state
        while current is not None:
            path.append(current.position)
            current = current.value
        return path[::-1]


maze = [[0, 0, 0, 0, 2, 0, 0, 0, 0, 0],
        [0, 0, -1, 0, 2, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 2, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 2, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 2, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 2, 0, 0, 2, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

start = (0,0)
goal = (6,8)
sword = False

PathFinding_puzzle = PathFinding(start, goal, sword)

mySearches = [
    PathFinding_puzzle
]