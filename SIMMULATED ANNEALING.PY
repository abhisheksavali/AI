import random
import math

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

def get_random_neighbor(state):

    neighbor = list(state)
    n = len(state)
    
    
    col = random.randint(0, n - 1)
    
  
    current_row = state[col]
    available_rows = [r for r in range(n) if r != current_row]
    new_row = random.choice(available_rows)
    
    neighbor[col] = new_row
    return neighbor

def simulated_annealing_8_queens(initial_state, initial_temp=100.0, cooling_rate=0.995, min_temp=0.001):

    current_state = list(initial_state)
    current_cost = calculate_cost(current_state)
    T = initial_temp
    
    print("--- Start Simulated Annealing ---")
    print(f"Initial State: {current_state} | Cost: {current_cost}\n")
    
    iteration = 0
   
    while T > min_temp:
        
        if current_cost == 0:
            break
            
       
        next_state = get_random_neighbor(current_state)
        next_cost = calculate_cost(next_state)
        
       
        delta_E = current_cost - next_cost
        
       
        if delta_E > 0:
            
            current_state = next_state
            current_cost = next_cost
        else:
          
            probability = math.exp(delta_E / T)
            if random.random() < probability:
                current_state = next_state
                current_cost = next_cost
                
        
        T *= cooling_rate
        iteration += 1
        
       
        if iteration % 200 == 0:
            print(f"Iteration {iteration:4d} | Temp: {T:.4f} | Current Cost: {current_cost}")
            
    print(f"\nOptimization Finished after {iteration} steps.")
    return current_state, current_cost


random.seed(42) 
initial_board = [random.randint(0, 7) for _ in range(8)]

final_board, final_cost = simulated_annealing_8_queens(initial_board)

print(f"Final State Config: {final_board}")
print(f"Final State Cost  : {final_cost} (Attacking pairs)")