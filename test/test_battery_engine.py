import unittest
from engine.model.battery import Battery
from engine.model.engine import Engine

class TestBattery(unittest.TestCase):
    def test_battery_initial_charge(self):
        battery = Battery(100)
        self.assertEqual(battery.get_charge(), 100)

    def test_battery_charge_after_drain(self):
        battery = Battery(100)
        battery.drain(50)
        self.assertEqual(battery.get_charge(), 50)

    def test_battery_charge_after_recharge(self):
        battery = Battery(100)
        battery.drain(50)
        battery.recharge(25)
        self.assertEqual(battery.get_charge(), 75)


class TestEngine(unittest.TestCase):
    def test_engine_initial_status(self):
        engine = Engine()
        self.assertFalse(engine.is_running())

    def test_engine_start(self):
        engine = Engine()
        engine.start()
        self.assertTrue(engine.is_running())

    def test_engine_stop(self):
        engine = Engine()
        engine.start()
        engine.stop()
        self.assertFalse(engine.is_running())


if __name__ == '__main__':
    unittest.main()
