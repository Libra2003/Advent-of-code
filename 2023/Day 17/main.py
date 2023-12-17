from heapq import heappop, heappush

matrix = [[int(value) for value in row] for row in open('input.txt').read().strip().split('\n')]
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def is_in_range(position, array):
    return position[0] in range(len(array)) and position[1] in range(len(array[0]))

def find_minimum_cost(min_distance, max_distance):
    # cost, x, y, disallowedDirection
    priority_queue = [(0, 0, 0, -1)]
    visited = set()
    costs = {}

    while priority_queue:
        cost, x, y, disallowed_direction = heappop(priority_queue)

        if x == len(matrix) - 1 and y == len(matrix[0]) - 1:  # goal x, goal y
            return cost

        if (x, y, disallowed_direction) in visited:
            continue

        visited.add((x, y, disallowed_direction))

        for direction in range(4):
            cost_increase = 0

            if direction == disallowed_direction or (direction + 2) % 4 == disallowed_direction:
                # can't go this way
                continue

            for distance in range(1, max_distance + 1):
                new_x = x + directions[direction][0] * distance
                new_y = y + directions[direction][1] * distance

                if is_in_range((new_x, new_y), matrix):
                    cost_increase += matrix[new_x][new_y]

                    if distance < min_distance:
                        continue

                    new_cost = cost + cost_increase

                    if costs.get((new_x, new_y, direction), 1e100) <= new_cost:
                        continue

                    costs[(new_x, new_y, direction)] = new_cost
                    heappush(priority_queue, (new_cost, new_x, new_y, direction))

print(find_minimum_cost(1, 3))
print(find_minimum_cost(4, 10))
