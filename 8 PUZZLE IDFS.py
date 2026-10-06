import random

def is_solvable(state):
    """Checks if an 8-puzzle configuration is solvable using inversion counts."""
    arr = [tile for tile in state if tile != 0]
    inversions = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                inversions += 1
    return inversions % 2 == 0

def generate_random_solvable_state(goal_state):
    """Generates a random state guaranteed to be solvable."""
    state_list = list(goal_state)
    while True:
        random.shuffle(state_list)
        random_tuple = tuple(state_list)
        if is_solvable(random_tuple) and random_tuple != goal_state:
            return random_tuple

def get_neighbors(state):
    """Generates all valid neighboring states from the current state."""
    neighbors = []
    blank_idx = state.index(0)
    row, col = divmod(blank_idx, 3)
    
    # Movements: Up, Down, Left, Right
    movements = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    for r_offset, c_offset in movements:
        new_row, new_col = row + r_offset, col + c_offset
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_blank_idx = new_row * 3 + new_col
            state_list = list(state)
            state_list[blank_idx], state_list[new_blank_idx] = state_list[new_blank_idx], state_list[blank_idx]
            neighbors.append(tuple(state_list))
            
    return neighbors

def depth_limited_search(state, goal_state, depth, visited):
    """
    Helper function that performs a depth-limited DFS.
    Returns the path as a list of states if found, otherwise None.
    """
    if state == goal_state:
        return [state]
    if depth <= 0:
        return None
        
    visited.add(state)
    
    for neighbor in get_neighbors(state):
        if neighbor not in visited:
            result = depth_limited_search(neighbor, goal_state, depth - 1, visited)
            if result is not None:
                return [state] + result
                
    # Backtrack: remove state from visited list for other parallel branches
    visited.remove(state)
    return None

def iddfs_solve(start_state, goal_state, max_depth=50):
    """Solves the 8-puzzle using Iterative Deepening DFS (IDDFS)."""
    for depth in range(max_depth):
        print(f"Searching at depth limit: {depth}...")
        visited = set()
        path = depth_limited_search(start_state, goal_state, depth, visited)
        if path is not None:
            return path
    return None

def print_board(state):
    """Prints a 1D tuple state as a clean 3x3 grid."""
    for i in range(0, 9, 3):
        print(f" {state[i]} {state[i+1]} {state[i+2]} ")
    print()

if __name__ == "__main__":
    # Target Final State
    goal = (1, 2, 3, 
            4, 5, 6, 
            7, 8, 0)
    
    print("Generating a random solvable initial state...")
    start = generate_random_solvable_state(goal)
    
    print("\n[Initial State]")
    print_board(start)
    
    print("[Final State]")
    print_board(goal)
    
    print("Starting IDDFS Search...")
    solution_path = iddfs_solve(start, goal)
    
    if solution_path:
        print(f"\nSuccess! Found the SHORTEST optimal path in {len(solution_path) - 1} moves.\n")
        for step_num, state in enumerate(solution_path):
            if step_num == 0:
                print("Start:")
            elif step_num == len(solution_path) - 1:
                print(f"Step {step_num} (Goal Reached):")
            else:
                print(f"Step {step_num}:")
            print_board(state)
    else:
        print("\nCould not find a solution within the depth limit.")
