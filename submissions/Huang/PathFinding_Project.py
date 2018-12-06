import math

class Node():

    def __init__(self, value, position):
        self.value = value
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0
        self.bag = []
        self.collected = False

    def __eq__(self, other):
        return self.position == other.position


def astar(maze, start, end):

    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, end)
    end_node.g = end_node.h = end_node.f = 0


    open_list = []
    closed_list = []

    open_list.append(start_node)

    while len(open_list) > 0:

        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index

        open_list.pop(current_index)
        closed_list.append(current_node)

        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.value
            return path[::-1]

        checkitem_node = current_node
        bagnow = []
        while checkitem_node is not None:
            bagnow.append(maze[checkitem_node.position[0]][checkitem_node.position[1]])
            checkitem_node = checkitem_node.value

        children = []

        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]:

            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (len(maze[len(maze)-1]) -1) or node_position[1] < 0:
                continue

            if maze[node_position[0]][node_position[1]] == 2:
                continue

            for items in bagnow:
                if items == -1:
                    current_node.collected = True

            if (maze[node_position[0]][node_position[1]] == 1) and (current_node.collected == False):
                continue

            new_node = Node(current_node, node_position)

            children.append(new_node)

        for child in children:

            #for closed_child in closed_list:
             #   if child == closed_child:
              #      continue
            sword = False
            child.bag.append(maze[child.position[0]][child.position[1]])
            child.g = current_node.g + 1
            for items in child.bag:
                if items == -1:
                    sword = True
            if sword == False:
                child.h = ((child.position[0] - end_node.position[0]) ** 2) + ((child.position[1] - end_node.position[1]) ** 2)
            else:
                child.h = math.sqrt(((child.position[0] - end_node.position[0]) ** 2) + ((child.position[1] - end_node.position[1]) ** 2))
            child.f = child.g + child.h

            for open_node in open_list:
                if child == open_node and child.g > open_node.g:
                    continue

            open_list.append(child)


def main():

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

    start = (0, 0)
    end = (6, 8)

    mazepath = maze
    path = astar(maze, start, end)
    for position in path:
        mazepath[position[0]][position[1]] = '.'
    for i in range(len(mazepath[1])):
        print(mazepath[i])


if __name__ == '__main__':
    main()