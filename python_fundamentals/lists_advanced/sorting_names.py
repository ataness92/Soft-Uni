list_of_names = input().split(', ')

print(list(sorted(list_of_names, key= lambda x: (-len(x), x))))

#def sorting(element):
#    return len(element)
#first_sort = sorted(list_of_names,reverse=True, key = sorting)#
#
#for x in range(len(first_sort)-2):
#    if len(first_sort[x]) == len(first_sort[x+1]):
#        first_sort[x], first_sort[x+1] = sorted([first_sort[x], first_sort[x+1]])

#print(first_sort)