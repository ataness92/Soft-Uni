def concatenate(*args, **kwargs):
    string = ''.join(args)
    for key, word in kwargs.items():
        string = string.replace(key,word)

    return string

print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))
print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))
