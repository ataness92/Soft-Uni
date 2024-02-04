def age_assignment(*names, **kwargs):
    my_dict = {}
    for name in names:
        my_dict[name] = kwargs.get(name[0])

    return '\n'.join(f"{x} is {y} years old." for x, y in sorted(my_dict.items()))

print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61)) 