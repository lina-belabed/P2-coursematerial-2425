# Write your code here
class BMICalculator:
    def __init__(self, weight_in_kg, height_in_m):
        self.__weight_in_kg = weight_in_kg
        self.__height_in_m = height_in_m
    
    @property
    def weight_in_kg(self):
        return self.__weight_in_kg
    
    @property
    def height_in_m(self):
        return self.__height_in_m
    
    @property
    def bmi(self):
        bmi = self.__weight_in_kg / self.__height_in_m**2
        return bmi
    
    @property
    def category(self):
        if self.bmi < 18.5:
            return "underweight"
        elif 18.5 < self.bmi < 25:
            return "normal"
        else:
            return "overweight"
        

calc = BMICalculator(weight_in_kg=80, height_in_m=1.80)
print(calc.bmi)
print(calc.category)