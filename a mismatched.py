# A* Search - Misplaced Tiles Heuristic

import heapq


def print_state(state):
    for i in range(0, 9, 3):
        print(state[i], state[i + 1], state[i + 2])
    print()


# Heuristic: Number of misplaced tiles
def misplaced_tiles(state, goal):
    count = 0

    for i in range(9):
        if state[i] != 0 and state[i] != goal[i]:
            count += 1

    return count


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

    # Priority queue: (f, g, state, path)
    pq = []

    h = misplaced_tiles(initial, goal)

    heapq.heappush(
        pq,
        (h, 0, initial, [initial])
    )

    visited = set()

    while pq:

        f, g, state, path = heapq.heappop(pq)

        if state == goal:
            return path

        if state in visited:
            continue

        visited.add(state)

        for neighbor in get_neighbors(state):

            if neighbor not in visited:

                new_g = g + 1

                new_h = misplaced_tiles(
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

    print("A* SEARCH - MISPLACED TILES")
    print("--------------------------------")

    print("Solution found!")
    print("Number of moves:", len(solution) - 1)

    for i, state in enumerate(solution):
        print("\nStep", i)
        print_state(state)

else:
    print("No solution found.")