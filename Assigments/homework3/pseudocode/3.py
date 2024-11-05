def calculate_total_energy(sequence, energy_matrix):
    total_energy = 0
    for i in range(len(sequence) - 1):
        total_energy += energy_matrix[sequence[i]][sequence[i+1]]
    return total_energy

def find_optimal_energy(current_position, remaining_parts, current_sequence, energy_matrix):
    if not remaining_parts:
        return calculate_total_energy(current_sequence, energy_matrix)
    
    min_energy = float('inf') 
    
    for next_part in remaining_parts:
        current_sequence.append(next_part)
        new_position = next_part
        
        energy = find_optimal_energy(new_position, remaining_parts - {next_part}, current_sequence, energy_matrix)

        min_energy = min(min_energy, energy)

        current_sequence.pop()
    
    return min_energy