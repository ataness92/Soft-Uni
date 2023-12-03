my_stops = input()

def add_stop(stops,index, string):
    if 0 <= index < len(stops):
        stops = stops[:index] + string + stops[index:]
    return stops

def remove_stop(stops, start_index, end_index):
    if 0 <= start_index < len(stops) and 0 <= end_index <= len(stops):
        stops = stops[:start_index] + stops[(end_index+1):]
    return stops

def switch(stops, old_string, new_string):
    stops = stops.replace(old_string, new_string)
    return stops
while True:
    command = input().split(':')

    if command[0] == 'Travel':
        break
    elif command[0] == 'Add Stop':
        my_stops = add_stop(my_stops,int(command[1]),command[2])
    elif command[0] == 'Remove Stop':
        my_stops = remove_stop(my_stops,int(command[1]),int(command[2]))
    elif command[0] == 'Switch':
        my_stops = switch(my_stops, command[1], command[2])
    print(my_stops)

print(f'Ready for world tour! Planned stops: {my_stops}')