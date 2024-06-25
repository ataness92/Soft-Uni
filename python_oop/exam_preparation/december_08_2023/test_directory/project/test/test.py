from collections import deque
from unittest import TestCase, main

from project.railway_station import RailwayStation


class TestRailwayStation(TestCase):

    def setUp(self):
        self.rs = RailwayStation("Plovdiv")

    def test_init(self):
        self.assertEqual("Plovdiv", self.rs.name)
        self.assertEqual(deque([]), self.rs.arrival_trains)
        self.assertEqual(deque([]), self.rs.departure_trains)

    def test_name_setter_value_less_than_three(self):
        with self.assertRaises(ValueError) as ve:
            self.rs.name = "Pld"

        self.assertEqual("Name should be more than 3 symbols!", str(ve.exception))

    def test_new_arrival_on_board(self):
        self.rs.new_arrival_on_board("Plovdiv Train Has Some"
                                     " New Arrivals!")

        self.rs.new_arrival_on_board("Plovdiv Train Has Some New Arrivals!")
        self.assertEqual("Plovdiv Train Has Some New Arrivals!", self.rs.arrival_trains[-1])

    def test_train_has_arrived_not_arrival_trains(self):
        self.assertEqual(len(self.rs.arrival_trains), 0)
        self.assertEqual(len(self.rs.departure_trains), 0)
        self.rs.arrival_trains.append("Some info")

        result = self.rs.train_has_arrived("Some info")
        expected_message = f"Some info is on the platform and will leave in 5 minutes."
