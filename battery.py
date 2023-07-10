from datetime import datetime, timedelta
from engine.model.battery import Battery

class SpindlerBattery(Battery):
    def __init__(self, charge):
        super().__init__(charge)
        self.last_service_date = datetime.now().date()

    def needs_service(self):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 3)
        return datetime.now().date() >= service_threshold_date
