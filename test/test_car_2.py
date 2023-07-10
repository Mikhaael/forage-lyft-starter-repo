import datetime
import unittest
from battery import SpindlerBattery

from car_factor import CarriganTires, OctoprimeTires


class TestCalliope(unittest.TestCase):
    # Existing tests...

    def test_spindler_battery_needs_service(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 4)
        battery = SpindlerBattery(last_service_date, 100)
        self.assertTrue(battery.needs_service())

    def test_spindler_battery_does_not_need_service(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 2)
        battery = SpindlerBattery(last_service_date, 100)
        self.assertFalse(battery.needs_service())

    def test_carrigan_tires_needs_service(self):
        tire_wear = [0.7, 0.8, 0.9, 0.95]
        tires = CarriganTires(tire_wear)
        self.assertTrue(tires.needs_service())

    def test_carrigan_tires_do_not_need_service(self):
        tire_wear = [0.7, 0.8, 0.9, 0.85]
        tires = CarriganTires(tire_wear)
        self.assertFalse(tires.needs_service())

    def test_octoprime_tires_needs_service(self):
        tire_wear = [0.5, 0.8, 0.9, 0.85]
        tires = OctoprimeTires(tire_wear)
        self.assertTrue(tires.needs_service())

    def test_octoprime_tires_do_not_need_service(self):
        tire_wear = [0.5, 0.8, 0.7, 0.85]
        tires = OctoprimeTires(tire_wear)
        self.assertFalse(tires.needs_service())
