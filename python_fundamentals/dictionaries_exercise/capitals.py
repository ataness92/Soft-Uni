countries = input().split(', ')
capitals = input().split(', ')

final_information = {countries[index] : capitals[index] for index in range(len(capitals))}

#new_dect = zip(countries,capitals)

for x, y in final_information.items():
    print(f"{x} -> {y}")

#print(tuple(new_dect))