def water_jug_dfs(jug1_capacity, jug2_capacity, target):
    stack = [(0, 0)]  
    visited = set() 

    while stack:
        current_state = stack.pop()

        if current_state in visited:
            continue
        visited.add(current_state)

        jug1, jug2 = current_state

        print(f"Jug1: {jug1}, Jug2: {jug2}")

        if jug1 == target or jug2 == target:
            print("Target reached!")
            return True

        possible_moves = [
            (jug1_capacity, jug2),         
            (jug1, jug2_capacity),         
            (0, jug2),                     
            (jug1, 0),                      
            (min(jug1 + jug2, jug1_capacity), max(0, jug2 - (jug1_capacity - jug1))),  
            (max(0, jug1 - (jug2_capacity - jug2)), min(jug1 + jug2, jug2_capacity))   
        ]

        for move in possible_moves:
            if move not in visited:
                stack.append(move)

    print("No solution found.")
    return False
jug1_capacity = 4
jug2_capacity = 3
target = 2

water_jug_dfs(jug1_capacity, jug2_capacity, target)
