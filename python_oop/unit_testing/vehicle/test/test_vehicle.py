from unittest import TestCase, main
from project.vehicle import Vehicle

class TestVehicle(TestCase):

    def setUp(self) -> None:
        self.vehicle = Vehicle(0.2, 1.5)

    def test_init(self):
        self.assertEqual(0.2, self.vehicle.fuel)
        self.assertEqual(0.2, self.vehicle.capacity)
        self.assertEqual(1.5, self.vehicle.horse_power)
        self.assertEqual(1.25, self.vehicle.DEFAULT_FUEL_CONSUMPTION)

    def test_drive_if_fuel_is_less_than_needed(self):
        self.vehicle.fuel = self.vehicle.fuel_consumption*5-1

        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(5)

        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_drive_if_fuel_is_enough(self):
        self.vehicle.fuel = self.vehicle.fuel_consumption*5
        self.vehicle.drive(5)
        self.assertEqual(0, self.vehicle.fuel)

    def test_refuel_when_fuel_is_more_than_capacity(self):
        self.vehicle.fuel += 10

        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(10)

        self.assertEqual("Too much fuel", str(ex.exception))

    def test_refuel_when_fuel_is_not_more_than_capacity(self):
        self.vehicle.capacity = 10
        self.vehicle.fuel = 5
        self.vehicle.refuel(1)

        self.assertEqual(6, self.vehicle.fuel)

    def test_str(self):
        self.assertEqual(f"The vehicle has 1.5 " \
                         f"horse power with 0.2 fuel left "
                         f"and 1.25 fuel "
                         f"consumption", str(self.vehicle))

if __name__ == "__main__":
    main()

