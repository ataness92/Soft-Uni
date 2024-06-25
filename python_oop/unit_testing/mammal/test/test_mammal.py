from unittest import TestCase, main

from project.mammal import Mammal


class TestMammal(TestCase):

    def setUp(self) -> None:
        self.mammal = Mammal("Nasko", "example", "muu")

    def test_init(self):
        self.assertEqual("Nasko", self.mammal.name)
        self.assertEqual("example", self.mammal.type)
        self.assertEqual("muu", self.mammal.sound)
        self.assertEqual("animals", self.mammal.get_kingdom())

    def test_make_sound(self):
        self.assertEqual("Nasko makes muu", self.mammal.make_sound())

    def test_info(self):
        self.assertEqual(f"Nasko is of type example", self.mammal.info())

if __name__ == "__main__":
    main()