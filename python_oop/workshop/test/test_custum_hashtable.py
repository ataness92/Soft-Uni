from unittest import TestCase, main

from python_oop.workshop.custom_hashtable import HashTable


class TestHashTable(TestCase):

    def setUp(self):
        self.h = HashTable()

    def test_init(self):
        self.assertEqual(self.h._HashTable__keys, [None, None, None, None])
        self.assertEqual(self.h._HashTable__values, [None, None, None, None])
        self.assertEqual(self.h._HashTable__length, 4)

    def test_count(self):
        result = self.h.count()
        self.assertEqual(result, 0)

    def test_length(self):
        self.assertEqual(len(self.h), 4)


if __name__ == "__main__":
    main()