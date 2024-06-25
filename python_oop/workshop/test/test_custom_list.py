from unittest import TestCase, main

from python_oop.workshop.custum_list import CustomList


class TestCustomList(TestCase):

    def setUp(self):
        self.l = CustomList()

    def test_init(self):
        self.assertEqual(self.l._CustomList__values, [])

    def test_add_only_one_element(self):
        self.assertEqual(self.l._CustomList__values, [])
        self.l.append(5)
        self.assertEqual(self.l._CustomList__values, [5])

    def test_has_existing_elements_using_add_appends_it_to_end(self):
        self.l._CustomList__values = [1, 2, 3]
        self.assertEqual(self.l._CustomList__values, [1, 2, 3])

        self.l.append(5)
        self.assertEqual(self.l._CustomList__values, [1, 2, 3, 5])

        last_element = self.l._CustomList__values[-1]
        self.assertEqual(last_element, 5)

        self.assertEqual(len(self.l._CustomList__values), 4)

    def test_returns_the_same_list_as_memory_loc(self):
        self.l._CustomList__values = [1, 2, 3]

        result = self.l.append(5)

        self.assertIs(result, self.l._CustomList__values)

    def test_check_index_is_positive(self):
        pass

    def test_index_argument_is_positive_or_zero_integer(self):
        pass





if __name__ == "__main__":
    main()