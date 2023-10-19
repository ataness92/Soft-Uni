def chair_info(room_list: list):
    room = 1
    free_chairs = 0
    needed_room = False
    for info in information:
        if len(info[0]) < int(info[1]):
            needed_room = True
            print(f"{abs(len(info[0])-int(info[1]))} more chairs needed in room {room}")
        elif len(info[0]) > int(info[1]):
            free_chairs += len(info[0]) - int(info[1])
        room += 1
    return free_chairs, needed_room


number_of_rooms = int(input())
information = []

for i in range(number_of_rooms):
    information.append([x for x in input().split()])

free_chairs, needed_room  = chair_info(information)

if free_chairs >= 0 and not needed_room:
    print(f'Game On, {free_chairs} free chairs left')
