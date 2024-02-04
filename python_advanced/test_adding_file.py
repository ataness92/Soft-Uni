import os

path = os.path.join("test.txt")

with open("test.txt", 'a') as file:
    file.writelines("Atanas This Is Your First File")


print("Atanas")