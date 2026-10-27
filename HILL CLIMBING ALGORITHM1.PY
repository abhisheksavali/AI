import itertools

def calculate_cost(state):
 
    attacks = 0
    n = len(state)
    for i in range(n):
        for j in range(i + 1, n):
            
            if state[i] == state[j]:
                attacks += 1
            
            elif abs(state[i] - state[j]) == abs(i - j):
                attacks += 1
    return attacks

def get_best_neighbor(state):
    
 
    n = len(state)
    best_neighbor = None
    min_cost = float('inf')
    best_swap_indices = (float('inf'), float('inf'))
    
   
    for i, j in itertools.combinations(range(n), 2):
       
        neighbor = list(state)
        neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
        
        cost = calculate_cost(neighbor)
        
        
        if cost < min_cost:
            min_cost = cost
            best_neighbor = neighbor
            best_swap_indices = (i, j)
        elif cost == min_cost:
          
            if (i, j) < best_swap_indices:
                best_neighbor = neighbor
                best_swap_indices = (i, j)
                
    return best_neighbor, min_cost, best_swap_indices

def hill_climbing_n_queens(initial_state):
   
    current_state = list(initial_state)
    current_cost = calculate_cost(current_state)
    
    print("--- Start Hill Climbing Optimization ---")
    print(f"Initial State: {current_state} | Initial Cost: {current_cost}\n")
    
    step = 1
    while True:
        neighbor, neighbor_cost, swapped_cols = get_best_neighbor(current_state)
        
        print(f"Step {step}:")
        print(f"  Current State : {current_state} (Cost: {current_cost})")
        print(f"  Best Neighbor : {neighbor} (Cost: {neighbor_cost}) via swapping columns {swapped_cols}")
        
       
        if neighbor_cost >= current_cost:
            print("\nTermination: No neighbor has a lower cost. Local minimum reached.")
            break
            
        current_state = neighbor
        current_cost = neighbor_cost
        step += 1
    
       
        if current_cost == 0:
            print("\nGoal state reached! Global minimum found.")
            break
            
    return current_state, current_cost


initial_configuration = [3, 1, 2, 0]
final_state, final_cost = hill_climbing_n_queens(initial_configuration)

print(f"\nFinal Board Configuration: {final_state}")
print(f"Final Attacking Pairs Cost : {final_cost}")