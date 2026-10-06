import random

def is_solvable(state):
    """
    Checks if an 8-puzzle configuration is solvable.
    An 8-puzzle is solvable if the number of inversions is even.
    """
    # Remove the blank tile (0) to count inversions
    arr = [tile for tile in state if tile != 0]
    inversions = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                inversions += 1
    return inversions % 2 == 0

def generate_random_solvable_state(goal_state):
    """Generates a random state that is guaranteed to be solvable."""
    state_list = list(goal_state)
    while True:
        random.shuffle(state_list)
        random_tuple = tuple(state_list)
        # It must be solvable and not already equal to the goal state
        if is_solvable(random_tuple) and random_tuple != goal_state:
            return random_tuple

def get_blank_position(state):
    """Finds the index of the blank tile (0) in the board."""
    return state.index(0)

def get_neighbors(state):
    """Generates all valid neighboring states from the current state."""
    neighbors = []
    blank_idx = get_blank_position(state)
    row, col = divmod(blank_idx, 3)
    
    # Possible movements: Up, Down, Left, Right
    movements = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    for r_offset, c_offset in movements:
        new_row, new_col = row + r_offset, col + c_offset
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_blank_idx = new_row * 3 + new_col
            state_list = list(state)
            # Swap blank tile with the neighbor
            state_list[blank_idx], state_list[new_blank_idx] = state_list[new_blank_idx], state_list[blank_idx]
            neighbors.append(tuple(state_list))
            
    return neighbors

def dfs_solve(start_state, goal_state):
    """Solves the 8-puzzle using Depth-First Search (DFS)."""
    # Stack stores tuples of (current_state, path_of_states)
    stack = [(start_state, [start_state])]
    visited = {start_state}
    
    while stack:
        current_state, path = stack.pop()
        
        if current_state == goal_state:
            return path
            
        for neighbor in get_neighbors(current_state):
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append((neighbor, path + [neighbor]))
                    
    return None

def print_board(state):
    """Prints a 1D tuple state as a clean 3x3 grid."""
    for i in range(0, 9, 3):
        print(f" {state[i]} {state[i+1]} {state[i+2]} ")
    print()

if __name__ == "__main__":
    # Define the target Final State
    goal = (1, 2, 3, 
            4, 5, 6, 
            7, 8, 0)
    
    print("Generating a random solvable initial state...")
    start = generate_random_solvable_state(goal)
    
    print("\n[Initial State]")
    print_board(start)
    
    print("[Final State]")
    print_board(goal)
    
    print("Searching for a path using DFS (this might take a few moments)...")
    solution_path = dfs_solve(start, goal)
    
    if solution_path:
        print(f"Success! Reached the final state in {len(solution_path) - 1} moves.\n")
        
        # Print the transitions step by step
        for step_num, state in enumerate(solution_path):
            if step_num == 0:
                print("Start:")
            elif step_num == len(solution_path) - 1:
                print(f"Step {step_num} (Goal Reached):")
            else:
                print(f"Step {step_num}:")
            print_board(state)
    else:
        print("No path could be found by DFS.")

