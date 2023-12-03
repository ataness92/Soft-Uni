items_dict = {}
flag = 0

def check_target(my_dict, my_flag):
    for key,value in my_dict.items():
        if value >= 250:
            if key == 'shards':
                print("Shadowmourne obtained!")
            elif key == 'motes':
                print("Dragonwrath obtained!")
            elif key == 'fragments':
                print("Valanyr obtained!")
            my_dict[key] = value - 250
            my_flag = 1

    return my_dict, my_flag

while True:
    obtained = 0
    list_input = input().split()
    for x in range(0, len(list_input), 2):
        if list_input[x+1].lower() not in items_dict.keys():
            items_dict[list_input[x+1].lower()] = int(list_input[x])
        else:
            items_dict[list_input[x+1].lower()] += int(list_input[x])

        items_dict, flag = check_target(items_dict, flag)

        if flag == 1:
            obtained = 1
            break

    if obtained == 1:
        break

if 'shards' in items_dict.keys():
    print(f"shards: {items_dict['shards']}")
else:
    print("shards: 0")
if 'fragments' in items_dict.keys():
    print(f"fragments: {items_dict['fragments']}")
else:
    print("fragments: 0")
if 'motes' in items_dict.keys():
    print(f"motes: {items_dict['motes']}")
else:
    print("motes: 0")

for key,value in items_dict.items():
    if key not in ['shards','fragments','motes']:
        print(f'{key}: {value}')

