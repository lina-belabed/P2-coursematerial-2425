# Write your code here
class Time:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    @property
    def hours(self):
        return self.__hours
    
    @hours.setter
    def hours(self, h_value):
        if 0 > h_value or h_value > 23:
            raise ValueError
        self.__hours = h_value

    @property
    def minutes(self):
        return self.__minutes
    
    @minutes.setter
    def minutes(self, m_value):
        if 0 > m_value or m_value > 59:
            raise ValueError
        self.__minutes = m_value

    @property
    def seconds(self):
        return self.__seconds
    
    @seconds.setter
    def seconds(self, s_value):
        if 0 > s_value or s_value > 59:
            raise ValueError
        self.__seconds = s_value

# time = Time(0, 0, 0)
# time.hours = 8
# print(time.hours)
# time.hours = -1
# print(time.hours)
# time.hours = 24
# print(time.hours)