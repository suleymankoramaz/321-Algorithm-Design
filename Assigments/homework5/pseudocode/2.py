def secure_perimeter(sensors):
    if len(sensors) == 0:
        return 0
    elif len(sensors) == 1:
        return 1
    
    # Sort sensors based on coordinates
    sensors.sort(key=lambda sensor: sensor.x)
    
    mid = len(sensors) // 2
    left_half = sensors[:mid]
    right_half = sensors[mid:]
    
    # Recursively find the minimum sensors for each half
    left_min = secure_perimeter(left_half)
    right_min = secure_perimeter(right_half)
    
    
    # Find the sensors on the dividing line
    mid_x = sensors[mid].x

    # Use the distance between mid_x and the nearest endpoint to determine the radius
    radius = min(abs(mid_x - left_half[-1].x), abs(mid_x - right_half[0].x))

    dividing_line = [sensor for sensor in sensors if abs(sensor.x - mid_x) < radius]
    
    # Sort the dividing line based on y-coordinates
    dividing_line.sort(key=lambda sensor: sensor.y)
    
    # Calculate the minimum sensors for the dividing line
    min_line = min_sensors_dividing_line(dividing_line, radius)
    
    return left_min + right_min + min_line

def min_sensors_dividing_line(dividing_line, radius):
    min_sensors = 1
    rightmost_sensor = dividing_line[0]
    
    for sensor in dividing_line[1:]:
        if sensor.y - radius > rightmost_sensor.y:
            min_sensors += 1
            rightmost_sensor = sensor
            
    return min_sensors