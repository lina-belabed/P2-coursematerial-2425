class LengthConverter:
    def __init__(self, distance_in_meter, distance_in_inch, distance_in_feet):
        self.distance_in_meter = distance_in_meter
        self.distance_in_inch = distance_in_inch
        self.distance_in_feet = distance_in_feet
    
    @property
    def meter(self):
        return self.distance_in_meter
    
    @meter.setter
    def meter(self, value):
        pass