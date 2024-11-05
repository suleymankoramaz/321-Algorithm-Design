def max_non_intersecting_antennas(antennas):
    # Sort antennas based on coverage endpoints
    antennas.sort(key=lambda antenna: antenna.end_point)
    
    selected_antennas = []
    current_coverage = float('-inf')
    
    # Iterate through sorted antennas
    for antenna in antennas:
        if antenna.start_point > current_coverage:
            selected_antennas.append(antenna)
            current_coverage = antenna.end_point
            
    return len(selected_antennas), selected_antennas
