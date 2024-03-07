from project.worker import Worker
from project.animal import Animal
from project.lion import Lion
from project.tiger import Tiger
from project.cheetah import Cheetah
from project.keeper import Keeper
from project.vet import Vet
from project.caretaker import Caretaker
from project.zoo import Zoo

import unittest

z = Zoo("My Zoo", 500, 3, 3)
z.add_animal(Lion("Leo", "Male", 3), 100)
z.add_animal(Tiger("Tigy", "Female", 4), 100)
z.add_animal(Cheetah("Chi", "Female", 2), 100)
print(z.animals_status())

# class Tests(unittest.TestCase):
#     def test_animal_status(self):
#         z = Zoo("My Zoo", 500, 3, 3)
#         z.add_animal(Lion("Leo", "Male", 3), 100)
#         z.add_animal(Tiger("Tigy", "Female", 4), 100)
#         z.add_animal(Cheetah("Chi", "Female", 2), 100)
#         res = z.animals_status()
#         self.assertEqual(res,
#                          "You have 3 animals\n----- 1 Lions:\nName: Leo, Age: 3, Gender: Male\n----- 1 Tigers:\nName: Tigy, Age: 4, Gender: Female\n----- 1 Cheetahs:\nName: Chi, Age: 2, Gender: Female")
#
# if __name__ == "__main__":
#     unittest.main()