from collections import deque

quantity = int(input())
remove_queue = 0
quantity_of_food = deque([int(x) for x in input().split()])
complete = True
print(max(quantity_of_food))
for _ in range(len(quantity_of_food)):
    remove_queue = quantity_of_food[0]
    if remove_queue > quantity:
        complete = False
        print("Orders left: ", end='')
        print(*quantity_of_food)
        break
    else:
        remove_queue = quantity_of_food.popleft()
        quantity-=remove_queue
  
if complete:
    print("Orders complete")
