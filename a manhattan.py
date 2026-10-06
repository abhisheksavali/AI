# A* Search - Manhattan Distance Heuristic

import heapq


def print_state(state):
    for i in range(0, 9, 3):
        print(state[i], state[i + 1], state[i + 2])
    print()


# Heuristic: Manhattan Distance
def manhattan_distance(state, goal):

    distance = 0

    for tile in range(1, 9):

        current_position = state.index(tile)
        goal_position = goal.index(tile)

        current_row = current_position // 3
        current_col = current_position % 3

        goal_row = goal_position // 3
        goal_col = goal_position % 3

        distance += abs(current_row - goal_row)
        distance += abs(current_col - goal_col)

    return distance


# Generate possible next states
def get_neighbors(state):

    neighbors = []

    zero = state.index(0)

    row = zero // 3
    col = zero % 3

    moves = [
        (-1, 0),   # Up
        (1, 0),    # Down
        (0, -1),   # Left
        (0, 1)     # Right
    ]

    for dr, dc in moves:

        new_row = row + dr
        new_col = col + dc

        if 0 <= new_row < 3 and 0 <= new_col < 3:

            new_zero = new_row * 3 + new_col

            new_state = list(state)

            new_state[zero], new_state[new_zero] = \
                new_state[new_zero], new_state[zero]

            neighbors.append(tuple(new_state))

    return neighbors


def a_star(initial, goal):

    # Priority queue
    # (f, g, state, path)

    pq = []

    h = manhattan_distance(
        initial,
        goal
    )

    heapq.heappush(
        pq,
        (h, 0, initial, [initial])
    )

    visited = set()

    while pq:

        f, g, state, path = heapq.heappop(pq)

        # Goal test
        if state == goal:
            return path

        if state in visited:
            continue

        visited.add(state)

        # Generate successors
        for neighbor in get_neighbors(state):

            if neighbor not in visited:

                new_g = g + 1

                new_h = manhattan_distance(
                    neighbor,
                    goal
                )

                new_f = new_g + new_h

                heapq.heappush(
                    pq,
                    (
                        new_f,
                        new_g,
                        neighbor,
                        path + [neighbor]
                    )
                )

    return None


# Initial state
initial = (
    1, 2, 3,
    4, 0, 6,
    7, 5, 8
)

# Goal state
goal = (
    1, 2, 3,
    4, 5, 6,
    7, 8, 0
)


# Run A*
solution = a_star(initial, goal)


# Display solution
if solution:

    print("A* SEARCH - MANHATTAN DISTANCE")
    print("-----------------------------------")

    print("Solution found!")
    print("Number of moves:", len(solution) - 1)

    for i, state in enumerate(solution):

        print("\nStep", i)

        print_state(state)

else:

    print("No solution found.")