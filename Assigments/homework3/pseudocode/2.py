def find_optional_assigment(users, processes, processors, cost_matrix):
    all_permutations = list(permutations(range(len(users))))

    best_assignment = None
    min_cost = float('inf')

    for permutation in all_permutations:
        current_cost = 0

        for i in range(len(processors)):
            user_index, process_index = divmod(permutation[i], len(users))
            current_cost += cost_matrix[processors[i]][users[user_index]][processes[process_index]]

        if current_cost < min_cost:
            min_cost = current_cost
            best_assignment = permutation

    return best_assignment, min_cost