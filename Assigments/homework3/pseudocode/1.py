def find_best_combinations(current_index, current_combination, all_stores):
    if current_index == len(all_stores):
        return calculate_discount(current_combination), current_combination
    

    with_current_store = find_best_combinations(current_index + 1, current_combination + [all_stores[current_index]], all_stores)
    without_current_store = find_best_combinations(current_index + 1, current_combination, all_stores)
    

    if with_current_store[0] > without_current_store[0]:
        return with_current_store
    else:
        return without_current_store